import threading
import signal, os
import socket


class WorkThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)


class SocketCom():
    
    def __init__(self,echoFun,rxCallback,disconCallback=None):
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.tcp = None
        self.echo = echoFun
        self.rxcb = rxCallback
        self.discb = disconCallback
        
    def refresh(self):
        self.probThread = WorkThread(self.probeWifi)
        self.probThread.setDaemon(True)
        self.probThread.start()
        
    def probeWifi(self):
        address = ('192.168.1.255', 333)
        self.udp.sendto("hello",address)
        self.udp.settimeout(3)
        try:
            data,addr = self.udp.recvfrom(1024)
            msg = "%s %s:%d" %(data[:-1],addr[0],addr[1])
            self.echo(msg)
            return addr
        except socket.timeout:
            self.echo("probe fail")
            return None

    def send(self,msg):
        try:    
            self.tcp.send(msg)
        except socket.error as e:
            print str(e)
        
    def close(self):
        self.connecting = False
        self.tcp.close()
        self.tcp = None

    def loopTcpRx(self):
        while self.connecting:
            try:
                data = self.tcp.recv(512)
                print "rx",str(data)
                self.rxcb(str(data))
                if len(data) == 0:
                    self.connecting = False
                    self.discb()
                    
            except Exception as e:
                if "timed out" not in str(e):
                    print "RX Error:",str(e)
                    self.connecting = False
                    self.discb()

    def connect(self,port):
        tmp = port.split()[1].split(":")
        addr = (tmp[0],int(tmp[1]))
        try:
            self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.tcp.settimeout(5)
            self.tcp.connect(addr)
            self.tcpRxThread = WorkThread(self.loopTcpRx)
            self.tcpRxThread.setDaemon(True)
            self.connecting = True
            self.tcpRxThread.start()
            return True
        except socket.error,msg:
            print msg
            return False











