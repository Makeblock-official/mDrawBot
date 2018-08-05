#-*-encoding:utf-8-*-
import sys
import os
import threading
import queue
import time
import mDraw
from ScaraGui import *

from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from RobotUtils import *
from math import *
import ParserGUI
import subprocess
import platform

       
class SvgConverter(QWidget):
    convertSig = pyqtSignal(str)
    def __init__(self,uidialog,bitmapFile,sig):
        super(SvgConverter, self).__init__()
        self.bitmapFile = str(bitmapFile)
        self.ui = uidialog()
        self.ui.setupUi(self)
        self.svgout = None
        self.ui.btnConvert.clicked.connect(self.convertToSvg)
        self.ui.btnReload.clicked.connect(self.loadBitmap)
        self.ui.btnPlotToMain.clicked.connect(self.plotToMainScene)
        self.ui.slideThr.valueChanged.connect(self.thresholdChanged)
        self.thresholdChanged()
        self.setupUI()
        self.show()
        self.loadBitmap()
        self.robotSig = sig
        self.convertSig.connect(self.parseConvertSig)
        
    def setupUI(self):
        rect = QRectF( self.ui.graphicsView.rect())
        self.scene = QGraphicsScene(rect)
        self.ui.graphicsView.setScene(self.scene)
        
    
    def parseConvertSig(self,cmd):
        print("svg sig",cmd)
        if "mkbitmap"  in cmd:
            self.potraceBitmap()
        elif "potrace" in cmd:
            """
            pm = QPixmap(self.svgout)
            print("svg pm",pm)
            pBitmap = self.scene.addPixmap(pm)
            pBitmap.setOffset(0,0)
            self.scene.update()
            """
            pm = QGraphicsSvgItem(self.svgout)
            self.scene.clear()
            self.scene.addItem(pm)
    
    def loadBitmap(self):
        self.scene.clear()
        pBitmap = self.scene.addPixmap(QPixmap(self.bitmapFile))
        pBitmap.setOffset(0,0)
        self.scene.setSceneRect(pBitmap.boundingRect())
    
    def thresholdChanged(self):
        th = "%02f" %(float(self.ui.slideThr.value())/100)
        self.ui.labelThr.setText(th)
    
    def convertToSvg(self):
        self.svgout = None
        self.loadBitmap()
        #self.bmtemp = os.getcwd()+"\\temp\\temp.pdm"
        #th = float(self.ui.slideThr.value())/100
        #cmd = "mkbitmap.exe -f 2 -s 2 -t %f %s -o %s" %(th,self.bitmapFile,self.bmtemp)
        #print cmd
        self.moveListThread = WorkInThread(self.potraceBitmap)
        self.moveListThread.setDaemon(True)
        self.moveListThread.start()  
    
    def potraceBitmap(self):
        p = os.getcwd()
        systemType = platform.system()
        th = float(self.ui.slideThr.value())/100
        self.svgout = self.bitmapFile+".svg"
        if "Windows" in systemType:
            #cmd = "potrace.exe -k %f -t 5 -s -o %s %s" %(th,self.svgout,self.bitmapFile)
            p  ="potrace.exe"
            cmd = "%s -k %f -t 5 -s -o %s %s" %(p,th,self.svgout,self.bitmapFile)
        elif "Darwin" in systemType:
            p  ="./potrace"
            cmd = "%s -k %f -t 5 -s -o %s %s" %(p,th,self.svgout,self.bitmapFile)
        p = subprocess.Popen(cmd,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.wait()
        self.convertSig.emit("potrace")
        """
        p = subprocess.Popen(cmd, stderr=subprocess.PIPE)
        while True:
            out = p.stderr.readline()
            if out == '' and p.poll() != None:
                print "potrace end",out
                self.convertSig.emit("potrace")
                break
            if out != '':
                print out
                #sys.stdout.write(out)
                #sys.stdout.flush()
        """
    def convertToBitmap(self,cmd):
        p = subprocess.Popen(cmd)
        p.wait()
        print("bitmap finished")
        self.convertSig.emit("mkbitmap")
        """
        while True:
            out = p.stderr.readline()
            if out == '' and p.poll() != None:
                print "convert end",out
                self.convertSig.emit("mkbitmap")
                break
            if out != '':
                print out
                #sys.stdout.write(out)
                #sys.stdout.flush()
                # something wrong
                return
        """
    def plotToMainScene(self):
        if self.svgout!=None:
            self.robotSig.emit("potrace "+self.svgout)
        self.hide()
            
        
        
        
        
        
        
        
        