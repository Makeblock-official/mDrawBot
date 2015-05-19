# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScaraSetup.ui'
#
# Created: Tue May 19 12:51:53 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 310)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Dialog.setFont(font)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 261))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineArm0 = QtGui.QLineEdit(self.groupBox)
        self.lineArm0.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.lineArm0.setObjectName(_fromUtf8("lineArm0"))
        self.lineArm1 = QtGui.QLineEdit(self.groupBox)
        self.lineArm1.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.lineArm1.setObjectName(_fromUtf8("lineArm1"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.motoA_CK = QtGui.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 120, 51, 51))
        self.motoA_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoA_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoA_CK.setObjectName(_fromUtf8("motoA_CK"))
        self.motoB_CK = QtGui.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 180, 51, 51))
        self.motoB_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoB_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoB_CK.setObjectName(_fromUtf8("motoB_CK"))
        self.motoA_CCK = QtGui.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 120, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-anticlockwise.png")))
        self.motoA_CCK.setObjectName(_fromUtf8("motoA_CCK"))
        self.motoB_CCK = QtGui.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 180, 51, 51))
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
        self.label_5.setGeometry(QtCore.QRect(170, 240, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 240, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.slidSpeed = QtGui.QSlider(self.groupBox)
        self.slidSpeed.setGeometry(QtCore.QRect(180, 90, 160, 19))
        self.slidSpeed.setProperty("value", 50)
        self.slidSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.slidSpeed.setObjectName(_fromUtf8("slidSpeed"))
        self.labelSpeed = QtGui.QLabel(self.groupBox)
        self.labelSpeed.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.labelSpeed.setObjectName(_fromUtf8("labelSpeed"))
        self.btnOk = QtGui.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(290, 280, 91, 23))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Scara Setups", None))
        self.label.setText(_translate("Dialog", "Arm A Length (mm):", None))
        self.label_2.setText(_translate("Dialog", "Arm B Length (mm):", None))
        self.label_3.setText(_translate("Dialog", "Stepper A Directoin:", None))
        self.label_4.setText(_translate("Dialog", "Stepper B Directoin:", None))
        self.label_5.setText(_translate("Dialog", "ClockWise", None))
        self.label_6.setText(_translate("Dialog", "Anti ClockWise", None))
        self.labelSpeed.setText(_translate("Dialog", "Speed (50%):", None))
        self.btnOk.setText(_translate("Dialog", "Ok", None))

import images_rc
