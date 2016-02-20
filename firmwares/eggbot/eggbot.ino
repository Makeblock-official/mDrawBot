#include <MeOrion.h>
#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <Wire.h>

// data stored in eeprom
union{
    struct{
      char name[8];
      unsigned char motoADir;
      unsigned char motoBDir;
      int speed;
      int penUpPos;
      int penDownPos;
    }data;
    char buf[64];
}roboSetup;

// arduino only handle A,B step mapping
float curSpd,tarSpd; // speed profile
float curX,curY,curZ;
float tarX,tarY,tarZ; // target xyz position
// step value
int tarA,tarB,posA,posB; // target stepper position
int8_t motorAfw,motorAbk;
int8_t motorBfw,motorBbk;

MePort stpA(PORT_1);
MePort stpB(PORT_2);
MePort ylimit(PORT_3);
int ylimit_pin1 = ylimit.pin1();
int ylimit_pin2 = ylimit.pin2();
MePort xlimit(PORT_6);
int xlimit_pin1 = xlimit.pin1();
int xlimit_pin2 = xlimit.pin2();
MeDCMotor laser(M2);
MePort servoPort(PORT_7);
int servopin =  servoPort.pin2();
Servo servoPen;

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


/************** calculate movements ******************/
//#define STEPDELAY_MIN 200 // micro second
//#define STEPDELAY_MAX 1000
long stepAuxDelay=0;
int stepdelay_min=500;
int stepdelay_max=2000;
#define YRATIO 5
#define ACCELERATION 2 // mm/s^2 don't get inertia exceed motor could handle
#define SEGMENT_DISTANCE 10 // 1 mm for each segment
#define SPEED_STEP 1

void doMove()
{
  long mDelay=stepdelay_max;
  int speedDiff = -SPEED_STEP;
  int dA,dB,maxD;
  float stepA,stepB,cntA=0,cntB=0;
  int d;
  dA = tarA - posA;
  dB = tarB - posB;
  maxD = max(abs(dA),abs(dB));
  stepA = (float)abs(dA)/(float)maxD;
  stepB = (float)abs(dB)/(float)maxD;
  //Serial.printf("target: %d %d\n",tarA,tarB);
  //Serial.printf("move: max:%d da:%d db:%d\n",maxD,dA,dB);
  //Serial.print(stepA);Serial.print(' ');Serial.println(stepB);
  for(int i=0;(posA!=tarA)||(posB!=tarB);i++){                         // Robbo1 2015/6/8 Changed - change loop terminate test to test for moving not finished rather than a preset amount of moves
    //Serial.printf("step %d A:%d B;%d tar:%d %d\n",i,posA,posB,tarA,tarB);
    // move A
    if(posA!=tarA){
      cntA+=stepA;
      if(cntA>=1){
        d = dA>0?motorAfw:motorAbk;
        posA+=(dA>0?1:-1);
        stepperMoveA(d);
        cntA-=1;
      }
    }
    // move B
    if(posB!=tarB){
      cntB+=stepB;
      if(cntB>=1){
        d = dB>0?motorBfw:motorBbk;
        posB+=(dB>0?1:-1);
        stepperMoveB(d);
        cntB-=1;
      }
    }
    mDelay=constrain(mDelay+speedDiff,stepdelay_min,stepdelay_max)+stepAuxDelay;
    if(mDelay > 10000)
    {
      delay(mDelay/1000);
      delayMicroseconds(mDelay%1000);
    }
    else
    {
      delayMicroseconds(mDelay);
    }
    if((maxD-i)<((stepdelay_max-stepdelay_min)/SPEED_STEP)){
      speedDiff=SPEED_STEP;
    }
  }
  //Serial.printf("finally %d A:%d B;%d\n",maxD,posA,posB);
  posA = tarA;
  posB = tarB;
}

/******** mapping xy position to steps ******/
#define STEPS_PER_CIRCLE 3200.0f
void prepareMove()
{
  int maxD;
  unsigned long t0,t1;
  float dx = tarX - curX;
  float dy = tarY - curY;
  float distance = sqrt(dx*dx+dy*dy);
  float distanceMoved=0,distanceLast=0;
  //Serial.print("distance=");Serial.println(distance);
  if (distance < 0.001)
    return;
  tarA = tarX*STEPS_PER_CIRCLE/360;
  tarB = tarY*STEPS_PER_CIRCLE/360*YRATIO;
  
  doMove();
  curX = tarX;
  curY = tarY;
}

