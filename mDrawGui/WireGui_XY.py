# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WireGui_XY.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 608)
        self.labelModel = QtWidgets.QLabel(Form)
        self.labelModel.setGeometry(QtCore.QRect(10, 10, 591, 591))
        self.labelModel.setStyleSheet("")
        self.labelModel.setText("")
        self.labelModel.setPixmap(QtGui.QPixmap(":/images/wire_xy.png"))
        self.labelModel.setObjectName("labelModel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import images_rc
