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
import CarSetup

class RobotSetupUI(QWidget):
    def __init__(self,uidialog,robot):
        super(RobotSetupUI, self).__init__()
        self.ui = uidialog()
        self.ui.setupUi(self)
        self.robot = robot
        self.setWindowTitle('Car Setup')
        self.updateUI()
        self.laserMode = False
        self.ui.motoA_CK.mousePressEvent = self.setMotorAck
        self.ui.motoA_CCK.mousePressEvent = self.setMotorAcck
        self.ui.motoB_CK.mousePressEvent = self.setMotorBck
        self.ui.motoB_CCK.mousePressEvent = self.setMotorBcck
        self.ui.btnOk.clicked.connect(self.applySetup)
        self.show()

    def updateUI(self):
        self.ui.lineWidth.setText(str(self.robot.carWidth))
        self.ui.lineScale.setText(str(self.robot.scaler))
        self.ui.radioHermit.setChecked(self.robot.useHermit)
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

    def applySetup(self):
        self.robot.scaler = float(str(self.ui.lineScale.text()))
        self.robot.carWidth = float(str(self.ui.lineWidth.text()))
        self.robot.useHermit = int(self.ui.radioHermit.isChecked())
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

class CarBot(QGraphicsItem):
    
    def __init__(self, scene, ui, parent=None):
        super(CarBot, self).__init__(parent)
        self.robotState = IDLE
        self.scene = scene
        self.ui = ui
        self.x = 0
        self.y = 0
        self.dir = 0
        self.carWidth = 123
        self.scaler = 0.5
        self.motoADir = 0
        self.motoBDir = 0
        self.useHermit = 1
        self.path = None
        self.pathPtr = None
        self.q = queue.Queue()
        self.moving = False
        self.robotCent = None
        self.printing = False
        self.pausing = False
        self.lastx = 9999
        self.lasty = 9999
        self.ui.label.setText("X(mm)")
        self.ui.label_2.setText("Y(mm)")
        
    def boundingRect(self):
        return  QRectF(0,0,100,100)
        
    def initRobotCanvas(self):
        if self.pathPtr != None:
            self.scene.removeItem(self.pathPtr)
        self.path = QtGui.QPainterPath()
        self.path.moveTo(self.x+self.robotCent[0], self.y+self.robotCent[1])
        self.pathPtr = self.scene.addPath(self.path)
        self.pathPtr.setPen(QtGui.QPen(QtGui.QColor(124, 124, 124)))
        self.ui.labelScale.setText(str(self.scaler))
        
    def paint(self, painter, option, widget=None):
        painter.setBrush(QtCore.Qt.darkGray)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        #x = self.x*self.scaler
        #y = -self.y*self.scaler
        # don't show scale on canvas
        x = self.x
        y = -self.y
        
        painter.setBrush(QtCore.Qt.darkGray)
        painter.drawEllipse(-5,-5,10,10)
        #painter.setBrush(QtCore.Qt.green)
        #painter.drawEllipse(-5+x,-5+y,10,10)
        #pen = QtGui.QPen(QtCore.Qt.green)
        #painter.setPen(pen)
        #painter.drawLine(x,y,x+20*cos(self.dir/180*pi),y-20*sin(self.dir/180*pi))
        img = QtGui.QImage(":/images/caricon.png")
        painter.translate(x,y);        
        painter.rotate(-self.dir)
        painter.drawImage(-30,-17,img) # minus the center of image
        
        if x!=self.lastx or y!=self.lasty:
            self.ui.labelXpos.setText("%.2f" %(x))
            self.ui.labelYpos.setText("%.2f" %(-y))
            self.lastx = x
            self.lasty = y


    def moveStep(self):
        while True:
            self.x+=self.deltaStep[0]
            self.y+=self.deltaStep[1]
            time.sleep(0.02)
            self.maxStep-=1
            
            if self.maxStep==0 or self.moving==False:
                self.moving = False
                return

    def prepareMove(self,target,absolute=False):
        if absolute==False:
            target = (target.x()/self.scaler,-target.y()/self.scaler)
        else:
            target = (target.x(),-target.y())
        
        self.path.lineTo(target[0]+self.robotCent[0], -target[1]+self.robotCent[1])
        self.pathPtr.setPath(self.path)
        
        dx = target[0] - self.x
        dy = target[1] - self.y
        self.dir = atan(dy/dx)/pi*180
        if dx<0:
            self.dir+=180
        #print("dir",self.dir,dx,dy)
        distance = sqrt(dx*dx+dy*dy)
        maxD = max(abs(dx),abs(dy))*0.5
        maxStep = ceil(maxD)
        self.deltaStep = (dx/maxStep,dy/maxStep)
        self.maxStep = maxStep
        #print("move to",target,maxStep)

    def moveTo(self,pos):
        if self.moving:
            self.moving = False
            self.moveThread.join()
        self.prepareMove(pos,True)
        pos=pos/self.scaler
        self.G1(pos.x(),-pos.y())
        self.moving = True
        self.moveThread = WorkInThread(self.moveStep)
        self.moveThread.setDaemon(True)
        self.moveThread.start()
    
    def parseEcho(self,msg):
        if "M10" in msg:
            tmp = msg.split()
            # todo: add firmware version echo
            if tmp[1]!="MCAR": return
            self.carWidth = int(tmp[2])
            if len(tmp)>6:
                self.useHermit = int(tmp[6][1])
                self.penUpPos = int(tmp[7][1:])
                self.ui.penUpSpin.setValue(self.penUpPos)
                self.penDownPos = int(tmp[8][1:])
                self.ui.penDownSpin.setValue(self.penDownPos)
            self.initRobotCanvas()
            self.robotState = IDLE
    
    def robotGoBusy(self):
        self.robotState = BUSYING
        self.ui.labelMachineState.setText("BUSY")
    
    def G1(self,x,y,feedrate=0,direction=None):
        if self.robotState != IDLE: return
        cmd = "G1 X%.2f Y%.2f" %(x,y)
        if direction!=None:
            cmd += " D%d" %(direction)
        cmd += '\n'
        self.robotGoBusy()
        self.sendCmd(cmd)
             
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
        cmd = "M5 W%d H%d\n" %(self.carWidth,self.useHermit)
        self.robotGoBusy()
        self.sendCmd(cmd)
        self.robotSig.emit("toggleComPort")
    
    def G28(self):
        if self.moving:
            self.moving = False
            self.moveThread.join()
        self.x = 0
        self.y = 0
        self.dir = 0
        self.initRobotCanvas()
        if self.robotState != IDLE: return
        cmd = "G28\n"
        self.sendCmd(cmd)
        
    def M10(self): # read robot arm setup and init pos
        cmd = "M10\n"
        self.sendCmd(cmd)
        
    def moveOverList(self):
        if self.moveList == None: return
        moveLen = len(self.moveList)
        moveCnt = 0
        for move in self.moveList:
            #loop for all points
            for i in range(len(move)):
                p = move[i]
                x=(p[0]-self.robotCent[0])/self.scaler
                y=-(p[1]-self.robotCent[1])/self.scaler
                #try:
                if self.printing == False:
                    return
                self.G1(x,y)
                # update canvas content
                dx = x - self.x/self.scaler
                dy = y - self.y/self.scaler
                if dx==0:
                    if dy>0:
                        self.dir = 90
                    else:
                        self.dir = -90
                else:
                    self.dir = atan(dy/dx)/pi*180
                if dx<0:
                    self.dir+=180
                self.x = x*self.scaler
                self.y = y*self.scaler
                self.q.get()
                if i == 0:
                    self.M1(self.penDownPos)
                    self.q.get()
                    time.sleep(0.2)
                #except:
                #    pass
            self.M1(self.penUpPos)
            self.q.get()
            time.sleep(0.2)
            moveCnt+=1
            self.robotSig.emit("pg %d" %(int(moveCnt*100/moveLen)))
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
        self.moveListThread = WorkInThread(self.moveOverList)
        self.moveListThread.setDaemon(True)
        self.moveListThread.start()
        
    def stopPrinting(self):
        self.printing = False

    def showSetup(self):
        self.robotSetup =  RobotSetupUI(CarSetup.Ui_Form,self)







