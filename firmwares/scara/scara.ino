#include <Makeblock.h>
#include <EEPROM.h>
#include <Servo.h>
#include <SoftwareSerial.h>
#include <Wire.h>

/*
	Version		1.0.1
	HISTORY
		Date			Author		Changes
		----			------		-------
		2015/June/8   - Robbo1		Fixed error with parameters being corrupted during the decoding of the cmd line  (Scara seemed to have a mind of its own)
		2015/June/8   - Robbo1		Fixed potential buffer overflow problem if newline character was ever corrupted/lost
		2015/June/8   - Robbo1		Fixed positional accuracy error.  Caused by using a test that allowed for finishing moving before all stepping complete
		
		
*/

// data stored in eeprom
union{
    struct{
      char name[8];
      unsigned char motoADir;
      unsigned char motoBDir;
      int arm0len;
      int arm1len;
      int speed;
    }data;
    char buf[64];
}roboSetup;

// arduino only handle A,B step mapping
float curSpd,tarSpd; // speed profile
float curX,curY,curZ;
float tarX,tarY,tarZ; // target xyz position
float curTh1, curTh2;
float tarTh1, tarTh2; // target angle of joint
int tarA,tarB,posA,posB; // target stepper position
int8_t motorAfw,motorAbk;
int8_t motorBfw,motorBbk;
MePort stpB(PORT_2);
MePort stpA(PORT_1);
MeDCMotor laser(M2);
MePort servoPort(PORT_7);
int servopin =  servoPort.pin2();
Servo servoPen;

#define ARML1 168
#define ARML2 206
/************** motor movements ******************/
void stepperMoveA(int dir)
{
//  Serial.printf("stepper A %d\n",dir);
  if(dir>0){
    stpA.dWrite1(LOW);
  }else{
    stpA.dWrite1(HIGH);
  }
  stpA.dWrite2(HIGH);
  stpA.dWrite2(LOW);
}

void stepperMoveB(int dir)
{
//  Serial.printf("stepper B %d\n",dir);
  if(dir>0){
    stpB.dWrite1(LOW);
  }else{
    stpB.dWrite1(HIGH);
  }
  stpB.dWrite2(HIGH);
  stpB.dWrite2(LOW);
}

/************** scara inversekinect **********************/
// th1 solution
//2*atan((2*L1*y + (- L1^4 + 2*L1^2*L2^2 + 2*L1^2*x^2 + 2*L1^2*y^2 - L2^4 + 2*L2^2*x^2 + 2*L2^2*y^2 - x^4 - 2*x^2*y^2 - y^4)^(1/2))/(L1^2 - 2*L1*x - L2^2 + x^2 + y^2))
// th2 solution
//2*atan(((- L1^2 + 2*L1*L2 - L2^2 + x^2 + y^2)*(L1^2 + 2*L1*L2 + L2^2 - x^2 - y^2))^(1/2)/(L1^2 + 2*L1*L2 + L2^2 - x^2 - y^2))
float th1,th2;
void scaraInverseKinect(float x, float y)
{
  float L1 = roboSetup.data.arm0len;
  float L2 = roboSetup.data.arm1len;
  //Serial.print("x ");Serial.println(x);
  //Serial.print("y ");Serial.println(y);
  th1 = 2*atan((2*L1*y + sqrt(- L1*L1*L1*L1 + 2*L1*L1*L2*L2 + 2*L1*L1*x*x + 2*L1*L1*y*y - L2*L2*L2*L2 + 2*L2*L2*x*x + 2*L2*L2*y*y - x*x*x*x - 2*x*x*y*y - y*y*y*y))/(L1*L1 - 2*L1*x - L2*L2 + x*x + y*y));
  th2 = 2*atan(sqrt((- L1*L1 + 2*L1*L2 - L2*L2 + x*x + y*y)*(L1*L1 + 2*L1*L2 + L2*L2 - x*x - y*y))/(L1*L1 + 2*L1*L2 + L2*L2 - x*x - y*y));
  //Serial.print("th1 ");Serial.println(th1/PI*180);
  //Serial.print("th2 ");Serial.println(th2/PI*180);
}

