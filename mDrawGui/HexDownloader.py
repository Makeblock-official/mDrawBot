import sys
import os
import threading
import subprocess
import platform
import UnoProgrammer
from RobotUtils import *
from tkinter.tix import Shell

class HexDownloader():
    def __init__(self, sig):
        self.sig = sig
        
    def loadHexFile(self, filename):
        f = open(filename,"r")
        lines  = f.readlines()
        for line in lines:
            [addr,t,cnt,data,crc] = self.parseHexLine(line)
            print("%x %s" %(addr,data))
        f.close()
        # save hex size
    
    def downloadThread(self,cmd):
        state = 0
        progress = 0
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.sig.emit("download start")
        while True:
            out = p.stderr.readline().decode("utf-8")
            if out == '' and p.poll() != None: # not work in py-installer
                if state==2:
                    self.sig.emit("download finished")
                else:
                    self.sig.emit("download failed")
                break
            if out != '':
                #sys.stdout.write(out)
                #sys.stdout.flush()
                #self.sig.emit(out)
                print(out)
                if "writing flash" in out:
                    state=1
                    progress = 0
                elif "reading on-chip flash data" in out:
                    state=2
                    progress = 0
                c = out.count('#')
                progress+=(c*2)
                if state>0 and c>0:
                    self.sig.emit("downpg %d" %(progress))
                
                
    
    def startDownloadUno(self, com, hexfile):
        systemType = platform.system()
        if "Windows" in systemType:
            avrdudepath = "avrdude.exe"
            confpath = "avrdude.conf"
            cmd = u"printenv && pwd && ls && %s -C%s -v -v -v -v -patmega328p -carduino -P%s -b115200 -D -Uflash:w:%s:i" %(avrdudepath,confpath,com,hexfile)
            print(cmd)
    #         os.system(cmd)
            self.moveListThread = WorkInThread(self.downloadThread,cmd)
            self.moveListThread.setDaemon(True)
            self.moveListThread.start()
        elif "Darwin" in systemType:
            # avrdudepath = "./avrdude"
            # confpath = "avrdude.mac.conf"
            # use a new homemade upload to upload mac os firmware
            programmer = UnoProgrammer.UnoProgrammer(com, self.sig, hexfile)
            self.moveListThread = WorkInThread(programmer.downloadThread)
            self.moveListThread.setDaemon(True)
            self.moveListThread.start()
        
    
    def startDownloadLeonardo(self, com, hexfile):
        p = os.getcwd()
        avrdudepath = "%s\\avrdude.exe" %(p)
        confpath = "%s\\avrdude.conf" %(p)
        cmd = "%s -C%s -v -v -v -v -patmega32u4 -cavr109 -P%s -b57600 -D -Uflash:w:%s:i" %(avrdudepath,confpath,com,hexfile)
        self.moveListThread = WorkInThread(self.downloadThread,cmd)
        self.moveListThread.setDaemon(True)
        self.moveListThread.start()
        
    def serialPost(self, cmd):
        ""
  
    def parseHexLine(self,line):
        cnt = int(line[1:3],16)
        addr = int(line[3:7],16)
        hextype = int(line[7:9])
        data = line[9:9+cnt*2]
        crc = line[9+cnt*2:9+cnt*2+2]
        return [addr,hextype,cnt,data,crc]








