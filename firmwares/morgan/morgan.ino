#include <MeOrion.h>
#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <Wire.h>

// morgan struct for mkb internal hackthon

// data stored in eeprom
union{
    struct{
      char name[8];
      unsigned char motoADir;
      unsigned char motoBDir;
      int arm0len;
      int arm1len;
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

float A = 80.0;
float B = 160.0;
float th1,th2;
//2*atan((2*B*y - (-(x^2 + y^2)*(- 4*B^2 + x^2 + y^2))^(1/2))/(x^2 - 2*B*x + y^2))
//2*atan((2*B*y - (-(A^2 - 2*A*x + x^2 + y^2)*(A^2 - 2*A*x - 4*B^2 + x^2 + y^2))^(1/2))/(A^2 - 2*A*x - 2*B*A + x^2 + 2*B*x + y^2))
void morganInverseKinect(float x, float y)
{
  th1 = 2*atan((2*B*y - sqrt(-(x*x + y*y)*(- 4*B*B + x*x + y*y)))/(x*x - 2*B*x + y*y));
  th2 = 2*atan((2*B*y - sqrt(-(A*A - 2*A*x + x*x + y*y)*(A*A - 2*A*x - 4*B*B + x*x + y*y)))/(A*A - 2*A*x - 2*B*A + x*x + 2*B*x + y*y));
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

/************** calculate movements ******************/
//#define STEPDELAY_MIN 200 // micro second
//#define STEPDELAY_MAX 1000
long stepAuxDelay=0;
int stepdelay_min=400;
int stepdelay_max=1000;
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
  //Serial.printf("move: max:%d da:%d db:%d\n",maxD,dA,dB);
  //Serial.print(stepA);Serial.print(' ');Serial.println(stepB);
  //for(int i=0;i<=maxD;i++){
    for(int i=0;i<maxD;i++){
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
  morganInverseKinect(tarX,tarY);
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
  curX = 40;
  curY = 317.49;
  morganInverseKinect(curX,curY);
  curTh1=th1;curTh2=th2;
  thetaToSteps(curTh1,curTh2);
  posA = pos1;
  posB = pos2;
  Serial.print("Init: ");Serial.print(posA);Serial.print(",");Serial.println(posB);
}

/************** calculate movements ******************/
void parseCordinate(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  while(str!=NULL){
    str = strtok_r(0, " ", &tmp);
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
      stepAuxDelay = atol(str+1);
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
  Serial.print(" B");Serial.println((int)roboSetup.data.motoBDir);
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
    }
  }
  syncRobotSetup();
}

void parseColorPalate(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  uint8_t pos = atoi(tmp);
  Wire.beginTransmission(4);
  Wire.write(pos); 
  Wire.endTransmission();
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
    case 11:
      parseColorPalate(cmd);
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
  if(strncmp(roboSetup.data.name,"SCARA",5)!=0){
    Serial.println("set to default setup");
    // set to default setup
    memset(roboSetup.buf,0,64);
    memcpy(roboSetup.data.name,"SCARA",5);
    roboSetup.data.motoADir = 0;
    roboSetup.data.motoBDir = 0;
    roboSetup.data.arm0len = ARML1;
    roboSetup.data.arm1len = ARML2;
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
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(115200);
  initRobotSetup();
  
  servoPen.attach(servopin);
  servoPen.write(10);
  initPosition();

}
int colorPos;
char buf[64];
char bufindex;
char buf2[64];
char bufindex2;

void loop() {
  if(Serial.available()){
    char c = Serial.read();
    buf[bufindex++]=c;
    if(c=='\n'){
      parseCmd(buf);
      memset(buf,0,64);
      bufindex = 0;
    }
  }

}