#define STEPS_PER_CIRCLE 16000.0f
long pos1,pos2;
void thetaToSteps(float th1, float th2)
{
  pos1 = round(th1/PI*STEPS_PER_CIRCLE/2);
  pos2 = round(th2/PI*STEPS_PER_CIRCLE/2);
}

/*
	Robbo1 8/June/2015
	
	Fixed loop test where the movement may not have actually stopped
	
	Sympton  - The movement would stop sometimes one step short because of floating point values 
	           not always the exact amount and 'N' additions of 'N' segments may not add up to 
			   the whole.  The best way is to loop until all steps have been done.
			   
	Solution - Change the loop finish test from 'i<maxD' to '(posA!=tarA)||(posB!=tarB)'
	           That is test for movement not yet finished
			   This is a miniminal change to enable the least changes to the code
			   
*/
/************** calculate movements ******************/
//#define STEPDELAY_MIN 200 // micro second
//#define STEPDELAY_MAX 1000
int stepAuxDelay=0;
int stepdelay_min=200;
int stepdelay_max=2000;
#define ACCELERATION 2 // mm/s^2 don't get inertia exceed motor could handle
#define SEGMENT_DISTANCE 10 // 1 mm for each segment
#define SPEED_STEP 1

void doMove()
{
  int mDelay=stepdelay_max;
  int speedDiff = -SPEED_STEP;
  int dA,dB,maxD;
  float stepA,stepB,cntA=0,cntB=0;
  int d;
  dA = tarA - posA;
  dB = tarB - posB;
  maxD = max(abs(dA),abs(dB));
  stepA = (float)abs(dA)/(float)maxD;
  stepB = (float)abs(dB)/(float)maxD;
  //Serial.printf("move: max:%d da:%d db:%d\n",maxD,dA,dB);
  //Serial.print(stepA);Serial.print(' ');Serial.println(stepB);
  //for(int i=0;i<=maxD;i++){
  //for(int i=0;i<maxD;i++){                                           // Robbo1 2015/6/8 Removed - kept for now to show what the loop looked like before
  for(int i=0;(posA!=tarA)||(posB!=tarB);i++){                         // Robbo1 2015/6/8 Changed - change loop terminate test to test for moving not finished rather than a preset amount of moves
    //Serial.printf("step %d A:%d B;%d\n",i,posA,posB);
    // move A
    if(posA!=tarA){
      cntA+=stepA;
      if(cntA>=1){
        d = dA>0?motorAfw:motorAbk;
        stepperMoveA(d);
        cntA-=1;
        posA+=d;
      }
    }
    // move B
    if(posB!=tarB){
      cntB+=stepB;
      if(cntB>=1){
        d = dB>0?motorBfw:motorBbk;
        stepperMoveB(d);
        cntB-=1;
        posB+=d;
      }
    }
    mDelay=constrain(mDelay+speedDiff,stepdelay_min,stepdelay_max)+stepAuxDelay;
    delayMicroseconds(mDelay);
    if((maxD-i)<((stepdelay_max-stepdelay_min)/SPEED_STEP)){
      speedDiff=SPEED_STEP;
    }
  }
  //Serial.printf("finally %d A:%d B;%d\n",maxD,posA,posB);
  posA = tarA;
  posB = tarB;
}

void prepareMove()
{
  int maxD;
  unsigned long t0,t1;
  float segInterval;
  float dx = tarX - curX;
  float dy = tarY - curY;
  float distance = sqrt(dx*dx+dy*dy);
  float distanceMoved=0,distanceLast=0;
  //Serial.print("distance=");Serial.println(distance);
  if (distance < 0.001) 
    return;
  scaraInverseKinect(tarX,tarY);
  thetaToSteps(th1, th2);
  tarA = pos1;tarB = pos2;
  //Serial.print("theta:");Serial.print(th1/PI*180);Serial.print(' ');Serial.println(th2/PI*180);
  //Serial.printf("tar Pos %d %d\r\n",tarA,tarB);
  doMove();
  curX = tarX;
  curY = tarY;
}

