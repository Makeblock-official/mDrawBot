# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParserGUI.ui'
#
# Created: Sun Aug  5 17:16:57 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(656, 480))
        Form.setMaximumSize(QtCore.QSize(656, 480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 461, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(480, 220, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btnConvert = QtWidgets.QPushButton(self.groupBox)
        self.btnConvert.setGeometry(QtCore.QRect(40, 110, 121, 23))
        self.btnConvert.setObjectName("btnConvert")
        self.slideThr = QtWidgets.QSlider(self.groupBox)
        self.slideThr.setGeometry(QtCore.QRect(10, 50, 151, 19))
        self.slideThr.setProperty("value", 40)
        self.slideThr.setOrientation(QtCore.Qt.Horizontal)
        self.slideThr.setObjectName("slideThr")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.label.setObjectName("label")
        self.labelThr = QtWidgets.QLabel(self.groupBox)
        self.labelThr.setGeometry(QtCore.QRect(50, 80, 54, 12))
        self.labelThr.setObjectName("labelThr")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(480, 10, 171, 131))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(1480, 150, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnConvert_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConvert_2.setGeometry(QtCore.QRect(40, 40, 121, 23))
        self.btnConvert_2.setObjectName("btnConvert_2")
        self.btnPlotToMain = QtWidgets.QPushButton(Form)
        self.btnPlotToMain.setGeometry(QtCore.QRect(480, 440, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnPlotToMain.setFont(font)
        self.btnPlotToMain.setObjectName("btnPlotToMain")
        self.btnReload = QtWidgets.QPushButton(Form)
        self.btnReload.setGeometry(QtCore.QRect(480, 410, 171, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btnReload.setFont(font)
        self.btnReload.setObjectName("btnReload")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SVG Converter"))
        self.groupBox.setTitle(_translate("Form", "Svg Converter"))
        self.btnConvert.setText(_translate("Form", "Convert to Svg"))
        self.label.setText(_translate("Form", "Threash Hold(%):"))
        self.labelThr.setText(_translate("Form", "0.45"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">Note that only laser kit support original format, if you are using pen or other servo driven kit, please translate bitmap to svg path.</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "Bitmap(only for laser)"))
        self.btnConvert_2.setText(_translate("Form", "Convert to Grey"))
        self.btnPlotToMain.setText(_translate("Form", "Plot to Main Scene"))
        self.btnReload.setText(_translate("Form", "Reload Bitmap Picture"))

