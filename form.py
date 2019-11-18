# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 398)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 541, 291))
        self.groupBox.setStyleSheet("font: 12pt \"Calibri\";")
        self.groupBox.setObjectName("groupBox")
        self.url_label = QtWidgets.QLabel(self.groupBox)
        self.url_label.setGeometry(QtCore.QRect(40, 40, 51, 31))
        self.url_label.setObjectName("url_label")
        self.url_text = QtWidgets.QLineEdit(self.groupBox)
        self.url_text.setGeometry(QtCore.QRect(90, 40, 431, 31))
        self.url_text.setText("")
        self.url_text.setObjectName("url_text")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(40, 160, 51, 31))
        self.name_label.setObjectName("name_label")
        self.time_label = QtWidgets.QLabel(self.groupBox)
        self.time_label.setGeometry(QtCore.QRect(40, 100, 51, 31))
        self.time_label.setObjectName("time_label")
        self.id_label = QtWidgets.QLabel(self.groupBox)
        self.id_label.setGeometry(QtCore.QRect(40, 220, 51, 31))
        self.id_label.setObjectName("id_label")
        self.time_text = QtWidgets.QLineEdit(self.groupBox)
        self.time_text.setGeometry(QtCore.QRect(90, 100, 201, 31))
        self.time_text.setObjectName("time_text")
        self.name_text = QtWidgets.QLineEdit(self.groupBox)
        self.name_text.setGeometry(QtCore.QRect(90, 160, 201, 31))
        self.name_text.setObjectName("name_text")
        self.id_text = QtWidgets.QLineEdit(self.groupBox)
        self.id_text.setGeometry(QtCore.QRect(90, 220, 201, 31))
        self.id_text.setObjectName("id_text")
        self.result_text = QtWidgets.QTextEdit(self.groupBox)
        self.result_text.setGeometry(QtCore.QRect(310, 100, 211, 151))
        self.result_text.setObjectName("result_text")
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(140, 340, 75, 31))
        self.AddButton.setStyleSheet("font: 12pt \"Calibri\";")
        self.AddButton.setObjectName("AddButton")
        self.confirmButton = QtWidgets.QPushButton(Form)
        self.confirmButton.setGeometry(QtCore.QRect(390, 340, 75, 31))
        self.confirmButton.setStyleSheet("font: 12pt \"Calibri\";")
        self.confirmButton.setObjectName("confirmButton")

        self.retranslateUi(Form)
        self.AddButton.clicked.connect(Form.add)
        self.confirmButton.clicked.connect(Form.confirm)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "请输入本次讲座信息"))
        self.url_label.setText(_translate("Form", "URL:"))
        self.name_label.setText(_translate("Form", "姓名:"))
        self.time_label.setText(_translate("Form", "时间:"))
        self.id_label.setText(_translate("Form", "学号:"))
        self.AddButton.setText(_translate("Form", "添加"))
        self.confirmButton.setText(_translate("Form", "查询"))
