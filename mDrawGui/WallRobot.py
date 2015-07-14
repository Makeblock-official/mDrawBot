import sys
import SerialCom
import threading
import queue
import time
from ScaraGui import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from RobotUtils import *
from math import *
import SpiderSetup
# segmentize all path as scara do
def sliceSegment(x,y,tarX,tarY):
    segList=[]
    dx = tarX - x
    dy = tarY - y
    maxD = max(abs(dx),abs(dy))
    maxSteps = int(ceil(maxD)) # 1:1mm per segment, 2:0.5mm
    if maxSteps==0:
        return []
    dxStep = float(dx)/maxSteps
    dyStep = float(dy)/maxSteps
    for i in range(0,maxSteps+1):
        segList.append((x+dxStep*i,y+dyStep*i))
    return segList[1:]

class RobotSetupUI(QWidget):
    def __init__(self,uidialog,robot):
        super(RobotSetupUI, self).__init__()
        self.ui = uidialog()
        self.ui.setupUi(self)
        self.robot = robot
        self.setWindowTitle('Spider Setup')
        self.updateUI()
        self.ui.motoA_CK.mousePressEvent = self.setMotorAck
        self.ui.motoA_CCK.mousePressEvent = self.setMotorAcck
        self.ui.motoB_CK.mousePressEvent = self.setMotorBck
        self.ui.motoB_CCK.mousePressEvent = self.setMotorBcck
        self.ui.btnOk.clicked.connect(self.applySetup)
        #self.ui.btnSwitch.clicked.connect(self.switchMotor)
        self.show()

    def updateUI(self):
        self.ui.lineAB.setText(str(self.robot.width))
        self.ui.lineHeight.setText(str(self.robot.height))
        self.ui.lineScale.setText(str(self.robot.scaler))
        if self.robot.motoADir == 0:
            self.ui.motoA_CK.setStyleSheet(motorSelectedStyle)
            self.ui.motoA_CCK.setStyleSheet("")
        else:
            self.ui.motoA_CK.setStyleSheet("")
            self.ui.motoA_CCK.setStyleSheet(motorSelectedStyle)
        if self.robot.motoBDir == 0:
            self.ui.motoB_CK.setStyleSheet(motorSelectedStyle)
            self.ui.motoB_CCK.setStyleSheet("")
        else:
            self.ui.motoB_CK.setStyleSheet("")
            self.ui.motoB_CCK.setStyleSheet(motorSelectedStyle)

    def switchMotor(self):
        ""

    def applySetup(self):
        self.robot.width = float(str(self.ui.lineAB.text()))
        self.robot.height = float(str(self.ui.lineHeight.text()))
        self.robot.scaler = float(str(self.ui.lineScale.text()))
        self.robot.M5()
        self.hide()
        self.robot.initRobotCanvas()

    def setMotorAck(self,event):
        self.robot.motoADir = 0
        self.updateUI()

    def setMotorAcck(self,event):
        self.robot.motoADir = 1
        self.updateUI()
        
    def setMotorBck(self,event):
        self.robot.motoBDir = 0
        self.updateUI()

    def setMotorBcck(self,event):
        self.robot.motoBDir = 1
        self.updateUI()

