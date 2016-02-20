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
      unsigned char motorSwitch;
      int hangPos;
      int width;
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
// string length
float curL,curR;
float tarL,tarR;
// step value
int tarA,tarB,posA,posB; // target stepper position
int8_t motorAfw,motorAbk;
int8_t motorBfw,motorBbk;

MePort stpB(PORT_1);
MePort stpA(PORT_2);
MePort servoPort(PORT_7);
MeDCMotor laser(M2);
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
int stepdelay_min=400;
int stepdelay_max=3000;
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

  //for(int i=0;i<=maxD;i++){
  for(int i=0;(posA!=tarA)||(posB!=tarB);i++){                         // Robbo1 2015/6/8 Changed - change loop terminate test to test for moving not finished rather than a preset amount of moves
    //Serial.printf("step %d A:%d B;%d\n",i,posA,posB);
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
#define WIDTH 700 // width between stepper axis
#define HANGPOS 500 // the init hang position
#define DIAMETER 58 // the diameter of stepper wheel
#define STEPS_PER_MM (STEPS_PER_CIRCLE/PI/DIAMETER) 
float initString;
void prepareMove()
{
  int maxD;
  unsigned long t0,t1;
  float segInterval;
  tarX = -tarX; // fix for x axis direction
  float dx = tarX - curX;
  float dy = tarY - curY;
  float distance = sqrt(dx*dx+dy*dy);
  float distanceMoved=0,distanceLast=0;
  //Serial.print("distance=");Serial.println(distance);
  if (distance < 0.1)
    return;
  // map xy to string length
  float Lx = tarX+roboSetup.data.width/2;
  float Ly = roboSetup.data.hangPos-tarY;
  tarL = sqrt(Lx*Lx+Ly*Ly);
  float Rx = roboSetup.data.width/2-tarX;
  float Ry = roboSetup.data.hangPos-tarY;
  tarR = sqrt(Rx*Rx+Ry*Ry);
  tarA = (tarL-initString)*STEPS_PER_MM; // fix the direction of steppers
  tarB = -(tarR-initString)*STEPS_PER_MM;
  //Serial.print("tarL:");Serial.print(tarL);Serial.print(' ');Serial.print("tarR:");Serial.println(tarR);
  //Serial.print("curL:");Serial.print(curL);Serial.print(' ');Serial.print("curR:");Serial.println(curR);
  //Serial.print("tarA:");Serial.print(tarA);Serial.print(' ');Serial.print("tarB:");Serial.println(tarB);
  //Serial.print("posA:");Serial.print(posA);Serial.print(' ');Serial.print("posB:");Serial.println(posB);
  doMove();
  curL = tarL;
  curR = tarR;
  curX = tarX;
  curY = tarY;
}

void initPosition()
{
  float x,y;
  curX=0; curY=0;
  posA = 0;posB = 0;
  x = roboSetup.data.width/2;
  y = roboSetup.data.hangPos;
  initString = curR = curL = sqrt(x*x+y*y);
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

void parseLaserPower(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pwm = atoi(tmp);
  laser.run(pwm);
}

void parseAuxDelay(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  stepAuxDelay = atol(tmp);
}

void parsePen(char * cmd)
{
  char * tmp;
  char * str;
  str = strtok_r(cmd, " ", &tmp);
  int pos = atoi(tmp);
  servoPen.write(pos);
}

void echoRobotSetup()
{
  Serial.print("M10 MSPIDER ");
  Serial.print(roboSetup.data.hangPos);Serial.print(' ');
  Serial.print(roboSetup.data.width);Serial.print(' ');
  Serial.print(curX);Serial.print(' ');
  Serial.print(curY);Serial.print(' ');
  Serial.print("A");Serial.print((int)roboSetup.data.motoADir);
  Serial.print(" B");Serial.print((int)roboSetup.data.motoBDir);
  Serial.print(" H");Serial.print((int)roboSetup.data.motorSwitch);
  Serial.print(" S");Serial.print((int)roboSetup.data.speed);
  Serial.print(" U");Serial.print((int)roboSetup.data.penUpPos);
  Serial.print(" D");Serial.println((int)roboSetup.data.penDownPos);
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
    }else if(str[0]=='B'){
      roboSetup.data.motoBDir = atoi(str+1);
    }else if(str[0]=='H'){
      roboSetup.data.hangPos = atoi(str+1);
    }else if(str[0]=='W'){
      roboSetup.data.width = atoi(str+1);
    }else if(str[0]=='S'){
      roboSetup.data.speed = atoi(str+1);
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
  //Serial.printf("M2 U:%d D:%d\r\n",roboSetup.data.penUpPos,roboSetup.data.penDownPos);
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
      tarX=0; tarY=0;
      prepareMove();
      break; 
  }
}

void parseCmd(char * cmd)
{
  if(cmd[0]=='G'){ // gcode
    parseGcode(cmd+1); 
    Serial.println("OK");
  }else if(cmd[0]=='M'){ // mcode
    parseMcode(cmd+1);
    Serial.println("OK");
  }
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
  if(strncmp(roboSetup.data.name,"SPIDER1",7)!=0){
    Serial.println("set to default setup");
    // set to default setup
    memset(roboSetup.buf,0,64);
    memcpy(roboSetup.data.name,"SPIDER1",7);
    roboSetup.data.motoADir = 0;
    roboSetup.data.motoBDir = 0;
    roboSetup.data.motorSwitch = 0;
    roboSetup.data.hangPos = HANGPOS;
    roboSetup.data.width = WIDTH;
    roboSetup.data.speed = 90;
    roboSetup.data.penUpPos = 160;
    roboSetup.data.penDownPos = 90;
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
  //int spd = 100 - roboSetup.data.speed;
  //stepdelay_min = spd*10;
  //stepdelay_max = spd*100;
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
  initPosition();
  delay(100);
  servoPen.write(roboSetup.data.penUpPos);
}

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
