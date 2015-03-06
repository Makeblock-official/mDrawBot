# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScaraGui.ui'
#
# Created: Sat Feb 28 15:14:23 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(959, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(959, 720))
        Form.setMaximumSize(QtCore.QSize(959, 768))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/mDraw.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(76, 76, 76);"))
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 751, 701))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setStyleSheet(_fromUtf8("background-color: rgb(249, 249, 249);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.btnLoadPic = QtGui.QPushButton(Form)
        self.btnLoadPic.setGeometry(QtCore.QRect(20, 20, 60, 40))
        self.btnLoadPic.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image: url(:/images/scara-UI-LoadPic_normal.png) 0;\n"
" }\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-LoadPic_hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-LoadPic_click.png) 0;\n"
" }"))
        self.btnLoadPic.setText(_fromUtf8(""))
        self.btnLoadPic.setObjectName(_fromUtf8("btnLoadPic"))
        self.btnPrintPic = QtGui.QPushButton(Form)
        self.btnPrintPic.setGeometry(QtCore.QRect(160, 20, 96, 40))
        self.btnPrintPic.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
        self.btnPrintPic.setObjectName(_fromUtf8("btnPrintPic"))
        self.btnClearPic = QtGui.QPushButton(Form)
        self.btnClearPic.setGeometry(QtCore.QRect(90, 20, 60, 40))
        self.btnClearPic.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image: url(:/images/scara-UI-ClearPic_normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-ClearPic_hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-ClearPic_click.png) 0;\n"
" }"))
        self.btnClearPic.setText(_fromUtf8(""))
        self.btnClearPic.setObjectName(_fromUtf8("btnClearPic"))
        self.btnStop = QtGui.QPushButton(Form)
        self.btnStop.setGeometry(QtCore.QRect(270, 20, 60, 40))
        self.btnStop.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/scara-UI-Stop-normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/scara-UI-Stop-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/scara-UI-Stop-click.png) 0;\n"