class WallRobot(QGraphicsItem):
    
    def __init__(self, scene, ui, parent=None):
        super(WallRobot, self).__init__(parent)
        self.robotState = IDLE
        self.scene = scene
        self.ui = ui
        self.moving = False
        self.laserMode = False
        self.robotCent = None
        #initial params
        self.scaler = 0.5
        self.motorSwitch = 0
        self.width = 960
        self.height = 400
        self.x = 0
        self.y = 0
        self.motoADir = 0
        self.motoBDir = 0
        self.speed = 50
        self.q = queue.Queue()
        self.pXLine = None
        self.pYLine = None
        self.moveList = None
        self.printing = False
        self.pausing = False
        self.lastx = 9999
        self.lasty = 9999
        self.ui.label.setText("X(mm)")
        self.ui.label_2.setText("Y(mm)")
        
    def boundingRect(self):
        return  QRectF(0,0,100,100)
    
    def initRobotCanvas(self):
        self.hang0 = (-self.width/2*self.scaler,-self.height*self.scaler)
        self.hang1 = (self.width/2*self.scaler,-self.height*self.scaler)
        if self.pXLine!=None:
            self.scene.removeItem(self.pXLine)
            self.scene.removeItem(self.pYLine)
        pen = QtGui.QPen(QtCore.Qt.gray)
        pen.setStyle(Qt.DashDotLine)
        self.pXLine = self.scene.addLine(-500+self.robotCent[0],self.robotCent[1],500+self.robotCent[0],self.robotCent[1],pen=pen)
        self.pYLine = self.scene.addLine(self.robotCent[0],self.robotCent[1]-500,self.robotCent[0],self.robotCent[1]+500,pen=pen)
        
        pTxt = self.scene.addText("O")
        cent = QPointF(self.robotCent[0],self.robotCent[1])
        pTxt.setPos(cent)
        pTxt.setDefaultTextColor(QtCore.Qt.darkGray)
        self.ui.labelScale.setText(str(self.scaler))
        
    def paint(self, painter, option, widget=None):
        painter.setBrush(QtCore.Qt.darkGray)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        x = self.x*self.scaler
        y = -self.y*self.scaler
        
        pen = QtGui.QPen(QtGui.QColor(124, 124, 124))
        painter.setPen(pen)
        line = QLineF(self.hang0[0],self.hang0[1],x,y)
        painter.drawLine(line)
        line = QLineF(self.hang1[0],self.hang1[1],x,y)
        painter.drawLine(line)
        
        painter.drawEllipse(-5+self.hang0[0],-5+self.hang0[1],10,10)
        painter.drawText(-10+self.hang0[0],self.hang0[1],"A")
        painter.drawEllipse(-5+self.hang1[0],-5+self.hang1[1],10,10)
        painter.drawText(10+self.hang1[0],self.hang1[1],"B")
        
        pen = QtGui.QPen(QtGui.QColor(0, 169, 231))
        painter.setBrush(QtGui.QColor(0, 169, 231))
        painter.setPen(pen)
        painter.drawEllipse(-5+x,-5+y,10,10)
        
        #painter.drawText(x-30,y+10,"(%.2f,%.2f)" %(x,-y))
        if self.x!=self.lastx or self.y!=self.lasty:
            self.ui.labelXpos.setText("%.2f" %(self.x))
            self.ui.labelYpos.setText("%.2f" %(self.y))
            self.lastx = self.x
            self.lasty = self.y
        
    def parseEcho(self,msg):
        if "M10" in msg:
            tmp = msg.split()
            if tmp[1]!="MSPIDER": return
            self.height = float(tmp[2])
            self.width = float(tmp[3])
            if tmp[6]=="A0":
                self.motoADir = 0
            else:
                self.motoADir = 1
            if tmp[7]=="B0":
                self.motoBDir = 0
            else:
                self.motoBDir = 1
            if msg.find("S")>-1:
                self.speed = int(tmp[9][1:])
            if msg.find("U")>-1:
                self.penUpPos = int(tmp[10][1:])
                self.ui.penUpSpin.setValue(self.penUpPos)
            if msg.find("D")>-1:
                self.penDownPos = int(tmp[11][1:])
                self.ui.penDownSpin.setValue(self.penDownPos)
            self.robotState = IDLE
            self.initRobotCanvas()
    
    def prepareMove(self,target,absolute=False):
        if absolute==False:
            target = (target.x()/self.scaler,-target.y()/self.scaler)
        else:
            target = (target.x(),-target.y())
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = sqrt(dx*dx+dy*dy)
        maxD = max(abs(dx),abs(dy))*0.5
        maxStep = ceil(maxD)
        self.deltaStep = (dx/maxStep,dy/maxStep)
        self.maxStep = maxStep
        print("move to",target,maxStep)
        
    def moveStep(self):
        while True:
            self.x+=self.deltaStep[0]
            self.y+=self.deltaStep[1]
            time.sleep(0.02)
            self.maxStep-=1
            
            if self.maxStep==0 or self.moving==False:
                self.moving = False
                break
    
    def moveTo(self,pos,absolute=False):
        if self.moving:
            self.moving = False
            self.moveThread.join()
        self.prepareMove(pos,absolute)
        self.G1(pos.x()/self.scaler,-pos.y()/self.scaler)
        self.moving = True
        self.moveThread = WorkInThread(self.moveStep)
        self.moveThread.setDaemon(True)
        self.moveThread.start()
        
    def robotGoBusy(self):
        self.robotState = BUSYING
        self.ui.labelMachineState.setText("BUSY")
        
    def M1(self,pos):
        if self.robotState != IDLE: return
        cmd = "M1 %d" %(pos)
        cmd += '\n'
        self.robotGoBusy()
        self.sendCmd(cmd)
        
    def M2(self):
        if self.robotState != IDLE: return
        posUp = int(self.ui.penUpSpin.value())
        posDown = int(self.ui.penDownSpin.value())
        cmd = "M2 U%d D%d\n" %(posUp,posDown)
        self.robotGoBusy()
        self.sendCmd(cmd)

    def M5(self):
        if self.robotState != IDLE: return
        cmd = "M5 A%d B%d H%d W%d S%d\n" %(self.motoADir,self.motoBDir,self.height,self.width,self.speed)
        self.robotGoBusy()
        self.sendCmd(cmd)
        self.robotSig.emit("toggleComPort")

    def G1(self,x,y,feedrate=0,auxdelay=None):
        if self.robotState != IDLE: return
        cmd = "G1 X%.2f Y%.2f" %(x,y)
        if auxdelay!=None:
            cmd += " A%d" %(auxdelay)
        cmd += '\n'
        #print(cmd)
        self.robotGoBusy()
        self.sendCmd(cmd)
    
    def G28(self):
        if self.robotState != IDLE: return
        cmd = "G28\n"
        self.sendCmd(cmd)
        self.x = 0
        self.y = 0
        
    def M10(self): # read robot arm setup and init pos
        cmd = "M10\n"
        self.sendCmd(cmd)
    
    def moveOverList(self):
        if self.moveList == None: return
        moveLen = len(self.moveList)
        moveCnt = 0
        for move in self.moveList:
            #loop for all points
            lineNode = len(move)
            for i in range(lineNode):
                p = move[i]
                x=(p[0]-self.robotCent[0])/self.scaler
                y=-(p[1]-self.robotCent[1])/self.scaler
                if i==0:
                    segList = [(x,y)]
                else:
                    segList = sliceSegment(self.x, self.y, x, y)
                for s in segList:
                    try:
                        if self.printing == False:
                            return
                        elif self.pausing == True:
                            while self.pausing==True:
                                time.sleep(0.5)
                        auxDelay = 0
                        #if self.laserMode and i>0:
                        #    auxDelay = 10000
                        if self.laserMode:
                            if i>0:
                                auxDelay = self.laserBurnDelay*1000
                            elif i==0:
                                self.M4(self.laserPower,0.0) # turn laser power down when perform transition
                                self.q.get()
                        self.G1(s[0],s[1],auxdelay = auxDelay)
                        self.x = s[0]
                        self.y = s[1]
                        self.q.get()
                        if not self.laserMode and i == 0 and lineNode>1:
                            self.M1(self.penDownPos)
                            self.q.get()
                            time.sleep(0.2)
                    except:
                        pass
            moveCnt+=1
            self.robotSig.emit("pg %d" %(int(moveCnt*100/moveLen)))
            self.M1(self.penUpPos)
            self.q.get()
            time.sleep(0.2)
        self.M1(self.penUpPos)
        self.G28()
        self.q.get()
        self.printing = False
        self.robotSig.emit("done")
    
    def printPic(self):
        #update pen servo position
        mStr = str(self.ui.penUpSpin.value())
        self.penUpPos = int(mStr)
        mStr = str(self.ui.penDownSpin.value())
        self.penDownPos = int(mStr)
        
        while not self.q.empty():
            self.q.get()
        self.printing = True
        self.pausing = False
        self.moveListThread = WorkInThread(self.moveOverList)
        self.moveListThread.setDaemon(True)
        self.moveListThread.start()
        
    def stopPrinting(self):
        self.printing = False
        self.pausing = False
        
    def pausePrinting(self,v):
        self.pausing = v
        
    def showSetup(self):
        self.robotSetup =  RobotSetupUI(SpiderSetup.Ui_Form,self)
        