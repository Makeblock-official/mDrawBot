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
import EggSetup

class RobotSetupUI(QWidget):
    def __init__(self,uidialog,robot):
        super(RobotSetupUI, self).__init__()
        self.ui = uidialog()
        self.ui.setupUi(self)
        self.robot = robot
        self.setWindowTitle('Eggbot Setup')
        self.updateUI()
        self.ui.motoA_CK.mousePressEvent = self.setMotorAck
        self.ui.motoA_CCK.mousePressEvent = self.setMotorAcck
        self.ui.motoB_CK.mousePressEvent = self.setMotorBck
        self.ui.motoB_CCK.mousePressEvent = self.setMotorBcck
        self.ui.btnOk.clicked.connect(self.applySetup)
        self.show()
        
    def updateUI(self):
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

class EggBot(QGraphicsItem):
    
    def __init__(self, scene, ui, parent=None):
        super(EggBot, self).__init__(parent)
        self.robotState = IDLE
        self.scene = scene
        self.ui = ui
        self.moving = False
        self.robotCent = None
        # in degree
        self.width = 360
        self.height = 120
        self.scaler = 1.0
        #initial params
        self.x = 0
        self.y = -self.height/2
        self.motoADir = 0
        self.motoBDir = 0
        self.laserBurnDelay = 0
        self.stretch = None
        self.origin = None
        self.xyorigin = None
        self.q = queue.Queue()
        self.pRect = None
        self.moveList = None
        self.printing = False
        self.pausing = False
        self.laserMode = False
        self.lastx = 9999
        self.lasty = 9999
        self.ui.label.setText("X(deg)")
        self.ui.label_2.setText("Y(deg)")
    

    def boundingRect(self):
        return  QRectF(0,0,100,100)
    
    def initRobotCanvas(self):
        self.origin = ((self.scene.width()-self.width)/2,(self.scene.height()-self.height)/2)
        if self.pRect!=None:
            self.scene.removeItem(self.pRect)
        pen = QtGui.QPen(QtGui.QColor(124, 124, 124))
        self.pRect = self.scene.addRect(self.origin[0],self.origin[1],self.width,self.height,pen)
        
        pTxt = self.scene.addText("O")
        cent = QPointF(self.origin[0]-10,self.origin[1]+self.height)
        pTxt.setPos(cent)
        pTxt.setDefaultTextColor(QtGui.QColor(124, 124, 124))
        
        pTxt = self.scene.addText("Latitude")
        cent = QPointF(self.origin[0]-10,self.origin[1]-10)
        pTxt.setPos(cent)
        pTxt.setDefaultTextColor(QtGui.QColor(124, 124, 124))
        
        pTxt = self.scene.addText("Longitude")
        cent = QPointF(self.origin[0]+self.width,self.origin[1]+self.height)
        pTxt.setPos(cent)
        pTxt.setDefaultTextColor(QtGui.QColor(124, 124, 124))
        self.ui.labelScale.setText(str(self.scaler))
    
    def parseEcho(self,msg):
        if "M10" in msg:
            tmp = msg.split()
            if tmp[1]!="EGG": return
            self.degreePerCircle = float(tmp[2])
            self.x = float(tmp[3])
            self.y = -float(tmp[4])
            if tmp[5]=="A0":
                self.motoADir = 0
            else:
                self.motoADir = 1
            if tmp[6]=="B0":
                self.motoBDir = 0
            else:
                self.motoBDir = 1
            self.initRobotCanvas()
            self.robotState = IDLE


    def paint(self, painter, option, widget=None):
        painter.setBrush(QtCore.Qt.darkGray)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        x = self.x+self.origin[0]-self.robotCent[0]
        y = self.y+self.origin[1]-self.robotCent[1]+self.height
        
        img = QtGui.QImage(":/images/mEggBot_machine.png")
        painter.translate(0,0);
        painter.drawImage(-450,-220,img) # minus the center of image
        #painter.drawText(x-30,y+10,"(%.2f,%.2f)" %(self.x,-self.y))
        pen = QtGui.QPen(QtGui.QColor(124, 124, 124))
        painter.setBrush(QtCore.Qt.darkGray)
        painter.setPen(pen)
        painter.drawLine(x,self.origin[1]-self.robotCent[1],x,self.origin[1]-self.robotCent[1]+self.height)
        painter.drawLine(self.origin[0]-self.robotCent[0],y,self.origin[0]-self.robotCent[0]+self.width,y)
        
        pen = QtGui.QPen(QtGui.QColor(0, 169, 231))
        painter.setBrush(QtGui.QColor(0, 169, 231))
        painter.setPen(pen)
        painter.drawEllipse(-5+x,-5+y,10,10)
        
        if self.x!=self.lastx or self.y!=self.lasty:
            self.ui.labelXpos.setText("%.2f" %(self.x))
            self.ui.labelYpos.setText("%.2f" %(-self.y))
            self.lastx = self.x
            self.lasty = self.y

    def prepareMove(self,target,absolute=False):
        if absolute==False:
            target = (target.x(),-target.y())
            target = (target[0]+self.robotCent[0]-self.origin[0],-target[1]-self.origin[1]+self.robotCent[1]-self.height)
        else: # position set by user
            target = (target.x(),target.y())
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = sqrt(dx*dx+dy*dy)
        maxD = max(abs(dx),abs(dy))*0.5
        maxStep = ceil(maxD)
        self.deltaStep = (dx/maxStep,dy/maxStep)
        self.maxStep = maxStep
        x = target[0]
        y = -target[1]
        print("move to",(x,y),maxStep)
        if x<0 or x>self.width or y<0 or y>self.height:
            return None
        return (x,y)

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
        pos = self.prepareMove(pos,absolute)
        if pos == None: 
            return
        self.G1(pos[0],pos[1])
        self.moving = True
        self.moveThread = WorkInThread(self.moveStep)
        self.moveThread.setDaemon(True)
        self.moveThread.start()

    def G1(self,x,y,feedrate=0,auxdelay=None):
        if self.robotState != IDLE: return
        cmd = "G1 X%.2f Y%.2f" %(x,y)
        if auxdelay!=None:
            cmd += " A%d" %(auxdelay)
        cmd += '\n'
        self.robotState = BUSYING
        self.sendCmd(cmd)

    def G28(self):
        if self.robotState != IDLE: return
        cmd = "G28\n"
        self.sendCmd(cmd)
        self.x = 0
        self.y = -self.height/2
    
    def M1(self,pos):
        if self.robotState != IDLE: return
        cmd = "M1 %d" %(pos)
        cmd += '\n'
        self.robotState = BUSYING
        self.sendCmd(cmd)
    
    def M3(self,auxdelay): # aux delay
        if self.robotState != IDLE: return
        cmd = "M3 %d\n" %(auxdelay)
        self.robotState = BUSYING
        self.sendCmd(cmd)
    
    def M4(self,laserPower,rate=1): # setup laser power
        if self.robotState != IDLE: return
        cmd = "M4 %d\n" %(int(laserPower*rate))
        self.robotState = BUSYING
        self.sendCmd(cmd)
    
    def M5(self):
        if self.robotState != IDLE: return
        cmd = "M5 A%d B%d\n" %(self.motoADir,self.motoBDir)
        self.robotState = BUSYING
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
                x=(p[0]-self.origin[0])
                y=(p[1]-self.origin[1]-self.height)
                try:
                    if self.printing == False:
                        if self.laserMode:
                            self.M4(0) # turn off the laser when the user aborts the printing process
                        return
                    elif self.pausing == True:
                        while self.pausing==True:
                            time.sleep(0.5)
                    self.waitWhilePaused(self.laserMode and i>0)
                    auxDelay = 0
                    if self.laserMode:
                        if i>0:
                            auxDelay = self.laserBurnDelay*1000
                        elif i==0:
                            self.M4(0) # turn laser power down when perform transition
                            self.q.get()
                    self.G1(x,-y,auxdelay = auxDelay)
                    self.x = x
                    self.y = y
                    while self.robotState==BUSYING:
                        self.q.get()
                    if self.laserMode and i==0:
                        self.M4(self.laserPower) # turn laser power back to set value
                        self.q.get()
                    if not self.laserMode and i==0:
                        self.M1(self.penDownPos)
                        self.q.get()
                        time.sleep(0.2)
                except:
                    pass
            if not self.laserMode:
                self.M1(self.penUpPos)
                self.q.get()
                time.sleep(0.2)
            moveCnt+=1
            self.robotSig.emit("pg %d" %(int(moveCnt*100/moveLen)))
        self.printing = False
        self.robotSig.emit("done")
    
    def printPic(self):
        #update pen servo position
        #update pen servo position
        mStr = str(self.ui.penUpSpin.value())
        self.penUpPos = int(mStr)
        mStr = str(self.ui.penDownSpin.value())
        self.penDownPos = int(mStr)
        value = int(self.ui.slideLaserPower.value())
        laserpwm = value*255/100
        self.laserPower = laserpwm
        
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
    def waitWhilePaused(self, isLaserOn):
        if self.pausing:
            if isLaserOn:
                self.M4(0) # turn off the laser while the printing is paused
            while self.pausing:
                time.sleep(0.5)
            if isLaserOn:
                self.M4(self.laserPower) # turn on laser when the printing is continued, and it was on before pausing
        
    def showSetup(self):
        self.robotSetup =  RobotSetupUI(EggSetup.Ui_Form, self)