void initPosition()
{
  curX=-(roboSetup.data.arm0len+roboSetup.data.arm1len-0.01); curY=0;
  scaraInverseKinect(curX,curY);
  curTh1=th1;curTh2=th2;
  thetaToSteps(curTh1,curTh2);
  posA = pos1;
  posB = pos2;
}

/*
	Robbo1 8/June/2015
	
	Fixed loop test where phantom parameters overwrite actual parameters and cause wild motions in scara
	
	Sympton  - The test was testing the previous loop's pointer and when last token/parameter is processed 
	           It would then loop one more time.  This meant that the loop used the NULL pointer as the 
			   string pointer.  Now if the bytes at address zero happened to start with the characters X or Y or Z or F or A
			   the loop would process that phantom string and convert the following bytes into a number and 
			   replace the actual parameters value with the phantom one.
			  
			   While this happened only in certain circumstances, it did happen for some svg files that 
			   happened to be placed in certain areas, because it seems the conversion codes would place 
			   intermediate data at addres 0 and if that data resulted in the byte at addres 0 being
			   one of the parameter labels (X Y Z F A) then the problem occurred.
			  
			   This explains why some people had wild things happen with the arms rotating all the way and 
			   crashing into the framework
			  
	Solution - Move the strtok_r to the while loop test which means that the loop test is done on the
	           current pointer.  This means that when there are no more tokens (str == NULL) the loop
			   terminates without processing it.
			   
	Other identified issues
				If the code is changed prior to calling the function, the initial strtok_r may gobble 
				up a parameter.  It is currently there because the "G" code is not removed from the 
				cmd string prior to calling the function and has to be removed prior to processing the
				parameters.
				
*/

/************** calculate movements ******************/
void parseCordinate(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);             // Robbo1 2015/6/8 comment - this removes the G code token from the input string - potential for future errors if method of processing G codes changes
  while((str=strtok_r(0, " ", &tmp))!=NULL){  // Robbo1 2015/6/8 changed - placed strtok_r into loop test so that the pointer tested is the one used in the current loop
    //str = strtok_r(0, " ", &tmp);           // Robbo1 2015/6/8 removed - removed from here and place in the while loop test
    //Serial.printf("%s;",str);
    if(str[0]=='X'){
      tarX = atof(str+1);
    }else if(str[0]=='Y'){
      tarY = atof(str+1);
    }else if(str[0]=='Z'){
      tarZ = atof(str+1);
    }else if(str[0]=='F'){
      float speed = atof(str+1);
      tarSpd = speed/60; // mm/min -> mm/s
    }else if(str[0]=='A'){
      stepAuxDelay = atoi(str+1);
    }
  }
  prepareMove();
}


void parseServo(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pos = atoi(tmp);
  servoPen.write(pos);
}

void parseAuxDelay(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  stepAuxDelay = atoi(tmp);
}

void parseLaserPower(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pwm = atoi(tmp);
  laser.run(pwm);
}

void parseGcode(char * cmd)
{
  int code;
  code = atoi(cmd);
  switch(code){
    case 1: // xyz move
      parseCordinate(cmd);
      break;
    case 28: // home
      stepAuxDelay = 0;
      tarX=-(roboSetup.data.arm0len+roboSetup.data.arm1len-0.01); tarY=0;
      prepareMove();
      break; 
  }
}

void echoArmSetup(char * cmd)
{
  Serial.print("M10 MSCARA ");
  Serial.print(roboSetup.data.arm0len);Serial.print(' ');
  Serial.print(roboSetup.data.arm1len);Serial.print(' ');
  Serial.print(curX);Serial.print(' ');
  Serial.print(curY);Serial.print(' ');
  Serial.print("A");Serial.print((int)roboSetup.data.motoADir);
  Serial.print(" B");Serial.print((int)roboSetup.data.motoBDir);
  Serial.print(" D");Serial.println((int)roboSetup.data.speed);
}

