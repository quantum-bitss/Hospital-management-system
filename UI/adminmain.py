# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setGeometry(QtCore.QRect(10, 0, 781, 741))
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 20, 541, 741))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_checkDoc = QtWidgets.QWidget()
        self.page_checkDoc.setObjectName("page_checkDoc")
        self.frame_5 = QtWidgets.QFrame(self.page_checkDoc)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 521, 521))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 501, 71))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(1, 4, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(10, 90, 501, 421))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 481, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_checkDoc)
        self.page_patient = QtWidgets.QWidget()
        self.page_patient.setObjectName("page_patient")
        self.tableWidget_patient = QtWidgets.QTableWidget(self.page_patient)
        self.tableWidget_patient.setGeometry(QtCore.QRect(10, 60, 521, 521))
        self.tableWidget_patient.setObjectName("tableWidget_patient")
        self.tableWidget_patient.setColumnCount(5)
        self.tableWidget_patient.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patient.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patient.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patient.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patient.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_patient.setHorizontalHeaderItem(4, item)
        self.tableWidget_patient.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_patient.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_patient)
        self.page_doctor = QtWidgets.QWidget()
        self.page_doctor.setObjectName("page_doctor")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_doctor)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 80, 521, 521))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_doctor)
        self.page_doctorModify = QtWidgets.QWidget()
        self.page_doctorModify.setObjectName("page_doctorModify")
        self.frame = QtWidgets.QFrame(self.page_doctorModify)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 501, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 521, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 100, 501, 411))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 50, 521, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(350, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(350, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(350, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(350, 30))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(350, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(350, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(350, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(350, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(350, 30))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(350, 30))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(170, -10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_confirm = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_confirm.setGeometry(QtCore.QRect(20, 350, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm.setSizePolicy(sizePolicy)
        self.pushButton_confirm.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_confirm.setMaximumSize(QtCore.QSize(200, 50))
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
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(0, 255, 255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 350, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(200, 50))
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
        self.stackedWidget.addWidget(self.page_doctorModify)
        self.page_patientModify = QtWidgets.QWidget()
        self.page_patientModify.setObjectName("page_patientModify")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_patientModify)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 541, 632))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(300, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(300, 100))
        self.textEdit_2.setMaximumSize(QtCore.QSize(300, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(300, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.pushButton_cancel_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel_2.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel_2.setSizePolicy(sizePolicy)
        self.pushButton_cancel_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_cancel_2.setMaximumSize(QtCore.QSize(200, 50))
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
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.pushButton_cancel_2)
        self.pushButton_confirm_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_confirm_2.sizePolicy().hasHeightForWidth())
        self.pushButton_confirm_2.setSizePolicy(sizePolicy)
        self.pushButton_confirm_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_confirm_2.setMaximumSize(QtCore.QSize(200, 50))
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
"    background-color:rgb(0, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(0, 255, 255);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.pushButton_confirm_2.setObjectName("pushButton_confirm_2")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pushButton_confirm_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_patientModify)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_18 = QtWidgets.QLabel(self.page_patientModify)
        self.label_18.setGeometry(QtCore.QRect(20, -10, 521, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_patientModify)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 202, 663))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_checkDoc = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_checkDoc.sizePolicy().hasHeightForWidth())
        self.pushButton_checkDoc.setSizePolicy(sizePolicy)
        self.pushButton_checkDoc.setMinimumSize(QtCore.QSize(190, 60))
        self.pushButton_checkDoc.setMaximumSize(QtCore.QSize(190, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_checkDoc.setFont(font)
        self.pushButton_checkDoc.setStyleSheet("QPushButton\n"
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
"}\n"
"")
        self.pushButton_checkDoc.setObjectName("pushButton_checkDoc")
        self.verticalLayout.addWidget(self.pushButton_checkDoc)
        self.pushButton_viewPatient = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_viewPatient.sizePolicy().hasHeightForWidth())
        self.pushButton_viewPatient.setSizePolicy(sizePolicy)
        self.pushButton_viewPatient.setMinimumSize(QtCore.QSize(190, 60))
        self.pushButton_viewPatient.setMaximumSize(QtCore.QSize(190, 60))
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
"}\n"
"")
        self.pushButton_viewPatient.setObjectName("pushButton_viewPatient")
        self.verticalLayout.addWidget(self.pushButton_viewPatient)
        self.pushButton_viewDoc = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_viewDoc.sizePolicy().hasHeightForWidth())
        self.pushButton_viewDoc.setSizePolicy(sizePolicy)
        self.pushButton_viewDoc.setMinimumSize(QtCore.QSize(190, 60))
        self.pushButton_viewDoc.setMaximumSize(QtCore.QSize(190, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_viewDoc.setFont(font)
        self.pushButton_viewDoc.setStyleSheet("QPushButton\n"
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
"}\n"
"")
        self.pushButton_viewDoc.setObjectName("pushButton_viewDoc")
        self.verticalLayout.addWidget(self.pushButton_viewDoc)
        self.pushButton_quit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(190, 60))
        self.pushButton_quit.setMaximumSize(QtCore.QSize(190, 60))
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
        self.verticalLayout.addWidget(self.pushButton_quit)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.listView.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(254, 234, 255, 255), stop:0.664773 rgba(155, 190, 235, 255), stop:1 rgba(245, 226, 223, 255))")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.frame_main.raise_()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please check the following information"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Doc. ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tel"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Department"))
        item = self.tableWidget_patient.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget_patient.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget_patient.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_patient.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tel"))
        item = self.tableWidget_patient.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Age"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tel"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Departmemt"))
        self.label_7.setText(_translate("Form", "You are modifying information of:"))
        self.label_3.setText(_translate("Form", "Name"))
        self.label_4.setText(_translate("Form", "Gender"))
        self.comboBox.setItemText(0, _translate("Form", "Male"))
        self.comboBox.setItemText(1, _translate("Form", "Female"))
        self.label_15.setText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Tel"))
        self.label_6.setText(_translate("Form", "Department"))
        self.comboBox_2.setItemText(0, _translate("Form", "Casualty Department"))
        self.comboBox_2.setItemText(1, _translate("Form", "Operating Theatre"))
        self.comboBox_2.setItemText(2, _translate("Form", "Intensive Care Unit"))
        self.comboBox_2.setItemText(3, _translate("Form", "Anesthesiology Department"))
        self.comboBox_2.setItemText(4, _translate("Form", "Cardiology Department"))
        self.comboBox_2.setItemText(5, _translate("Form", "ENT Department"))
        self.comboBox_2.setItemText(6, _translate("Form", "Geriatric Department"))
        self.comboBox_2.setItemText(7, _translate("Form", "Gastroenterology Department"))
        self.label_16.setText(_translate("Form", "Infor_review"))
        self.pushButton_confirm.setText(_translate("Form", "Confirm"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.label_8.setText(_translate("Form", "Name"))
        self.label_9.setText(_translate("Form", "Gender"))
        self.comboBox_3.setItemText(0, _translate("Form", "Male"))
        self.comboBox_3.setItemText(1, _translate("Form", "Female"))
        self.label_17.setText(_translate("Form", "Password"))
        self.label_10.setText(_translate("Form", "Tel"))
        self.label_12.setText(_translate("Form", "Age"))
        self.label_11.setText(_translate("Form", "Medical History"))
        self.label_13.setText(_translate("Form", "Allergy"))
        self.label_14.setText(_translate("Form", "Ward No."))
        self.pushButton_cancel_2.setText(_translate("Form", "Cancel"))
        self.pushButton_confirm_2.setText(_translate("Form", "Confirm"))
        self.label_18.setText(_translate("Form", "You are modifying information of:"))
        self.pushButton_checkDoc.setText(_translate("Form", "Check Doc. Info"))
        self.pushButton_viewPatient.setText(_translate("Form", "View Patient Info"))
        self.pushButton_viewDoc.setText(_translate("Form", "View Doctor Info"))
        self.pushButton_quit.setText(_translate("Form", "Quit"))
