# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctormain.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 750)
        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setGeometry(QtCore.QRect(20, 10, 841, 671))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setGeometry(QtCore.QRect(310, 20, 531, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_patient = QtWidgets.QWidget()
        self.page_patient.setObjectName("page_patient")
        self.tableWidget = QtWidgets.QTableWidget(self.page_patient)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 511, 541))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_patient)
        self.page_add = QtWidgets.QWidget()
        self.page_add.setObjectName("page_add")
        self.frame_8 = QtWidgets.QFrame(self.page_add)
        self.frame_8.setGeometry(QtCore.QRect(-10, 50, 541, 521))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setGeometry(QtCore.QRect(10, 10, 501, 80))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame_8)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(30, 110, 565, 166))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setGeometry(QtCore.QRect(50, 290, 475, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(475, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(170, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 350, 475, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(475, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:white;\n"
"    background-color:rgb(230, 162, 149);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_add)
        self.page_ward = QtWidgets.QWidget()
        self.page_ward.setObjectName("page_ward")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_ward)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 30, 511, 571))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_ward)
        self.page_profile = QtWidgets.QWidget()
        self.page_profile.setObjectName("page_profile")
        self.frame = QtWidgets.QFrame(self.page_profile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 501, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(1, 4, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 160, 501, 411))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 504, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 240, 438, 102))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm.setSizePolicy(sizePolicy)
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_confirm.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(170, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.horizontalLayout_2.addWidget(self.pushButton_confirm)
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:white;\n"
"    background-color:rgb(230, 162, 149);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.stackedWidget.addWidget(self.page_profile)
        self.page_treatment = QtWidgets.QWidget()
        self.page_treatment.setObjectName("page_treatment")
        self.label_11 = QtWidgets.QLabel(self.page_treatment)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 431, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_patient = QtWidgets.QLineEdit(self.page_treatment)
        self.lineEdit_patient.setGeometry(QtCore.QRect(320, 40, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_patient.sizePolicy().hasHeightForWidth())
        self.lineEdit_patient.setSizePolicy(sizePolicy)
        self.lineEdit_patient.setMinimumSize(QtCore.QSize(150, 50))
        self.lineEdit_patient.setMaximumSize(QtCore.QSize(150, 50))
        self.lineEdit_patient.setReadOnly(True)
        self.lineEdit_patient.setObjectName("lineEdit_patient")
        self.textEdit = QtWidgets.QTextEdit(self.page_treatment)
        self.textEdit.setGeometry(QtCore.QRect(10, 120, 491, 331))
        self.textEdit.setObjectName("textEdit")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_treatment)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 470, 589, 37))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(360, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(360, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_treatment)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 501, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_confirm_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm_2.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm_2.setSizePolicy(sizePolicy)
        self.pushButton_confirm_2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_confirm_2.setFont(font)
        self.pushButton_confirm_2.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(170, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(85, 255, 255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_confirm_2.setObjectName("pushButton_confirm_2")
        self.horizontalLayout.addWidget(self.pushButton_confirm_2)
        self.pushButton_cancel_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel_2.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel_2.setSizePolicy(sizePolicy)
        self.pushButton_cancel_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_cancel_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cancel_2.setFont(font)
        self.pushButton_cancel_2.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:white;\n"
"    background-color:rgb(230, 162, 149);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_cancel_2.setObjectName("pushButton_cancel_2")
        self.horizontalLayout.addWidget(self.pushButton_cancel_2)
        self.stackedWidget.addWidget(self.page_treatment)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_main)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 50, 271, 581))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(265, 265))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.HongKong))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(False)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.pushButton_viewPatient = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_viewPatient.sizePolicy().hasHeightForWidth())
        self.pushButton_viewPatient.setSizePolicy(sizePolicy)
        self.pushButton_viewPatient.setMinimumSize(QtCore.QSize(265, 35))
        self.pushButton_viewPatient.setMaximumSize(QtCore.QSize(265, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_viewPatient.setFont(font)
        self.pushButton_viewPatient.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_viewPatient.setObjectName("pushButton_viewPatient")
        self.verticalLayout_3.addWidget(self.pushButton_viewPatient)
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(265, 35))
        self.pushButton_add.setMaximumSize(QtCore.QSize(265, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_ward = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ward.sizePolicy().hasHeightForWidth())
        self.pushButton_ward.setSizePolicy(sizePolicy)
        self.pushButton_ward.setMinimumSize(QtCore.QSize(265, 35))
        self.pushButton_ward.setMaximumSize(QtCore.QSize(265, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ward.setFont(font)
        self.pushButton_ward.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_ward.setObjectName("pushButton_ward")
        self.verticalLayout_3.addWidget(self.pushButton_ward)
        self.pushButton_myProfile = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_myProfile.sizePolicy().hasHeightForWidth())
        self.pushButton_myProfile.setSizePolicy(sizePolicy)
        self.pushButton_myProfile.setMinimumSize(QtCore.QSize(265, 35))
        self.pushButton_myProfile.setMaximumSize(QtCore.QSize(265, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_myProfile.setFont(font)
        self.pushButton_myProfile.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:black;\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(231, 215, 215);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_myProfile.setObjectName("pushButton_myProfile")
        self.verticalLayout_3.addWidget(self.pushButton_myProfile)
        self.pushButton_quit = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(265, 35))
        self.pushButton_quit.setMaximumSize(QtCore.QSize(265, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_quit.setFont(font)
        self.pushButton_quit.setStyleSheet("QPushButton\n"
"{\n"
"    font-family:Microsoft Yahei;\n"
"    font:20px;\n"
"    color:white;\n"
"    background-color:rgb(230, 162, 149);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(184, 67, 44);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.verticalLayout_3.addWidget(self.pushButton_quit)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 900, 750))
        self.listView.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(254, 234, 255, 255), stop:0.664773 rgba(155, 190, 235, 255), stop:1 rgba(245, 226, 223, 255))")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.frame_main.raise_()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ward No."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Age"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tel"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Medical History"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Allergy"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">You are now adding </p><p align=\"center\">a new patient!</p></body></html>"))
        self.label_8.setText(_translate("Form", "Name"))
        self.label_9.setText(_translate("Form", "  ID"))
        self.label_10.setText(_translate("Form", "Ward No."))
        self.label_12.setText(_translate("Form", "Nurse Name"))
        self.pushButton.setText(_translate("Form", "Comfirm"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ward No."))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Patient"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Patient ID"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nurse"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">If you want to modify the departmemt info, </span></p><p align=\"center\"><span style=\" font-weight:600;\">please contact the administrator</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Gender"))
        self.comboBox.setItemText(0, _translate("Form", "Male"))
        self.comboBox.setItemText(1, _translate("Form", "Female"))
        self.label_4.setText(_translate("Form", " Tel"))
        self.pushButton_confirm.setText(_translate("Form", "Confirm"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">You are now editting the </span></p><p><span style=\" font-size:10pt; font-weight:600;\">treatment information of:</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "Ward number"))
        self.pushButton_confirm_2.setText(_translate("Form", "Confirm"))
        self.pushButton_cancel_2.setText(_translate("Form", "Cancel"))
        self.pushButton_viewPatient.setText(_translate("Form", "Patient Info"))
        self.pushButton_add.setText(_translate("Form", "Add Patient"))
        self.pushButton_ward.setText(_translate("Form", "Ward Info"))
        self.pushButton_myProfile.setText(_translate("Form", "My Profile"))
        self.pushButton_quit.setText(_translate("Form", "Quit"))
