import sys
import os
import threading
from PyQt4 import QtGui
from PyQt4.QtCore import *
import threading
import subprocess
import ParserGUI

class WorkInThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)

class HexDownloader():
    def __init__(self, com, sig):
        self.com = com
        self.sig = sig