void initPosition()
{
  curX=0; curY=60;
  posA = 0;
  posB = (STEPS_PER_CIRCLE*curY/360*YRATIO);
}

/************** calculate movements ******************/
void parseCordinate(char * cmd)
{
  char * tmp;
  char * str;

  tarX = curX;
  tarY = curY;
  str = strtok_r(cmd, " ", &tmp);             // Robbo1 2015/6/8 comment - this removes the G code token from the input string - potential for future errors if method of processing G codes changes
  while((str=strtok_r(0, " ", &tmp))!=NULL){  // Robbo1 2015/6/8 changed - placed strtok_r into loop test so that the pointer tested is the one used in the current loop
    //str = strtok_r(0, " ", &tmp);           // Robbo1 2015/6/8 removed - removed from here and place in the while loop test

    //Serial.printf("%s;",str);
    if(str[0]=='X'){
      tarX = atof(str+1);
      //Serial.print("tarX ");Serial.print(tarX);
    }else if(str[0]=='Y'){
      tarY = atof(str+1);
      //Serial.print("tarY ");Serial.print(tarY);
    }else if(str[0]=='Z'){
      tarZ = atof(str+1);
    }else if(str[0]=='F'){
      float speed = atof(str+1);
      tarSpd = speed/60; // mm/min -> mm/s
    }else if(str[0]=='A'){
      stepAuxDelay = atol(str+1);
    }
  }
  //Serial.print("G1 ");Serial.print(tarX);Serial.print(" ");Serial.println(tarY);
  prepareMove();
}

void echoRobotSetup()
{
  Serial.print("M10 EGG ");
  Serial.print(STEPS_PER_CIRCLE);
  Serial.print(' ');Serial.print(curX);
  Serial.print(' ');Serial.print(curY);
  Serial.print(" A");Serial.print((int)roboSetup.data.motoADir);
  Serial.print(" B");Serial.print((int)roboSetup.data.motoBDir);
  Serial.print(" S");Serial.print((int)roboSetup.data.speed);
  Serial.print(" U");Serial.print((int)roboSetup.data.penUpPos);
  Serial.print(" D");Serial.println((int)roboSetup.data.penDownPos);
}

void parseAuxDelay(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  stepAuxDelay = atol(tmp);
}

void parseLaserPower(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pwm = atoi(tmp);
  laser.run(pwm);
}

void parsePen(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pos = atoi(tmp);
  servoPen.write(pos);
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
      //Serial.print("motorADir ");Serial.print(roboSetup.data.motoADir);
    }else if(str[0]=='B'){
      roboSetup.data.motoBDir = atoi(str+1);
      //Serial.print("motoBDir ");Serial.print(roboSetup.data.motoBDir);
    }else if(str[0]=='D'){
      roboSetup.data.speed = atoi(str+1);
      //Serial.print("Speed ");Serial.print(roboSetup.data.speed);
    }
  }
  syncRobotSetup();
}

void parsePenPosSetup(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  while(str!=NULL){
    str = strtok_r(0, " ", &tmp);
    if(str[0]=='U'){
      roboSetup.data.penUpPos = atoi(str+1);
    }else if(str[0]=='D'){
      roboSetup.data.penDownPos = atoi(str+1);    
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
      parsePen(cmd);
      break;
    case 2: // set pen position
      parsePenPosSetup(cmd);
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
    case 10:
      echoRobotSetup();
      break;
  }
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
      tarX=0; tarY=60;
      prepareMove();
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
  if(strncmp(roboSetup.data.name,"EGG3",4)!=0){
    Serial.println("set to default setup");
    // set to default setup
    memset(roboSetup.buf,0,64);
    memcpy(roboSetup.data.name,"EGG3",4);
    roboSetup.data.motoADir = 0;
    roboSetup.data.motoBDir = 0;
    syncRobotSetup();
  }
  if(roboSetup.data.motoADir==0){
    motorAfw=1;motorAbk=-1;
  }else{
    motorAfw=-1;motorAbk=1;
  }
  if(roboSetup.data.motoBDir==0){
    motorBfw=-1;motorBbk=1;
  }else{
    motorBfw=1;motorBbk=-1;
  }
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
  initPosition();
  servoPen.attach(servopin);
  servoPen.write(0);
}

char buf[64];
char bufindex;
char buf2[64];
char bufindex2;

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

