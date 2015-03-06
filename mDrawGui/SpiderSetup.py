# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpiderSetup.ui'
#
# Created: Wed Jan 28 10:32:46 2015
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
        Form.resize(400, 310)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineAB = QtGui.QLineEdit(self.groupBox)
        self.lineAB.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.lineAB.setObjectName(_fromUtf8("lineAB"))
        self.lineHeight = QtGui.QLineEdit(self.groupBox)
        self.lineHeight.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.lineHeight.setObjectName(_fromUtf8("lineHeight"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.motoA_CK = QtGui.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 110, 51, 51))
        self.motoA_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoA_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoA_CK.setObjectName(_fromUtf8("motoA_CK"))
        self.motoB_CK = QtGui.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 170, 51, 51))
        self.motoB_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoB_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoB_CK.setObjectName(_fromUtf8("motoB_CK"))
        self.motoA_CCK = QtGui.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 110, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-anticlockwise.png")))
        self.motoA_CCK.setObjectName(_fromUtf8("motoA_CCK"))
        self.motoB_CCK = QtGui.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 170, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-anticlockwise.png")))
        self.motoB_CCK.setObjectName(_fromUtf8("motoB_CCK"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 24, 24))
        self.pushButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image: url(:/images/help-icon.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/help-icon-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/help-icon-click.png) 0;\n"
" }\n"
""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 230, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 230, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineScale = QtGui.QLineEdit(self.groupBox)
        self.lineScale.setGeometry(QtCore.QRect(180, 20, 113, 20))
        self.lineScale.setObjectName(_fromUtf8("lineScale"))
        self.btnOk = QtGui.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(290, 280, 91, 23))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Spider Setups", None))
        self.label.setText(_translate("Form", "A-B Hang Width (mm):", None))
        self.label_2.setText(_translate("Form", "AB-O Hang Height (mm):", None))
        self.label_3.setText(_translate("Form", "Stepper A Directoin:", None))
        self.label_4.setText(_translate("Form", "Stepper B Directoin:", None))
        self.label_5.setText(_translate("Form", "ClockWise", None))
        self.label_6.setText(_translate("Form", "Anti ClockWise", None))
        self.label_7.setText(_translate("Form", "Scaler :", None))
        self.btnOk.setText(_translate("Form", "Ok", None))

import images_rc
