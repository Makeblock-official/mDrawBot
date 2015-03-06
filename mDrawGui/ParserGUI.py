# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParserGUI.ui'
#
# Created: Thu Jan 15 16:57:38 2015
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
        Form.resize(656, 480)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 461, 461))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(480, 220, 171, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnConvert = QtGui.QPushButton(self.groupBox)
        self.btnConvert.setGeometry(QtCore.QRect(60, 110, 101, 23))
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))
        self.slideThr = QtGui.QSlider(self.groupBox)
        self.slideThr.setGeometry(QtCore.QRect(10, 50, 151, 19))
        self.slideThr.setProperty("value", 40)
        self.slideThr.setOrientation(QtCore.Qt.Horizontal)
        self.slideThr.setObjectName(_fromUtf8("slideThr"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.labelThr = QtGui.QLabel(self.groupBox)
        self.labelThr.setGeometry(QtCore.QRect(50, 80, 54, 12))
        self.labelThr.setObjectName(_fromUtf8("labelThr"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(480, 10, 171, 131))
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 150, 171, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnConvert_2 = QtGui.QPushButton(self.groupBox_2)
        self.btnConvert_2.setGeometry(QtCore.QRect(40, 40, 121, 23))
        self.btnConvert_2.setObjectName(_fromUtf8("btnConvert_2"))
        self.btnPlotToMain = QtGui.QPushButton(Form)
        self.btnPlotToMain.setGeometry(QtCore.QRect(480, 440, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.btnPlotToMain.setFont(font)
        self.btnPlotToMain.setObjectName(_fromUtf8("btnPlotToMain"))
        self.btnReload = QtGui.QPushButton(Form)
        self.btnReload.setGeometry(QtCore.QRect(480, 410, 171, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.btnReload.setFont(font)
        self.btnReload.setObjectName(_fromUtf8("btnReload"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Svg Converter", None))
        self.btnConvert.setText(_translate("Form", "Convert to Svg", None))
        self.label.setText(_translate("Form", "Threash Hold(%):", None))
        self.labelThr.setText(_translate("Form", "0.45", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">Note that only laser kit support original format, if you are using pen or other servo driven kit, please translate bitmap to svg path.</span></p></body></html>", None))
        self.groupBox_2.setTitle(_translate("Form", "Bitmap(only for laser)", None))
        self.btnConvert_2.setText(_translate("Form", "Convert to Grey", None))
        self.btnPlotToMain.setText(_translate("Form", "Plot to Main Scene", None))
        self.btnReload.setText(_translate("Form", "Reload Bitmap Picture", None))