" }\n"
""))
        self.btnStop.setText(_fromUtf8(""))
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 680, 731, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.robotCombo = QtGui.QComboBox(Form)
        self.robotCombo.setGeometry(QtCore.QRect(770, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.robotCombo.setFont(font)
        self.robotCombo.setStyleSheet(_fromUtf8(" QComboBox {\n"
"     color: rgb(255, 255, 255);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"     border: 0px;\n"
" }\n"
" QComboBox::down-arrow {\n"
"    border-image: url(:/images/scara-UI-drop_down.png);\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(230, 230, 230);\n"
"     border: 2px solid darkgray;\n"
"     border-radius: 4px;\n"
"     selection-background-color: rgb(127,127,127);\n"
"     min-height: 80px;\n"
"}"))
        self.robotCombo.setObjectName(_fromUtf8("robotCombo"))
        self.robotCombo.addItem(_fromUtf8(""))
        self.robotCombo.addItem(_fromUtf8(""))
        self.robotCombo.addItem(_fromUtf8(""))
        self.robotCombo.addItem(_fromUtf8(""))
        self.robotCombo.addItem(_fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(770, 240, 181, 171))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox {\n"
"    background-color: rgb(49, 49, 49);\n"
"    border: 1px solid rgb(108, 108, 108);\n"
"    border-radius: 5px;\n"
"}"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 179, 169))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8(" QTabWidget::pane { /* The tab widget frame */\n"
"    background-color: rgb(77, 77, 77);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-top : 1px;\n"
"    border-radius: 5px;\n"
" } \n"
"\n"
"QTabBar::tab {\n"
"     color: rgb(108,108,108);\n"
"     background-color: rgb(49, 49, 49);\n"
"     border: 1px solid rgb(40, 40, 40);\n"
"     border-bottom-color: rgb(77, 77, 77);\n"
"     border-top-left-radius: 0px;\n"
"     border-top-right-radius: 2px;\n"
"     height: 22px;\n"
"     padding: 2px;\n"
"     min-width: 50px;\n"
" }\n"
" QTabBar::tab:selected{\n"
"     color: white;\n"
"     background-color: rgb(77, 77, 77);\n"
" }r"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabPen = QtGui.QWidget()
        self.tabPen.setObjectName(_fromUtf8("tabPen"))
        self.btnPenUp = QtGui.QPushButton(self.tabPen)
        self.btnPenUp.setGeometry(QtCore.QRect(10, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnPenUp.setFont(font)
        self.btnPenUp.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnPenUp.setObjectName(_fromUtf8("btnPenUp"))
        self.linePenUp = QtGui.QLineEdit(self.tabPen)
        self.linePenUp.setGeometry(QtCore.QRect(100, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.linePenUp.setFont(font)
        self.linePenUp.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color: rgb(255, 255, 255);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color: rgb(76, 76, 76);\n"
"     border-bottom : 1px dashed white;\n"
" }\n"
""))
        self.linePenUp.setAlignment(QtCore.Qt.AlignCenter)
        self.linePenUp.setObjectName(_fromUtf8("linePenUp"))
        self.btnPenDown = QtGui.QPushButton(self.tabPen)
        self.btnPenDown.setGeometry(QtCore.QRect(10, 60, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnPenDown.setFont(font)
        self.btnPenDown.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnPenDown.setObjectName(_fromUtf8("btnPenDown"))
        self.linePenDown = QtGui.QLineEdit(self.tabPen)
        self.linePenDown.setGeometry(QtCore.QRect(100, 60, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.linePenDown.setFont(font)
        self.linePenDown.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color: rgb(255, 255, 255);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color: rgb(76, 76, 76);\n"
"     border-bottom : 1px dashed white;\n"
" }\n"
""))
        self.linePenDown.setAlignment(QtCore.Qt.AlignCenter)
        self.linePenDown.setObjectName(_fromUtf8("linePenDown"))
        self.tabWidget.addTab(self.tabPen, _fromUtf8(""))
        self.tabLaser = QtGui.QWidget()
        self.tabLaser.setObjectName(_fromUtf8("tabLaser"))
        self.slideLaserPower = QtGui.QSlider(self.tabLaser)
        self.slideLaserPower.setGeometry(QtCore.QRect(10, 20, 121, 19))
        self.slideLaserPower.setStyleSheet(_fromUtf8("QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     border-radius: 3px;\n"
"     margin: -8px 0; /* expand outside the groove */\n"
"     width: 10px;\n"
"     height: 18px;\n"
" }\n"
"QSlider::groove:horizontal {\n"
"    height: 3px;\n"
"    background-color: rgb(53, 53, 53);\n"
"    border: 1px solid #5c5c5c;\n"
"}"))
        self.slideLaserPower.setMaximum(254)
        self.slideLaserPower.setOrientation(QtCore.Qt.Horizontal)
        self.slideLaserPower.setObjectName(_fromUtf8("slideLaserPower"))
        self.labelLaserDelay = QtGui.QLabel(self.tabLaser)
        self.labelLaserDelay.setGeometry(QtCore.QRect(130, 70, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.labelLaserDelay.setFont(font)
        self.labelLaserDelay.setStyleSheet(_fromUtf8("color:rgb(204,204,204);"))
        self.labelLaserDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLaserDelay.setObjectName(_fromUtf8("labelLaserDelay"))
        self.slideLaserDelay = QtGui.QSlider(self.tabLaser)
        self.slideLaserDelay.setGeometry(QtCore.QRect(10, 70, 121, 19))
        self.slideLaserDelay.setStyleSheet(_fromUtf8("QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"     border: 1px solid #5c5c5c;\n"
"     border-radius: 3px;\n"
"     margin: -8px 0; /* expand outside the groove */\n"
"     width: 10px;\n"
"     height: 18px;\n"
" }\n"
"QSlider::groove:horizontal {\n"
"    height: 3px;\n"
"    background-color: rgb(53, 53, 53);\n"
"    border: 1px solid #5c5c5c;\n"
"}"))
        self.slideLaserDelay.setMaximum(100)
        self.slideLaserDelay.setOrientation(QtCore.Qt.Horizontal)
        self.slideLaserDelay.setObjectName(_fromUtf8("slideLaserDelay"))
        self.label_13 = QtGui.QLabel(self.tabLaser)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("color:rgb(204,204,204);"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_12 = QtGui.QLabel(self.tabLaser)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("color:rgb(204,204,204);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.labelLaserPower = QtGui.QLabel(self.tabLaser)
        self.labelLaserPower.setGeometry(QtCore.QRect(130, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.labelLaserPower.setFont(font)
        self.labelLaserPower.setStyleSheet(_fromUtf8("color:rgb(204,204,204);"))
        self.labelLaserPower.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLaserPower.setObjectName(_fromUtf8("labelLaserPower"))
        self.btnLaserStart = QtGui.QPushButton(self.tabLaser)
        self.btnLaserStart.setGeometry(QtCore.QRect(10, 110, 61, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnLaserStart.setFont(font)
        self.btnLaserStart.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnLaserStart.setObjectName(_fromUtf8("btnLaserStart"))
        self.btnLaserReset = QtGui.QPushButton(self.tabLaser)
        self.btnLaserReset.setGeometry(QtCore.QRect(100, 110, 61, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnLaserReset.setFont(font)
        self.btnLaserReset.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnLaserReset.setObjectName(_fromUtf8("btnLaserReset"))
        self.tabWidget.addTab(self.tabLaser, _fromUtf8(""))
        self.btnSetRobot = QtGui.QPushButton(Form)
        self.btnSetRobot.setGeometry(QtCore.QRect(892, 10, 61, 31))
        self.btnSetRobot.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(178,178,178);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnSetRobot.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/scara-UI-setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetRobot.setIcon(icon1)
        self.btnSetRobot.setIconSize(QtCore.QSize(24, 24))
        self.btnSetRobot.setObjectName(_fromUtf8("btnSetRobot"))
        self.btnHome = QtGui.QPushButton(Form)
        self.btnHome.setGeometry(QtCore.QRect(690, 20, 61, 41))
        self.btnHome.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image: url(:/images/scara-UI-home-normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-home-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-home-click.png) 0;\n"
" }\n"
""))
        self.btnHome.setText(_fromUtf8(""))
        self.btnHome.setObjectName(_fromUtf8("btnHome"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(770, 420, 181, 291))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox {\n"
"    background-color: rgb(77, 77, 77);\n"
"    border: 1px solid rgb(107, 107, 107);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(1, 1, 179, 289))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox {\n"
"    background-color: rgb(77, 77, 77);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(255, 255, 255);\n"
"}"))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.portCombo = QtGui.QComboBox(self.groupBox_3)
        self.portCombo.setGeometry(QtCore.QRect(4, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.portCombo.setFont(font)
        self.portCombo.setStyleSheet(_fromUtf8(" QComboBox {\n"
"     color: rgb(255, 255, 255);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     border: 0px;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(230, 230, 230);\n"
"     border: 2px solid darkgray;\n"
"     border-radius: 3px;\n"
"     selection-background-color: rgb(127,127,127);\n"
"     min-height: 80px;\n"
"}\n"
" QComboBox::down-arrow {\n"
"    border-image: url(:/images/scara-UI-drop_down.png);\n"
" }"))
        self.portCombo.setObjectName(_fromUtf8("portCombo"))
        self.portCombo.addItem(_fromUtf8(""))
        self.portCombo.addItem(_fromUtf8(""))
        self.btnConnect = QtGui.QPushButton(self.groupBox_3)
        self.btnConnect.setGeometry(QtCore.QRect(97, 10, 77, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnConnect.setFont(font)
        self.btnConnect.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.textConsole = QtGui.QTextEdit(self.groupBox_3)
        self.textConsole.setGeometry(QtCore.QRect(4, 50, 170, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.textConsole.setFont(font)
        self.textConsole.setStyleSheet(_fromUtf8(" QTextEdit, QListView {\n"
"    color: white;\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 1px solid rgb(107, 107, 107);\n"
"    border-radius: 3px;\n"
" }"))
        self.textConsole.setObjectName(_fromUtf8("textConsole"))
        self.lineSend = QtGui.QLineEdit(self.groupBox_3)
        self.lineSend.setGeometry(QtCore.QRect(4, 260, 121, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lineSend.setFont(font)
        self.lineSend.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 1px solid rgb(97,97,97);\n"
"     color: rgb(255, 255, 255);\n"
"     background-color:rgb(51,51,51);\n"
" }\n"
""))
        self.lineSend.setObjectName(_fromUtf8("lineSend"))
        self.btnSend = QtGui.QPushButton(self.groupBox_3)
        self.btnSend.setGeometry(QtCore.QRect(130, 260, 41, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnSend.setFont(font)
        self.btnSend.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 3px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.labelXpos = QtGui.QLineEdit(Form)
        self.labelXpos.setGeometry(QtCore.QRect(690, 110, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.labelXpos.setFont(font)
        self.labelXpos.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
""))
        self.labelXpos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXpos.setObjectName(_fromUtf8("labelXpos"))
        self.labelYpos = QtGui.QLineEdit(Form)
        self.labelYpos.setGeometry(QtCore.QRect(690, 140, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.labelYpos.setFont(font)
        self.labelYpos.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
""))
        self.labelYpos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYpos.setObjectName(_fromUtf8("labelYpos"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(650, 110, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(650, 140, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(770, 50, 181, 181))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
"    background-color: rgb(49, 49, 49);\n"
"    border: 1px solid rgb(108, 108, 108);\n"
"    border-radius: 5px;\n"
"}"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.labelModel = QtGui.QLabel(self.groupBox_2)
        self.labelModel.setGeometry(QtCore.QRect(10, 10, 161, 131))
        self.labelModel.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);\n"
"border-image: url(:/images/scara.png);"))
        self.labelModel.setText(_fromUtf8(""))
        self.labelModel.setObjectName(_fromUtf8("labelModel"))
        self.btnUpdateFirmware = QtGui.QPushButton(self.groupBox_2)
        self.btnUpdateFirmware.setGeometry(QtCore.QRect(10, 150, 131, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdateFirmware.setFont(font)
        self.btnUpdateFirmware.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     color: rgb(230,230,230);\n"
"     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #6E6E6E,stop:1 #5F5F5F);\n"
" }\n"
"\n"
" QPushButton::hover {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #787878);\n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"     color: rgb(231,231,231);\n"
"     background-color: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:0.7 #828282,stop:1 #6E6E6E);\n"
" }\n"
"\n"
""))
        self.btnUpdateFirmware.setObjectName(_fromUtf8("btnUpdateFirmware"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 120, 18, 18))
        self.pushButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-image: url(:/images/mDraw-info-icon.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-image: url(:/images/mDraw-info-icon-click.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-image: url(:/images/mDraw-info-icon-hover.png) 0;\n"
" }\n"
""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(650, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelScale = QtGui.QLineEdit(Form)
        self.labelScale.setGeometry(QtCore.QRect(690, 170, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.labelScale.setFont(font)
        self.labelScale.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
""))
        self.labelScale.setAlignment(QtCore.Qt.AlignCenter)
        self.labelScale.setObjectName(_fromUtf8("labelScale"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(650, 170, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.labelPic = QtGui.QGroupBox(Form)
        self.labelPic.setGeometry(QtCore.QRect(640, 610, 101, 51))
        self.labelPic.setStyleSheet(_fromUtf8("QGroupBox{\n"
"    color: black;\n"
"    background-color: rgb(243,243,243);\n"
"    border: 1px solid rgb(124,124,124);\n"
"    border-radius: 3px;\n"
"}\n"
" "))
        self.labelPic.setTitle(_fromUtf8(""))
        self.labelPic.setObjectName(_fromUtf8("labelPic"))
        self.label_5 = QtGui.QLabel(self.labelPic)
        self.label_5.setGeometry(QtCore.QRect(5, 5, 31, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color:  rgb(243,243,243);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineSvgWidth = QtGui.QLineEdit(self.labelPic)
        self.lineSvgWidth.setGeometry(QtCore.QRect(40, 5, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lineSvgWidth.setFont(font)
        self.lineSvgWidth.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color:  rgb(243,243,243);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
""))
        self.lineSvgWidth.setText(_fromUtf8(""))
        self.lineSvgWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSvgWidth.setObjectName(_fromUtf8("lineSvgWidth"))
        self.lineSvgHeight = QtGui.QLineEdit(self.labelPic)
        self.lineSvgHeight.setGeometry(QtCore.QRect(40, 25, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lineSvgHeight.setFont(font)
        self.lineSvgHeight.setStyleSheet(_fromUtf8(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color:  rgb(243,243,243);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
""))
        self.lineSvgHeight.setText(_fromUtf8(""))
        self.lineSvgHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSvgHeight.setObjectName(_fromUtf8("lineSvgHeight"))
        self.label_6 = QtGui.QLabel(self.labelPic)
        self.label_6.setGeometry(QtCore.QRect(5, 25, 31, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(124, 124, 124);\n"
"background-color:  rgb(243,243,243);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.robotCombo.setItemText(0, _translate("Form", "mScara", None))
        self.robotCombo.setItemText(1, _translate("Form", "mSpider", None))
        self.robotCombo.setItemText(2, _translate("Form", "mEggBot", None))
        self.robotCombo.setItemText(3, _translate("Form", "mCar", None))
        self.robotCombo.setItemText(4, _translate("Form", "XY", None))
        self.btnPenUp.setText(_translate("Form", "Pen Up", None))
        self.linePenUp.setText(_translate("Form", "M1 130", None))
        self.btnPenDown.setText(_translate("Form", "Pen Down", None))
        self.linePenDown.setText(_translate("Form", "M1 90", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPen), _translate("Form", "Pen", None))
        self.labelLaserDelay.setText(_translate("Form", "0", None))
        self.label_13.setText(_translate("Form", "Delay", None))
        self.label_12.setText(_translate("Form", "Power", None))
        self.labelLaserPower.setText(_translate("Form", "0", None))
        self.btnLaserStart.setText(_translate("Form", "On", None))
        self.btnLaserReset.setText(_translate("Form", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLaser), _translate("Form", "Laser", None))
        self.portCombo.setItemText(0, _translate("Form", "No Connection", None))
        self.portCombo.setItemText(1, _translate("Form", "新建项目", None))
        self.btnConnect.setText(_translate("Form", "Connect", None))
        self.btnSend.setText(_translate("Form", "Send", None))
        self.label.setText(_translate("Form", "X(mm):", None))
        self.label_2.setText(_translate("Form", "Y(mm):", None))
        self.btnUpdateFirmware.setText(_translate("Form", "Update Firmware", None))
        self.label_3.setText(_translate("Form", "Extruder Position", None))
        self.label_4.setText(_translate("Form", "Scale:", None))
        self.label_5.setText(_translate("Form", "width", None))
        self.label_6.setText(_translate("Form", "height", None))

import images_rc
