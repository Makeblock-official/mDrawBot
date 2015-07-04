# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScaraGui.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(959, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(959, 720))
        Form.setMaximumSize(QtCore.QSize(959, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/mDraw.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 751, 701))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.graphicsView.setObjectName("graphicsView")
        self.btnLoadPic = QtWidgets.QPushButton(Form)
        self.btnLoadPic.setGeometry(QtCore.QRect(20, 20, 60, 40))
        self.btnLoadPic.setStyleSheet(" QPushButton {\n"
"    border-image: url(:/images/scara-UI-LoadPic_normal.png) 0;\n"
" }\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-LoadPic_hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-LoadPic_click.png) 0;\n"
" }")
        self.btnLoadPic.setText("")
        self.btnLoadPic.setObjectName("btnLoadPic")
        self.btnPrintPic = QtWidgets.QPushButton(Form)
        self.btnPrintPic.setGeometry(QtCore.QRect(160, 20, 96, 40))
        self.btnPrintPic.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnPrintPic.setObjectName("btnPrintPic")
        self.btnClearPic = QtWidgets.QPushButton(Form)
        self.btnClearPic.setGeometry(QtCore.QRect(90, 20, 60, 40))
        self.btnClearPic.setStyleSheet(" QPushButton {\n"
"    border-image: url(:/images/scara-UI-ClearPic_normal.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/scara-UI-ClearPic_hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/scara-UI-ClearPic_click.png) 0;\n"
" }")
        self.btnClearPic.setText("")
        self.btnClearPic.setObjectName("btnClearPic")
        self.btnStop = QtWidgets.QPushButton(Form)
        self.btnStop.setGeometry(QtCore.QRect(270, 20, 60, 40))
        self.btnStop.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnStop.setText("")
        self.btnStop.setObjectName("btnStop")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 680, 731, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.robotCombo = QtWidgets.QComboBox(Form)
        self.robotCombo.setGeometry(QtCore.QRect(770, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.robotCombo.setFont(font)
        self.robotCombo.setStyleSheet(" QComboBox {\n"
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
"}")
        self.robotCombo.setObjectName("robotCombo")
        self.robotCombo.addItem("")
        self.robotCombo.addItem("")
        self.robotCombo.addItem("")
        self.robotCombo.addItem("")
        self.robotCombo.addItem("")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(770, 240, 181, 171))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 49, 49);\n"
