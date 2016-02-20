#include <MeOrion.h>
#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <Wire.h>

MePort stpB(PORT_1);
MePort stpA(PORT_2);
MePort servoPort(PORT_7);
int servopin =  servoPort.pin2();
Servo servoPen;

// data stored in eeprom
union{
    struct{
      char name[8];
      int width;
      int useHermit;
      int penUpPos;
      int penDownPos;
    }data;
    char buf[64];
}roboSetup;

// arduino only handle A,B step mapping
float curX,curY,curZ;
float tarX,tarY,tarZ; // target xyz position
float curVecX,curVecY;
float tarVecX,tarVecY;
// step value
long curA,curB;
long tarA,tarB;
float curD,tarD; // target direction
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
int stepdelay_min=200;
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
  dA = tarA - curA;
  dB = tarB - curB;
  maxD = max(abs(dA),abs(dB));
  stepA = (float)abs(dA)/(float)maxD;
  stepB = (float)abs(dB)/(float)maxD;
  //Serial.printf("move: max:%d da:%d db:%d\n",maxD,dA,dB);
  //Serial.print(stepA);Serial.print(' ');Serial.println(stepB);
  for(int i=0;i<=maxD;i++){
    //Serial.printf("step %d A:%d B;%d\n",i,posA,posB);
    // move A
    if(curA!=tarA){
      cntA+=stepA;
      if(cntA>=1){
        d = dA>0?1:-1;
        stepperMoveA(d);
        cntA-=1;
        curA+=d;
      }
    }
    // move B
    if(curB!=tarB){
      cntB+=stepB;
      if(cntB>=1){
        d = dB>0?1:-1;
        stepperMoveB(d);
        cntB-=1;
        curB+=d;
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
  curA = tarA;
  curB = tarB;
}

//#define A 0.5f //tangents tightness
float tmpVecX,tmpVecY;
void calcVector(float x0, float y0, float x, float y)
{
  float dx = x-x0;
  float dy = y-y0;
  float dis = sqrt(dx*dx+dy*dy);
  tmpVecX = dx/dis;
  tmpVecY = dy/dis;
}

float hx,hy;
void updateHermitVector(float s)
{
  float h1,h2,h3,h4;
  h1 = 2*s*s*s-3*s*s+1;  
  h2 = -2*s*s*s+3*s*s;
  h3 = s*s*s-2*s*s+s;
  h4 = s*s*s-s*s;
  hx = h1*curX+h2*tarX+h3*curVecX+h4*tarVecX;
  hy = h1*curY+h2*tarY+h3*curVecY+h4*tarVecY;
}

#define STEPS_PER_CIRCLE 3200 // 200*16
#define DIAMETER 64.0 // wheel diameter mm
#define WIDTH 141 // distance between wheel
#define STEP_PER_MM (STEPS_PER_CIRCLE/PI/DIAMETER)
void prepareMove()
{
  int segs,i;
  unsigned long t0,t1;
  float ang0,x0,y0;
  float ang,dLeft,dRight;
  float dx = tarX - curX;
  float dy = tarY - curY;
  float distance = sqrt(dx*dx+dy*dy);

  tarD = atan2(dy,dx);
  if(tarD>PI)
  {
    tarD-=(2*PI);
  }
  else if(tarD<-PI)
  {
      tarD+=(2*PI);
  }

  calcVector(curX,curY,tarX,tarY);
  tarVecX = tmpVecX;  tarVecY = tmpVecY;
 
  if (distance < 0.001)
  {
    return;
  }
  if(roboSetup.data.useHermit==0) // algorithm for normal straight line
  {
    float dAng = tarD - curD;
    if(dAng>PI)
    {
      dAng-=(2*PI);
    }
    else if(dAng<-PI)
    {
      dAng+=(2*PI);
    }
    float dL = (dAng)/2*roboSetup.data.width;
    float dStep = dL*STEP_PER_MM;
    tarA = curA+dStep;
    tarB = curB+dStep;
    //Serial.print("dir:"); Serial.print((tarD)/PI*180);
    //Serial.print(" "); Serial.print(dx);Serial.print(" "); Serial.print(dy);Serial.print(" "); Serial.println(dL);
    doMove();
    // move to targe xy position
    dStep = distance*STEP_PER_MM;
    tarA = curA+dStep;
    tarB = curB-dStep;
    //Serial.print("dis:"); Serial.println(distance);
    doMove();
  }
  else // hermit interpolation algorithm
  {
    segs = (int)distance+1;
    x0 = curX; y0=curY;
    //Serial.print("Move:");Serial.print(curVecX);Serial.print(" ");Serial.print(curVecY);Serial.print(" ");Serial.print(tarVecX);Serial.print(" ");Serial.println(tarVecY);
    ang0 = atan2(curVecY,curVecX);
    if(ang0>PI) 
    {
      ang0-=(2*PI);
    }
    for(i=1;i<=segs;i++)
    {
      updateHermitVector((float)i/segs);
      // inverse to left right movement
      dx = hx-x0; dy = hy-y0;
      float dv = sqrt(dx*dx+dy*dy);
      ang = atan2(dy,dx);
      if(ang>PI)
      {
        ang-=(2*PI);
      }
      float dw = ang-ang0;
      if(dw>PI)
      {
        dw-=(2*PI);
      }
      else if(dw<-PI)
      {
        dw+=(2*PI);
      }
      //Serial.print(i);Serial.print("hermit ");Serial.print(hx);Serial.print(" ");Serial.print(hy);Serial.print(" ");Serial.print(dv);Serial.print(" ");Serial.print(dw/PI*180);
      dLeft = (dv+dw/2*roboSetup.data.width)*STEP_PER_MM;
      dRight = (dv-dw/2*roboSetup.data.width)*STEP_PER_MM;
      //Serial.print(" ");Serial.print(dLeft);Serial.print(" ");Serial.println(dRight);
      tarA = curA+dLeft;
      tarB = curB-dRight;
      doMove();
      ang0 = ang;
      x0=hx;y0=hy;
    }
  }
  curD = tarD;
  curX = tarX;
  curY = tarY;
  curVecX = tarVecX;  curVecY = tarVecY;
}

void initPosition()
{
  //servoPen.write(120);
  curX=0; curY=0;
  curA = 0;
  curB = 0;
  curVecX=1;
  curVecY=0;
  curD = 0;
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
    }
  }
  prepareMove();
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
      servoPen.write(roboSetup.data.penUpPos);
      prepareMove();
      initPosition();
      break; 
  }
}

