import threading

DEBUG_NORMAL = 0
DEBUG_DEBUG = -2
DEBUG_ERR = -3
IDLE = 0
BUSYING = 1

motorSelectedStyle = "border: 1px solid rgb(67,67,67);\r\nborder-radius: 4px;\r\n"

class WorkInThread(threading.Thread):
    def __init__(self, target, *args):
        self.targetFun = target
        self.kArgs = args
        threading.Thread.__init__(self)
 
    def run(self):
        self.targetFun(*self.kArgs)