"    border: 1px solid rgb(108, 108, 108);\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 179, 169))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(" QTabWidget::pane { /* The tab widget frame */\n"
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
" }r")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabPen = QtWidgets.QWidget()
        self.tabPen.setObjectName("tabPen")
        self.btnPenUp = QtWidgets.QPushButton(self.tabPen)
        self.btnPenUp.setGeometry(QtCore.QRect(10, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnPenUp.setFont(font)
        self.btnPenUp.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnPenUp.setObjectName("btnPenUp")
        self.btnPenDown = QtWidgets.QPushButton(self.tabPen)
        self.btnPenDown.setGeometry(QtCore.QRect(10, 60, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnPenDown.setFont(font)
        self.btnPenDown.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnPenDown.setObjectName("btnPenDown")
        self.penUpSpin = QtWidgets.QSpinBox(self.tabPen)
        self.penUpSpin.setGeometry(QtCore.QRect(100, 20, 71, 22))
        self.penUpSpin.setStyleSheet("color: rgb(230,230,230)")
        self.penUpSpin.setMaximum(180)
        self.penUpSpin.setProperty("value", 130)
        self.penUpSpin.setObjectName("penUpSpin")
        self.penDownSpin = QtWidgets.QSpinBox(self.tabPen)
        self.penDownSpin.setGeometry(QtCore.QRect(100, 60, 71, 22))
        self.penDownSpin.setStyleSheet("color: rgb(230,230,230);")
        self.penDownSpin.setMaximum(180)
        self.penDownSpin.setProperty("value", 90)
        self.penDownSpin.setObjectName("penDownSpin")
        self.btnSavePos = QtWidgets.QPushButton(self.tabPen)
        self.btnSavePos.setGeometry(QtCore.QRect(10, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnSavePos.setFont(font)
        self.btnSavePos.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnSavePos.setObjectName("btnSavePos")
        self.tabWidget.addTab(self.tabPen, "")
        self.tabLaser = QtWidgets.QWidget()
        self.tabLaser.setObjectName("tabLaser")
        self.slideLaserPower = QtWidgets.QSlider(self.tabLaser)
        self.slideLaserPower.setGeometry(QtCore.QRect(20, 60, 121, 19))
        self.slideLaserPower.setStyleSheet("QSlider::handle:horizontal {\n"
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
"}")
        self.slideLaserPower.setMaximum(100)
        self.slideLaserPower.setOrientation(QtCore.Qt.Horizontal)
        self.slideLaserPower.setObjectName("slideLaserPower")
        self.labelLaserDelay = QtWidgets.QLabel(self.tabLaser)
        self.labelLaserDelay.setGeometry(QtCore.QRect(130, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelLaserDelay.setFont(font)
        self.labelLaserDelay.setStyleSheet("color:rgb(204,204,204);")
        self.labelLaserDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLaserDelay.setObjectName("labelLaserDelay")
        self.slideLaserDelay = QtWidgets.QSlider(self.tabLaser)
        self.slideLaserDelay.setGeometry(QtCore.QRect(20, 110, 121, 19))
        self.slideLaserDelay.setStyleSheet("QSlider::handle:horizontal {\n"
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
"}")
        self.slideLaserDelay.setMaximum(100)
        self.slideLaserDelay.setOrientation(QtCore.Qt.Horizontal)
        self.slideLaserDelay.setObjectName("slideLaserDelay")
        self.label_13 = QtWidgets.QLabel(self.tabLaser)
        self.label_13.setGeometry(QtCore.QRect(20, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(204,204,204);")
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.tabLaser)
        self.label_12.setGeometry(QtCore.QRect(20, 40, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(204,204,204);")
        self.label_12.setObjectName("label_12")
        self.labelLaserPower = QtWidgets.QLabel(self.tabLaser)
        self.labelLaserPower.setGeometry(QtCore.QRect(130, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelLaserPower.setFont(font)
        self.labelLaserPower.setStyleSheet("color:rgb(204,204,204);")
        self.labelLaserPower.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLaserPower.setObjectName("labelLaserPower")
        self.radioLaserMode = QtWidgets.QRadioButton(self.tabLaser)
        self.radioLaserMode.setGeometry(QtCore.QRect(20, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.radioLaserMode.setFont(font)
        self.radioLaserMode.setStyleSheet("     color: rgb(230,230,230);\n"
"")
        self.radioLaserMode.setObjectName("radioLaserMode")
        self.tabWidget.addTab(self.tabLaser, "")
        self.tabUtil = QtWidgets.QWidget()
        self.tabUtil.setObjectName("tabUtil")
        self.btnPenUp_2 = QtWidgets.QPushButton(self.tabUtil)
        self.btnPenUp_2.setGeometry(QtCore.QRect(10, 10, 151, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnPenUp_2.setFont(font)
        self.btnPenUp_2.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnPenUp_2.setObjectName("btnPenUp_2")
        self.tabWidget.addTab(self.tabUtil, "")
        self.btnSetRobot = QtWidgets.QPushButton(Form)
        self.btnSetRobot.setGeometry(QtCore.QRect(892, 10, 61, 31))
        self.btnSetRobot.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnSetRobot.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/scara-UI-setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetRobot.setIcon(icon1)
        self.btnSetRobot.setIconSize(QtCore.QSize(24, 24))
        self.btnSetRobot.setObjectName("btnSetRobot")
        self.btnHome = QtWidgets.QPushButton(Form)
        self.btnHome.setGeometry(QtCore.QRect(690, 20, 61, 41))
        self.btnHome.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnHome.setText("")
        self.btnHome.setObjectName("btnHome")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(770, 420, 181, 291))
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(77, 77, 77);\n"
"    border: 1px solid rgb(107, 107, 107);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(1, 1, 179, 289))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(77, 77, 77);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.portCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.portCombo.setGeometry(QtCore.QRect(4, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.portCombo.setFont(font)
        self.portCombo.setStyleSheet(" QComboBox {\n"
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
" }")
        self.portCombo.setObjectName("portCombo")
        self.portCombo.addItem("")
        self.portCombo.addItem("")
        self.btnConnect = QtWidgets.QPushButton(self.groupBox_3)
        self.btnConnect.setGeometry(QtCore.QRect(97, 10, 77, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnConnect.setFont(font)
        self.btnConnect.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnConnect.setObjectName("btnConnect")
        self.textConsole = QtWidgets.QTextEdit(self.groupBox_3)
        self.textConsole.setGeometry(QtCore.QRect(4, 50, 170, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.textConsole.setFont(font)
        self.textConsole.setStyleSheet(" QTextEdit, QListView {\n"
"    color: white;\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: 1px solid rgb(107, 107, 107);\n"
"    border-radius: 3px;\n"
" }")
        self.textConsole.setObjectName("textConsole")
        self.lineSend = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineSend.setGeometry(QtCore.QRect(4, 260, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lineSend.setFont(font)
        self.lineSend.setStyleSheet(" QLineEdit {\n"
"     border: 1px solid rgb(97,97,97);\n"
"     color: rgb(255, 255, 255);\n"
"     background-color:rgb(51,51,51);\n"
" }\n"
"")
        self.lineSend.setObjectName("lineSend")
        self.btnSend = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSend.setGeometry(QtCore.QRect(130, 260, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnSend.setFont(font)
        self.btnSend.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnSend.setObjectName("btnSend")
        self.labelXpos = QtWidgets.QLineEdit(Form)
        self.labelXpos.setGeometry(QtCore.QRect(690, 110, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelXpos.setFont(font)
        self.labelXpos.setStyleSheet(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
"")
        self.labelXpos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXpos.setObjectName("labelXpos")
        self.labelYpos = QtWidgets.QLineEdit(Form)
        self.labelYpos.setGeometry(QtCore.QRect(690, 140, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelYpos.setFont(font)
        self.labelYpos.setStyleSheet(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
"")
        self.labelYpos.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYpos.setObjectName("labelYpos")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(650, 110, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(650, 140, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(770, 50, 181, 181))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(49, 49, 49);\n"
"    border: 1px solid rgb(108, 108, 108);\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.labelModel = QtWidgets.QLabel(self.groupBox_2)
        self.labelModel.setGeometry(QtCore.QRect(10, 10, 161, 131))
        self.labelModel.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-image: url(:/images/scara.png);")
        self.labelModel.setText("")
        self.labelModel.setObjectName("labelModel")
        self.btnUpdateFirmware = QtWidgets.QPushButton(self.groupBox_2)
        self.btnUpdateFirmware.setGeometry(QtCore.QRect(10, 150, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnUpdateFirmware.setFont(font)
        self.btnUpdateFirmware.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnUpdateFirmware.setObjectName("btnUpdateFirmware")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(140, 20, 18, 18))
        self.pushButton.setStyleSheet(" QPushButton {\n"
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
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.btnWiring = QtWidgets.QPushButton(self.groupBox_2)
        self.btnWiring.setGeometry(QtCore.QRect(130, 150, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnWiring.setFont(font)
        self.btnWiring.setStyleSheet(" QPushButton {\n"
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
"")
        self.btnWiring.setObjectName("btnWiring")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(650, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.label_3.setObjectName("label_3")
        self.labelScale = QtWidgets.QLineEdit(Form)
        self.labelScale.setGeometry(QtCore.QRect(690, 170, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelScale.setFont(font)
        self.labelScale.setStyleSheet(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color: rgb(249, 249, 249);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
"")
        self.labelScale.setAlignment(QtCore.Qt.AlignCenter)
        self.labelScale.setObjectName("labelScale")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(650, 170, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.label_4.setObjectName("label_4")
        self.labelPic = QtWidgets.QGroupBox(Form)
        self.labelPic.setGeometry(QtCore.QRect(640, 610, 101, 51))
        self.labelPic.setStyleSheet("QGroupBox{\n"
"    color: black;\n"
"    background-color: rgb(243,243,243);\n"
"    border: 1px solid rgb(124,124,124);\n"
"    border-radius: 3px;\n"
"}\n"
" ")
        self.labelPic.setTitle("")
        self.labelPic.setObjectName("labelPic")
        self.label_5 = QtWidgets.QLabel(self.labelPic)
        self.label_5.setGeometry(QtCore.QRect(5, 5, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color:  rgb(243,243,243);")
        self.label_5.setObjectName("label_5")
        self.lineSvgWidth = QtWidgets.QLineEdit(self.labelPic)
        self.lineSvgWidth.setGeometry(QtCore.QRect(40, 5, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lineSvgWidth.setFont(font)
        self.lineSvgWidth.setStyleSheet(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color:  rgb(243,243,243);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
"")
        self.lineSvgWidth.setText("")
        self.lineSvgWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSvgWidth.setObjectName("lineSvgWidth")
        self.lineSvgHeight = QtWidgets.QLineEdit(self.labelPic)
        self.lineSvgHeight.setGeometry(QtCore.QRect(40, 25, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.lineSvgHeight.setFont(font)
        self.lineSvgHeight.setStyleSheet(" QLineEdit {\n"
"     border: 0px ;\n"
"     color:rgb(124, 124, 124);\n"
"    background-color:  rgb(243,243,243);\n"
"     selection-color: rgb(108, 199, 232);\n"
"     selection-background-color:rgb(249, 249, 249);\n"
"     border-bottom : 1px dashed rgb(124, 124, 124);\n"
" }\n"
"")
        self.lineSvgHeight.setText("")
        self.lineSvgHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSvgHeight.setObjectName("lineSvgHeight")
        self.label_6 = QtWidgets.QLabel(self.labelPic)
        self.label_6.setGeometry(QtCore.QRect(5, 25, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color:  rgb(243,243,243);")
        self.label_6.setObjectName("label_6")
        self.labelEstTime = QtWidgets.QLabel(Form)
        self.labelEstTime.setGeometry(QtCore.QRect(320, 660, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelEstTime.setFont(font)
        self.labelEstTime.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.labelEstTime.setObjectName("labelEstTime")
        self.labelMachineState = QtWidgets.QLabel(Form)
        self.labelMachineState.setGeometry(QtCore.QRect(720, 200, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.labelMachineState.setFont(font)
        self.labelMachineState.setStyleSheet("color: rgb(124, 124, 124);\n"
"background-color: rgb(249, 249, 249);")
        self.labelMachineState.setObjectName("labelMachineState")
        self.btnHFlip = QtWidgets.QPushButton(Form)
        self.btnHFlip.setGeometry(QtCore.QRect(340, 20, 60, 40))
        self.btnHFlip.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image:url(:/images/mDraw_UI-icon-VSymmetric.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-VSymmetric-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-VSymmetric-click.png) 0;\n"
" }\n"
"\n"
"")
        self.btnHFlip.setText("")
        self.btnHFlip.setObjectName("btnHFlip")
        self.btnVFlip = QtWidgets.QPushButton(Form)
        self.btnVFlip.setGeometry(QtCore.QRect(410, 20, 60, 40))
        self.btnVFlip.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image:url(:/images/mDraw_UI-icon-HSymmetric.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-HSymmetric-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-HSymmetric-click.png) 0;\n"
" }\n"
"\n"
"")
        self.btnVFlip.setText("")
        self.btnVFlip.setObjectName("btnVFlip")
        self.btnRollC = QtWidgets.QPushButton(Form)
        self.btnRollC.setGeometry(QtCore.QRect(480, 20, 60, 40))
        self.btnRollC.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image:url(:/images/mDraw_UI-icon-clockwise-rotation.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-clockwise-rotation-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-clockwise-rotation-click.png) 0;\n"
" }\n"
"\n"
"")
        self.btnRollC.setText("")
        self.btnRollC.setObjectName("btnRollC")
        self.btnRollAC = QtWidgets.QPushButton(Form)
        self.btnRollAC.setGeometry(QtCore.QRect(550, 20, 60, 40))
        self.btnRollAC.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image:url(:/images/mDraw_UI-icon-anticlockwise-rotation.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-anticlockwise-rotation-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-anticlockwise-rotation-click.png) 0;\n"
" }\n"
"\n"
"")
        self.btnRollAC.setText("")
        self.btnRollAC.setObjectName("btnRollAC")
        self.btnHelp = QtWidgets.QPushButton(Form)
        self.btnHelp.setGeometry(QtCore.QRect(620, 20, 60, 40))
        self.btnHelp.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image:url(:/images/mDraw_UI-icon-help_info.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-help_info-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    background-color: rgb(249, 249, 249);\n"
"    border-image: url(:/images/mDraw_UI-icon-help_info-click.png) 0;\n"
" }\n"
"\n"
"")
        self.btnHelp.setText("")
        self.btnHelp.setObjectName("btnHelp")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.robotCombo.setItemText(0, _translate("Form", "mScara"))
        self.robotCombo.setItemText(1, _translate("Form", "mSpider"))
        self.robotCombo.setItemText(2, _translate("Form", "mEggBot"))
        self.robotCombo.setItemText(3, _translate("Form", "mCar"))
        self.robotCombo.setItemText(4, _translate("Form", "XY"))
        self.btnPenUp.setText(_translate("Form", "Pen Up"))
        self.btnPenDown.setText(_translate("Form", "Pen Down"))
        self.btnSavePos.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPen), _translate("Form", "Pen"))
        self.labelLaserDelay.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form", "Delay (ms)"))
        self.label_12.setText(_translate("Form", "Power %"))
        self.labelLaserPower.setText(_translate("Form", "0"))
        self.radioLaserMode.setText(_translate("Form", "Enable Laser Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLaser), _translate("Form", "Laser"))
        self.btnPenUp_2.setText(_translate("Form", "Sync Position (G92)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUtil), _translate("Form", "Utils"))
        self.portCombo.setItemText(0, _translate("Form", "No Connection"))
        self.portCombo.setItemText(1, _translate("Form", "新建项目"))
        self.btnConnect.setText(_translate("Form", "Connect"))
        self.btnSend.setText(_translate("Form", "Send"))
        self.label.setText(_translate("Form", "X(mm):"))
        self.label_2.setText(_translate("Form", "Y(mm):"))
        self.btnUpdateFirmware.setText(_translate("Form", "Update Firmware"))
        self.btnWiring.setText(_translate("Form", "Wire"))
        self.label_3.setText(_translate("Form", "Extruder Position"))
        self.label_4.setText(_translate("Form", "Scale:"))
        self.label_5.setText(_translate("Form", "width"))
        self.label_6.setText(_translate("Form", "height"))
        self.labelEstTime.setText(_translate("Form", "Time Left: 00:00:00"))
        self.labelMachineState.setText(_translate("Form", "IDLE"))

import images_rc