void parseRobotSetup(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  while(str!=NULL){
    str = strtok_r(0, " ", &tmp);
    if(str[0]=='A'){
      roboSetup.data.motoADir = atoi(str+1);
      Serial.print("motorADir ");Serial.print(roboSetup.data.motoADir);
    }else if(str[0]=='B'){
      roboSetup.data.motoBDir = atoi(str+1);
      Serial.print("motoBDir ");Serial.print(roboSetup.data.motoBDir);
    }else if(str[0]=='M'){
      roboSetup.data.arm0len = atoi(str+1);
      Serial.print("ARML1 ");Serial.print(roboSetup.data.arm0len);
    }else if(str[0]=='N'){
      roboSetup.data.arm1len = atoi(str+1);
      Serial.print("ARML2 ");Serial.print(roboSetup.data.arm1len);
    }else if(str[0]=='D'){
      roboSetup.data.speed = atoi(str+1);
      Serial.print("Speed ");Serial.print(roboSetup.data.speed);
    }
  }
  syncRobotSetup();
}


void parseMcode(char * cmd)
{
  int code;
  code = atoi(cmd);
  switch(code){
    case 1:
      parseServo(cmd);
      break;
    case 2:
    
      break;
    case 3:
      parseAuxDelay(cmd);
      break;
    case 4:
      parseLaserPower(cmd);
      break;
    case 5:
      parseRobotSetup(cmd);
      break;
    case 10: // echo robot config
      echoArmSetup(cmd);
      break;
  }

}


void parseCmd(char * cmd)
{
  if(cmd[0]=='G'){ // gcode
    parseGcode(cmd+1);  
  }else if(cmd[0]=='M'){ // mcode
    parseMcode(cmd+1);
  }else if(cmd[0]=='P'){
    Serial.print("POS X");Serial.print(curX);Serial.print(" Y");Serial.println(curY);
  }
  Serial.println("OK");
}

// local data
void initRobotSetup()
{
  int i;
  //Serial.println("read eeprom");
  for(i=0;i<64;i++){
    roboSetup.buf[i] = EEPROM.read(i);
    //Serial.print(roboSetup.buf[i],16);Serial.print(' ');
  }
  //Serial.println();
  if(strncmp(roboSetup.data.name,"SCARA3",6)!=0){
    Serial.println("set to default setup");
    // set to default setup
    memset(roboSetup.buf,0,64);
    memcpy(roboSetup.data.name,"SCARA3",6);
    roboSetup.data.motoADir = 0;
    roboSetup.data.motoBDir = 0;
    roboSetup.data.arm0len = ARML1;
    roboSetup.data.arm1len = ARML2;
    roboSetup.data.speed = 80;
    syncRobotSetup();
  }
  // init motor direction
  if(roboSetup.data.motoADir==0){
    motorAfw=1;motorAbk=-1;
  }else{
    motorAfw=-1;motorAbk=1;
  }
  if(roboSetup.data.motoBDir==0){
    motorBfw=1;motorBbk=-1;
  }else{
    motorBfw=-1;motorBbk=1;
  }
  int spd = 100 - roboSetup.data.speed;
  stepdelay_min = spd*10;
  stepdelay_max = spd*100;
  //Serial.printf("spd %d %d\n",stepdelay_min,stepdelay_max);
}

void syncRobotSetup()
{
  int i;
  for(i=0;i<64;i++){
    EEPROM.write(i,roboSetup.buf[i]);
  }
}

/************** arduino ******************/
void setup() {
  Serial.begin(115200);
  initRobotSetup();
  servoPen.attach(servopin);
  servoPen.write(10);
  initPosition();
}

char buf[64];
char bufindex;
char buf2[64];
char bufindex2;

/*
	Robbo1 8/June/2015
	
	Fixed potential probelms from buffer overflow and first cmd string not being null terminated
	
*/

void loop() {
  if(Serial.available()){
    char c = Serial.read();
    //buf[bufindex++]=c;                 // Robbo1 2015/6/8 Removed - Do not store the \n
    if(c=='\n'){
      buf[bufindex++]='\0';              // Robbo1 2015/6/8 Add     - Null terminate the string - Essential for first use of 'buf' and good programming practice
      parseCmd(buf);
      memset(buf,0,64);
      bufindex = 0;
    }else if(bufindex<64){               // Robbo1 2015/6/8 Add     - Only add char to string if the string can fit it and still be null terminated 
      buf[bufindex++]=c;                 // Robbo1 2015/6/8 Moved   - Store the character here now
	}
  }

}