void echoRobotSetup()
{
  Serial.print("M10 MCAR ");
  Serial.print(roboSetup.data.width);Serial.print(' ');
  Serial.print(DIAMETER);Serial.print(' ');
  Serial.print(curX);Serial.print(' ');
  Serial.print(curY);
  Serial.print(" H");Serial.print(roboSetup.data.useHermit);
  Serial.print(" U");Serial.print((int)roboSetup.data.penUpPos);
  Serial.print(" D");Serial.println((int)roboSetup.data.penDownPos);
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
    if(str[0]=='W'){
      roboSetup.data.width = atoi(str+1);
    }else if(str[0]=='H'){
      roboSetup.data.useHermit = atoi(str+1);
    }
  }
  syncRobotSetup();
}

void syncRobotSetup()
{
  int i;
  for(i=0;i<64;i++){
    EEPROM.write(i,roboSetup.buf[i]);
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
  if(strncmp(roboSetup.data.name,"CAR1",4)!=0){
    Serial.println("set to default setup");
    // set to default setup
    memset(roboSetup.buf,0,64);
    memcpy(roboSetup.data.name,"CAR1",4);
    // default connection move inversely
    roboSetup.data.width = WIDTH;
    roboSetup.data.useHermit = 1;
    roboSetup.data.penUpPos = 160;
    roboSetup.data.penDownPos = 90;
    syncRobotSetup();
  }
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
  Serial.print("M2 U:");
  Serial.print(roboSetup.data.penUpPos);
  Serial.print(" D:");
  Serial.println(roboSetup.data.penDownPos);
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
    case 5:
      parseRobotSetup(cmd);
      break;
    case 10:
      echoRobotSetup();
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

/************** arduino ******************/
void setup() {
  Serial.begin(115200);
  servoPen.attach(servopin);
  initRobotSetup();
  initPosition();
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


