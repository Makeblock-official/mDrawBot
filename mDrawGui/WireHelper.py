#-*-encoding:utf-8-*-
import sys
import os
import threading
import queue
import time
import mDraw
import WireGui

from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *

class WireHelper(QWidget):
    def __init__(self,uidialog):
        super(WireHelper, self).__init__()
        self.ui = uidialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Wiring')
        self.show()

