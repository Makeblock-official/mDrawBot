# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarSetup.ui'
#
# Created: Sun Aug  5 14:35:42 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1020, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1020, 316))
        Form.setMaximumSize(QtCore.QSize(1020, 316))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.btnOk = QtWidgets.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(290, 280, 91, 23))
        self.btnOk.setObjectName("btnOk")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.label_4.setObjectName("label_4")
        self.motoA_CK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 120, 51, 51))
        self.motoA_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoA_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoA_CK.setObjectName("motoA_CK")
        self.motoB_CK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 180, 51, 51))
        self.motoB_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoB_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoB_CK.setObjectName("motoB_CK")
        self.motoA_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 120, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoA_CCK.setObjectName("motoA_CCK")
        self.motoB_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 180, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoB_CCK.setObjectName("motoB_CCK")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 240, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 240, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 151, 16))
        self.label_7.setObjectName("label_7")
        self.lineScale = QtWidgets.QLineEdit(self.groupBox)
        self.lineScale.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.lineScale.setObjectName("lineScale")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label.setObjectName("label")
        self.lineWidth = QtWidgets.QLineEdit(self.groupBox)
        self.lineWidth.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.lineWidth.setObjectName("lineWidth")
        self.radioHermit = QtWidgets.QRadioButton(self.groupBox)
        self.radioHermit.setGeometry(QtCore.QRect(20, 90, 281, 16))
        self.radioHermit.setObjectName("radioHermit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 611, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/mCar_setup.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnOk.setText(_translate("Form", "Ok"))
        self.groupBox.setTitle(_translate("Form", "Car Setups"))
        self.label_3.setText(_translate("Form", "Motor A Directoin:"))
        self.label_4.setText(_translate("Form", "Motor B Directoin:"))
        self.label_5.setText(_translate("Form", "ClockWise"))
        self.label_6.setText(_translate("Form", "Anti ClockWise"))
        self.label_7.setText(_translate("Form", "Scaler :"))
        self.label.setText(_translate("Form", "Width (mm):"))
        self.radioHermit.setText(_translate("Form", "Use Hermit interpolation Algorithm"))

import images_rc
