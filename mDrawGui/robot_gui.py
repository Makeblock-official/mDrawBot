#-*-encoding:utf-8-*-
import sys
import os
import SerialCom
import SocketCom
import threading
from ScaraGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
import SvgParser
import ParserGUI
import time
import math
import ScaraRobot
import WallRobot
import XYRobot
import CarRobot
import EggBot
import SvgConverter
import HexDownloader
import sys
import urllib2

robotVersion="1.02 2015-2-28"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

DEBUG_NORMAL = 0
DEBUG_DEBUG = -2
DEBUG_ERR = -3
IDLE = 0
BUSYING = 1
def millis():
    return int(round(time.time() * 1000))

class WorkInThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)
        
class MainUI(QtGui.QWidget):
    sceneUpdateSig = pyqtSignal()
    robotSig = pyqtSignal(str)
    def __init__(self):
        super(MainUI, self).__init__()
        self.pic = None
        self.robot = None
        self.ptrPicRect = None
        self.ptrPicRez = None
        self.tempPicRect = None
        self.mouseOverPic = False
        self.mouseResizePic = False
        self.bufferedM10msg = ""
        self.picX0 = 300
        self.picY0 = 200
        self.picWidth = 0
        self.picHeight = 0
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # get sys serial port and update combo box
        self.comm = None
        self.serial = SerialCom.serialCom(self.commRx)
        self.socket = SocketCom.SocketCom(self.refreshDone,self.commRx,self.disconnectPort)
        self.refreshCom()
        # link button
        self.ui.btnConnect.clicked.connect(self.connectPort)
        self.ui.btnLoadPic.clicked.connect(self.loadPic)
        self.ui.btnClearPic.clicked.connect(self.clearPic)
        self.ui.btnSend.clicked.connect(self.sendCmd)
        self.ui.btnPrintPic.clicked.connect(self.robotPrint)
        self.ui.btnStop.clicked.connect(self.robotStop)
        self.ui.btnSetRobot.clicked.connect(self.showRobotSetup)
        self.ui.portCombo.mousePressEvent = self.portComboPressed
        self.ui.labelXpos.returnPressed.connect(self.userSetPos)
        self.ui.labelYpos.returnPressed.connect(self.userSetPos)
        self.ui.lineSvgHeight.returnPressed.connect(self.userSetSvgRect)
        self.ui.lineSvgWidth.returnPressed.connect(self.userSetSvgRect)
        self.ui.lineSend.returnPressed.connect(self.sendCmd)
        self.ui.btnUpdateFirmware.clicked.connect(self.uploadFirmware)
        # init scene
        rect = QRectF( self.ui.graphicsView.rect())
        self.scene = QtGui.QGraphicsScene(rect)
        item = QtGui.QGraphicsEllipseItem(75, 10, 60, 40)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.progressBar.setVisible(False)
        self.ui.labelPic.setVisible(False)
        #fix the 1 pix margin of graphic view
        rcontent = self.ui.graphicsView.contentsRect();
        self.ui.graphicsView.setSceneRect(0, 0, rcontent.width(), rcontent.height());
        
        # mouse movement
        self.ui.graphicsView.mousePressEvent = self.graphMouseClick
        self.ui.graphicsView.mouseMoveEvent = self.graphMouseMove
        self.ui.graphicsView.mouseReleaseEvent = self.graphMouseRelease
        # path from user paint
        self.userPaint = None
        # init robot parts (default to scara robot)
        self.robot = ScaraRobot.Scara(self.scene, self.ui)
        self.robot.sendCmd = self.sendCmd
        self.robot.robotSig = self.robotSig
        # connect robot delegate
        self.ui.btnHome.clicked.connect(self.robotGoHome)
        # connect pen widget
        self.ui.btnPenUp.clicked.connect(self.plotPenUp)
        self.ui.btnPenDown.clicked.connect(self.plotPenDown)
        # connect laser widget
        self.ui.slideLaserPower.setEnabled(False)
        self.ui.slideLaserDelay.setEnabled(False)
        self.ui.slideLaserPower.valueChanged.connect(self.laserValue)
        self.ui.slideLaserDelay.valueChanged.connect(self.laserDelay)
        self.ui.btnLaserStart.clicked.connect(self.laserMode)
        
        self.ui.tabWidget.currentChanged.connect(self.tabWidgetChanged)
        
        self.ui.robotCombo.currentIndexChanged.connect(self.tabChanged)

        self.sceneUpdateSig.connect(self.scene.update)
        self.robotSig.connect(self.parseRobotSig)
        self.robotSig.emit("pg 0")
        
        self.initGraphView()
        self.robot.initRobotCanvas()
        self.setWindowTitle('mDraw')
        self.show()
        # start refresh thread
        self.refreshThread = WorkInThread(self.sceneRefresh)
        self.refreshThread.setDaemon(True)
        self.refreshThread.start()
        # get update info
        self.htmlThread = WorkInThread(self.getUpdateInfo)
        self.htmlThread.setDaemon(True)
        self.htmlThread.start()
        
    def sceneRefresh(self):
        while True:
            self.sceneUpdateSig.emit()
            time.sleep(0.05)
            
    def parseRobotSig(self,msg):
        msg=str(msg)
        if "pg" in msg:
            tmp = msg.split()
            progress = int(tmp[1])
            self.ui.progressBar.setValue(progress)
        elif "done" in msg:
            self.robot.stopPrinting()
            self.ui.progressBar.setVisible(False)
            self.switchPrintButton("Go")
            if self.robot.laserMode:
                self.laserMode("Off")
        elif "potrace" in msg:
            svgfile = msg.split()[1]
            self.loadPic(svgfile)
        elif "download" in msg:
            if "start" in msg:
                self.ui.progressBar.setValue(0)
                self.ui.progressBar.show()
            else: # finished or failed
                self.ui.progressBar.hide()
                self.dbg(msg)
        else:
            self.dbg(msg)

    def commRx(self,msg):
        try:
            if "OK" in msg:
                self.robot.robotState = IDLE
                self.robot.q.put(1)
            elif "M" in msg:
                self.dbg(msg,DEBUG_DEBUG)
                if "M10" in msg:
                    if "MSCARA" in msg and str(self.ui.robotCombo.currentText())!="mScara":
                        self.ui.robotCombo.setCurrentIndex(0)
                    elif "MSPIDER" in msg and str(self.ui.robotCombo.currentText())!="mSpider":
                        self.ui.robotCombo.setCurrentIndex(1)
                    elif "XY" in msg and str(self.ui.robotCombo.currentText())!="XY":
                        self.ui.robotCombo.setCurrentIndex(4)
                    elif "EGG" in msg and str(self.ui.robotCombo.currentText())!="mEggBot":
                        self.ui.robotCombo.setCurrentIndex(2)
                    elif "MCAR" in msg and str(self.ui.robotCombo.currentText())!="mCar":
                        self.ui.robotCombo.setCurrentIndex(3)
                    self.bufferedM10msg = msg
                    self.robot.parseEcho(msg)
        except:
            """todo: may screw if we connect to a wrong serial port"""
            pass
    
    def sendCmd(self,cmd=""):
        if self.comm == None: return
        if cmd==False:
            cmd = str(self.ui.lineSend.text())+'\n'
        self.comm.send(cmd)
    
    def robotGoHome(self):
        self.robot.G28()
    
    def getRobotConfig(self):
        self.robot.M10()
            
    def refreshCom(self):
        self.commList = {}
        self.ui.portCombo.clear()
        serPorts = SerialCom.serialList()
        for s in serPorts:
            self.commList[s]="COM"
            self.ui.portCombo.addItem(s)
        #self.socket.refresh()
    
    def portComboPressed(self, event):
        self.refreshCom()
        self.ui.portCombo.showPopup()
   
    def refreshDone(self,msg):
        ""
        self.dbg(msg)
        if "fail" not in msg:
            self.commList[msg]="WIFI"
            self.ui.portCombo.addItem(msg)
            
    def disconnectPort(self):
        if self.comm==None:
            return
        self.comm.close()
        self.ui.btnConnect.clicked.connect(self.connectPort)
        self.ui.btnConnect.clicked.disconnect(self.disconnectPort)
        self.ui.btnConnect.setText("Connect")
        self.dbg("port closed")
        self.comm = None
        return
    
    def connectPort(self):
        port = str(self.ui.portCombo.currentText())
        try:
            if self.commList[port] == "COM":
                self.serial.connect(port)
                self.comm = self.serial
            elif self.commList[port] == "WIFI":
                self.socket.connect(port)
                self.comm = self.socket
            self.ui.btnConnect.clicked.connect(self.disconnectPort)
            self.ui.btnConnect.clicked.disconnect(self.connectPort)
            self.ui.btnConnect.setText("Disconnect")
            self.dbg("%s open success" %(port))
            threading.Timer(2, self.getRobotConfig).start() # wait for bootloader finished on arduino
            self.robotState = IDLE
        except Exception as e:
            self.dbg(e,-3)
            raise Exception(e)
        
    def initGraphView(self):
        scene = self.ui.graphicsView.scene()
        # remove graph reference first
        self.ptrPicRect = None
        self.pic = None
        scene.clear()
        rc = scene.sceneRect()
        cent = QPointF(rc.width()/2,rc.height()/2+100)
        self.robotCent = cent
        self.robot.robotCent =(cent.x(),cent.y())
        print "rc",cent
        scene.addItem(self.robot)
        self.robot.setPos(cent)
    
    def tabChanged(self,tabindex):
        #print "tab changed",tabindex
        ssTemplate = "background-color: rgb(247, 247, 247);border-image: url(:/images/model.png);"
        if tabindex==0:
            self.robot = ScaraRobot.Scara(self.scene, self.ui)
            self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "scara"))
        elif tabindex==1:
            self.robot = WallRobot.WallRobot(self.scene, self.ui)
            self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "spider"))
        elif tabindex==4:
            self.robot = XYRobot.XYBot(self.scene,self.ui)
            self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "xy"))
        elif tabindex==2:
            self.robot = EggBot.EggBot(self.scene,self.ui)
            self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "egg"))
        elif tabindex==3:
            self.robot = CarRobot.CarBot(self.scene,self.ui)
            self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "car"))
        # connect robot delegate
        self.robot.sendCmd = self.sendCmd
        self.robot.robotSig = self.robotSig
        self.ui.labelPic.setVisible(False)
        self.initGraphView()
        self.robot.initRobotCanvas()
        self.robot.parseEcho(self.bufferedM10msg)
        self.bufferedM10msg = ""
        
    def dbg(self,log,level=DEBUG_NORMAL):
        if level == DEBUG_ERR:
            dbgstr="<font color=red>%s</font>" %str(log)
            self.ui.textConsole.append(dbgstr)
        elif level == DEBUG_DEBUG:
            dbgstr="<font color=green>%s</font>" %str(log)
            self.ui.textConsole.append(dbgstr)
        else:
            dbgstr="<font color=white>%s</font>" %str(log)
            self.ui.textConsole.append(dbgstr)
            
    def loadPic(self,filename=False):
        self.clearPic()
        if filename==False:
            filename = str(QtGui.QFileDialog.getOpenFileName(self, 'Open Svg/Bmp', '', ".svg;.bmp(*.svg;*.bmp)").toUtf8())
        self.dbg(filename)
        if len(filename)==0:
            return
        filetype =filename.split(".")[-1] 
        if filetype=="svg":
            self.pic = SvgParser.SvgParser(filename,self.scene)
            self.ui.labelPic.setVisible(True)
            self.picX0 = 300
            self.picY0 = 200
            self.picWidth = 150
            self.picHeight = 150
            self.updatePic()
        elif filetype=="bmp":
            self.showConverter(filename)

    def showConverter(self,bmpPath):
        self.converter = SvgConverter.SvgConverter(ParserGUI.Ui_Form,bmpPath,self.robotSig)
        

    def clearPic(self):
        if self.pic == None: return
        if self.ptrPicRect!=None:
            for path in self.pic.ptrList:
                self.scene.removeItem(path)
            self.scene.removeItem(self.ptrPicRect)
            self.scene.removeItem(self.ptrPicRez)
        self.ui.labelPic.setVisible(False)
        self.picWidth = 0
        self.picHeight = 0
        self.ptrPicRect = None
        self.ptrPicRez = None        
        
    def updatePic(self):
        x = self.picX0
        y = self.picY0
        w = self.picWidth
        h = self.picHeight
        if self.ptrPicRect!=None:
            self.scene.removeItem(self.ptrPicRect)
            self.scene.removeItem(self.ptrPicRez)
        pen = QtGui.QPen(QtGui.QColor(0, 169, 231))
        if self.pic == None: return
        for path in self.pic.ptrList:
            self.scene.removeItem(path)
        (w,h) = self.pic.resize((x,y,w,h)) # get rect of target svg
        #stretch for eggbot
        #ycent = self.robot.origin[1]+self.robot.height/2
        if self.robot.__class__.__name__=="EggBot" and self.robot.stretch!=None:
            ycent = y+h/2
            self.pic.stretch(ycent,self.robot.stretch)
        
        self.picWidth = w
        self.picHeight = h
        #self.ui.labelPic.setText(" w: %d mm\n h: %d mm" %(w,h))
        self.ui.lineSvgWidth.setText("%.2f" %w)
        self.ui.lineSvgHeight.setText("%.2f" %h)
        self.ui.labelPic.move(QPoint(x+w+20,y+h+20))
        self.ptrPicRect = self.scene.addRect(x,y,w,h,pen) # refresh boundary
        self.ptrPicRez = self.scene.addRect(x+w,y+h,5,5,pen)
        self.robot.moveList = self.pic.pathList
        self.pic.plotToScene()
        
    def robotPrint(self):
        if not self.robot.printing:
            self.ui.progressBar.setValue(0)
            self.robot.printPic()
            self.ui.progressBar.setVisible(True)
            #self.ui.btnPrintPic.setText("Stop")
            self.switchPrintButton("Pause")
        else:
            if self.robot.pausing == False:
                self.robot.pausePrinting(True)
                self.switchPrintButton("Go")
            else:
                self.robot.pausePrinting(False)
                self.switchPrintButton("Pause")
            
    def robotStop(self):
        if self.robot.printing:
            self.robot.stopPrinting()
            self.ui.progressBar.setVisible(False)
            self.switchPrintButton("Go")
    
    def switchPrintButton(self,s):
        if s=="Go":
            self.ui.btnPrintPic.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image:url(:/images/scara-UI-Start-normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-Start-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-Start-click.png) 0;\n"
