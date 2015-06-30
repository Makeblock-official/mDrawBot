# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpiderSetup.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(990, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(990, 480))
        Form.setMaximumSize(QtCore.QSize(990, 480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 151, 16))
        self.label_2.setObjectName("label_2")
        self.lineAB = QtWidgets.QLineEdit(self.groupBox)
        self.lineAB.setGeometry(QtCore.QRect(180, 50, 113, 20))
        self.lineAB.setObjectName("lineAB")
        self.lineHeight = QtWidgets.QLineEdit(self.groupBox)
        self.lineHeight.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.lineHeight.setObjectName("lineHeight")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_4.setObjectName("label_4")
        self.motoA_CK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 110, 51, 51))
        self.motoA_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoA_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoA_CK.setObjectName("motoA_CK")
        self.motoB_CK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 170, 51, 51))
        self.motoB_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoB_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoB_CK.setObjectName("motoB_CK")
        self.motoA_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 110, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoA_CCK.setObjectName("motoA_CCK")
        self.motoB_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 170, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoB_CCK.setObjectName("motoB_CCK")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 24, 24))
        self.pushButton.setStyleSheet(" QPushButton {\n"
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
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 230, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 230, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_7.setObjectName("label_7")
        self.lineScale = QtWidgets.QLineEdit(self.groupBox)
        self.lineScale.setGeometry(QtCore.QRect(180, 20, 113, 20))
        self.lineScale.setObjectName("lineScale")
        self.btnOk = QtWidgets.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(290, 280, 91, 23))
        self.btnOk.setObjectName("btnOk")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(400, 10, 581, 471))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/images/mSpider_setup.png"))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Spider Setups"))
        self.label.setText(_translate("Form", "A-B Hang Width (mm):"))
        self.label_2.setText(_translate("Form", "AB-O Hang Height (mm):"))
        self.label_3.setText(_translate("Form", "Motor A Directoin:"))
        self.label_4.setText(_translate("Form", "Motor B Directoin:"))
        self.label_5.setText(_translate("Form", "ClockWise"))
        self.label_6.setText(_translate("Form", "Anti ClockWise"))
        self.label_7.setText(_translate("Form", "Scaler :"))
        self.btnOk.setText(_translate("Form", "Ok"))

import images_rc
