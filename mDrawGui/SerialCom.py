import os
import glob
import sys
import serial
import platform
import threading

# http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
def serialList():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
#             s = serial.Serial(port)
#             s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class serialRead(threading.Thread):
    def __init__(self,ser,cb):
        self.ser = ser
        self.cb = cb
        self.running = True
        threading.Thread.__init__(self)
    
    def run(self):
        while self.running:
            l = self.ser.readline().decode('utf-8')
            # print("read: "+l) receive log
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
        self.ser.write(msg.encode('utf-8'))
        # print("send: "+msg) # send log
        