" }\n"
"\n"
""))
        else:
            self.ui.btnPrintPic.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image:url(:/images/scara-UI-Suspendend-normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-Suspendend-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-Suspendend-click.png) 0;\n"
" }\n"
"\n"
""))
    
    def userSetSvgRect(self):
        ratio = self.picHeight/self.picWidth
        sender = self.sender().objectName()
        if sender == "lineSvgWidth":
            strW = str(self.ui.lineSvgWidth.text())
            w = float(strW)
            h = w*ratio
        else:
            strH = str(self.ui.lineSvgHeight.text())
            h = float(strH)
            w = h/ratio
        self.picWidth = w
        self.picHeight = h
        self.updatePic()
    
    def userSetPos(self):
        strX = str(self.ui.labelXpos.text())
        strY = str(self.ui.labelYpos.text())
        x = float(strX)
        y = -float(strY)
        pos = QtCore.QPointF(x,y)
        print pos
        self.robot.moveTo(pos,True)
            

    def graphMouseRelease(self,event):
        #self.userPaint.lineTo(event.pos())
        #self.pathptr.setPath(self.userPaint)
        if self.tempPicRect==None:
            pos = event.pos()-self.robotCent
            #print "POS",pos
            try:
                self.robot.moveTo(pos)
            except Exception as e:
                pass
                
        else:
            if self.mouseOverPic:
                w = self.picWidth
                h = self.picHeight
                pos = event.pos()
                px,py = pos.x(),pos.y()
                x = px-self.rectBias[0]
                y = py-self.rectBias[1]
                self.tempPicRect.setRect(x,y,w,h)
                self.scene.removeItem(self.tempPicRect)
                self.tempPicRect = None
                self.picX0 = x
                self.picY0 = y
                self.updatePic()
            elif self.mouseResizePic:
                x = self.picX0
                y = self.picY0
                pos = event.pos()
                rect = self.tempPicRect.rect()
                w = rect.width()
                h = rect.height()
                self.tempPicRect.setRect(x,y,w,h)
                self.scene.removeItem(self.tempPicRect)
                self.tempPicRect = None
                self.picWidth = w
                self.picHeight = h
                self.updatePic()
                
            
    def graphMouseMove(self,event):
        #self.userPaint.lineTo(event.pos())
        #self.pathptr.setPath(self.userPaint)
        if self.tempPicRect!=None:
            if self.mouseOverPic:
                w = self.picWidth
                h = self.picHeight
                pos = event.pos()
                px,py = pos.x(),pos.y()
                self.tempPicRect.setRect(px-self.rectBias[0],py-self.rectBias[1],w,h)
            elif self.mouseResizePic:
                x = self.picX0
                y = self.picY0
                ratio = self.picHeight/self.picWidth
                pos = event.pos()
                px,py = pos.x(),pos.y()
                w = px-x
                if w<10:
                    w=10
                #h = py-y
                h=w*ratio # fix svg w/h ratio
                #self.ui.labelPic.setText(" w: %d mm\n h: %d mm" %(w,h))
                self.ui.lineSvgWidth.setText("%.2f" %w)
                self.ui.lineSvgHeight.setText("%.2f" %h)
                # let label follow mouse positions
                self.ui.labelPic.move(QPoint(x+w+20,y+h+20))
                self.tempPicRect.setRect(x,y,w,h)
        else: # restore mouse icon
            pos = event.pos()
            x = self.picX0
            y = self.picY0
            w = self.picWidth
            h = self.picHeight
            px,py = pos.x(),pos.y()
            if px>x and px<(x+w) and py>y and py<(y+h):
                if self.mouseOverPic==False:
                    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(Qt.SizeAllCursor))
                    self.mouseOverPic = True
            elif px>(x+w) and px<(x+w+5) and py>(y+h) and py<(y+h+5):
                if self.mouseResizePic==False:
                    QtGui.QApplication.setOverrideCursor(QtGui.QCursor(Qt.SizeFDiagCursor))
                    self.mouseResizePic = True
            else:
                if self.mouseOverPic==True or self.mouseResizePic==True:
                    QtGui.QApplication.restoreOverrideCursor()
                    QtGui.QApplication.restoreOverrideCursor()
                    self.mouseOverPic = False
                    self.mouseResizePic = False
                 
        
    def graphMouseClick(self,event):
        #self.userPaint = QtGui.QPainterPath()
        #self.userPaint.moveTo(event.pos())
        #self.pathptr = self.scene.addPath(self.userPaint)
        if self.ptrPicRect==None: return
        pos = event.pos()
        x = self.picX0
        y = self.picY0
        w = self.picWidth
        h = self.picHeight
        px,py = pos.x(),pos.y()
        if self.mouseOverPic or self.mouseResizePic:
            pen = QtGui.QPen(QtGui.QColor(0, 169, 231),3,QtCore.Qt.DashDotLine)
            self.tempPicRect =  self.scene.addRect(x,y,w,h,pen)
            self.rectBias = (px-x,py-y)

    def plotPenUp(self):
        mStr = str(self.ui.linePenUp.text())
        pos = int(mStr.split()[1])
        self.robot.M1(pos)
    
    def plotPenDown(self):
        mStr = str(self.ui.linePenDown.text())
        pos = int(mStr.split()[1])
        self.robot.M1(pos)
      
    def laserValue(self):
        value = self.ui.slideLaserPower.value()
        self.ui.labelLaserPower.setText(str(value))
        self.robot.M4(value)
        
    def laserDelay(self):
        delay = self.ui.slideLaserDelay.value()
        self.ui.labelLaserDelay.setText(str(delay))
        self.robot.laserBurnDelay = delay
    
    def laserMode(self,txt=False):
        if txt==False:
            txt = str(self.ui.btnLaserStart.text())
        if txt=="Off":
            self.ui.slideLaserPower.setEnabled(False)
            self.ui.slideLaserDelay.setEnabled(False)
            self.ui.slideLaserPower.setValue(0)
            self.ui.slideLaserDelay.setValue(0)
            self.robot.laserMode = False
            self.ui.btnLaserStart.setText("On")
        else:
            self.ui.slideLaserPower.setEnabled(True)
            self.ui.slideLaserDelay.setEnabled(True)
            self.robot.laserMode = True
            self.ui.btnLaserStart.setText("Off")
    
    def tabWidgetChanged(self,i):
        ssTemplate = "background-color: rgb(247, 247, 247);border-image: url(:/images/model.png);"
        if str(self.ui.robotCombo.currentText())=="mScara":
            if i==0:
                self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "scara"))
            else:
                self.ui.labelModel.setStyleSheet(ssTemplate.replace("model", "scara_laser"))
    
    def showRobotSetup(self):
        self.robot.showSetup()
    
    def uploadFirmware(self):
        robotType = str(self.ui.robotCombo.currentText())
        firmpath = robotType+".hex"
        comport = str(self.ui.portCombo.currentText())
        # disconnect any comport before upload
        self.disconnectPort()
        self.hexDownloader = HexDownloader.HexDownloader(self.robotSig)
        self.hexDownloader.startDownloadUno(comport, firmpath)
        
    def closeEvent(self, event):
        if hasattr(self.robot, 'robotSetup'):
            self.robot.robotSetup.close()
        
    def getUpdateInfo(self):
        self.dbg("version=%s" %robotVersion)
        response = urllib2.urlopen('http://makeblock.sinaapp.com/config/mdraw.php')
        html = response.read()
        # self.dbg(html)
        # todo: parse the received update info

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def getPkgPath(name):
    # include every thing , make pyinstaller happy
    pkg_source={}
    pkg_source["avrdude"] = resource_path("avrdude")
    pkg_source["potrace"] = resource_path("potrace")
    pkg_source["avrdude.exe"] = resource_path("avrdude.exe")
    pkg_source["potrace.exe"] = resource_path("potrace.exe")
    pkg_source["avrdude.conf"] = resource_path("avrdude.conf")
    pkg_source["XY.hex"] = resource_path("XY.hex")
    pkg_source["mScara.hex"] = resource_path("mScara.hex")
    pkg_source["mSpider.hex"] = resource_path("mSpider.hex")
    pkg_source["mEggBot.hex"] = resource_path("mEggBot.hex")
    pkg_source["mCar.hex"] = resource_path("mCar.hex")
    print "get pkg",name
    return pkg_source[name]
 
if __name__ == '__main__':
    #sys.stdout = open("stdout.log", "w")
    #sys.stderr = open("stderr.log", "w")
    try:
        print sys._MEIPASS
    except:
        pass
    
    app = QtGui.QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())

