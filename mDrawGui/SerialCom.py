import os
import glob
import sys
import serial
import platform
import threading

try:
    import _winreg
except:
    pass


def serialList():
    """
        Retrieve a list of serial ports found in the system.
    :param forAutoDetect: if true then only the USB serial ports are listed. Else all ports are listed.
    :return: A list of strings where each string is a serial port.
    """
    baselist=[]
    if platform.system() == "Windows":
        try:
            key=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"HARDWARE\\DEVICEMAP\\SERIALCOMM")
            i=0
            while True:
                values = _winreg.EnumValue(key, i)
                baselist+=[values[1]]
                i+=1
        except:
            pass

    baselist = baselist + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob("/dev/cu.*") + glob.glob("/dev/tty.usb*") + glob.glob("/dev/rfcomm*") + glob.glob('/dev/serial/by-id/*')
    return baselist

class serialRead(threading.Thread):
    def __init__(self,ser,cb):
        self.ser = ser
        self.cb = cb
        self.running = True
        threading.Thread.__init__(self)
    
    def run(self):
        while self.running:
            l = self.ser.readline()
            print l
            self.cb(l)

class serialCom():
    def __init__(self,rxCallback):
        self.rxcb = rxCallback
        self.ser = None
        return
    
    def connect(self,port,baud=115200):
        self.ser = serial.Serial(port, baud)
        self.rxth = serialRead(self.ser,self.rxcb)
        self.rxth.setDaemon(True)
        self.rxth.start() 
        return
    
    def close(self):
        self.rxth.running = False
        self.ser.close()
        self.rxth = None
        self.ser = None
        
    def send(self,msg):
        if self.ser == None:
            return
        self.ser.write(msg)
        





