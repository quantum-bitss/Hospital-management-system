from UI.admin import Ui_Form as adminui
from UI.login import Ui_MainWindow as loginui
from UI.doctor import Ui_Form as doctorui
from UI.patient import Ui_Form as patientui
from UI.adminmain import Ui_Form as adminmainui
from UI.doctorlog import Ui_Form as doctorlogui
from UI.patientlog import Ui_Form as patientlogui
from UI.doctormain import Ui_Form as doctormainui
from UI.patientmain import Ui_Form as patientmainui
from PyQt5 import QtWidgets
import tkinter
from tkinter import messagebox
import sys
from DataBase import DataBase


root = tkinter.Tk()
root.withdraw()
db = DataBase()
id_reassign = False  # 标志是否是逻辑删账号的ID
login_id = 0  # 记录目前账号的id
modifying_id = 0  # 正在修改的账号的id
last_widget_idx = 0  # 上一堆叠窗口的idx


class Login(QtWidgets.QMainWindow, loginui):  # 登录界面
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)


class Admin(QtWidgets.QWidget, adminui):  # 管理员登录界面
    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)


class Doctor(QtWidgets.QWidget, doctorui):  # 医生登录界面
    def __init__(self):
        super(Doctor, self).__init__()
        self.setupUi(self)


class Patient(QtWidgets.QWidget, patientui):  # 病人登录界面
    def __init__(self):
        super(Patient, self).__init__()
        self.setupUi(self)


class AdminMain(QtWidgets.QWidget, adminmainui):  # 管理员主界面
    def __init__(self):
        super(AdminMain, self).__init__()
        self.setupUi(self)


class DoctorMain(QtWidgets.QWidget, doctormainui):  # 医生主界面
    def __init__(self):
        super(DoctorMain, self).__init__()
        self.setupUi(self)


class PatientMain(QtWidgets.QWidget, patientmainui):  # 病人主界面
    def __init__(self):
        super(PatientMain, self).__init__()
        self.setupUi(self)


class DoctorLogin(QtWidgets.QWidget, doctorlogui):
    def __init__(self):
        super(DoctorLogin, self).__init__()
        self.setupUi(self)


class PatientLogin(QtWidgets.QWidget, patientlogui):
    def __init__(self):
        super(PatientLogin, self).__init__()
        self.setupUi(self)


def patient_entrance():
    login.close()
    patientlogin.lineEdit.setText('')
    patientlogin.lineEdit_2.setText('')
    patientlogin.show()


def doctor_entrance():
    login.close()
    doctorlogin.lineEdit.setText('')
    doctorlogin.lineEdit_2.setText('')
    doctorlogin.show()


def admin_entrance():
    login.close()
    admin.lineEdit.setText('')
    admin.show()


def doctor_register():
    id_assignment(0)
    doctor.lineEdit_2.setText('')
    doctor.lineEdit_3.setText('')
    doctor.comboBox.setCurrentIndex(0)
    doctor.lineEdit_5.setText('')
    doctor.comboBox_2.setCurrentIndex(0)
    doctorlogin.close()
    doctor.show()


def patient_register():
    id_assignment(1)
    patient.lineEdit_2.setText('')
    patient.lineEdit_3.setText('')
    patient.comboBox.setCurrentIndex(0)
    patient.lineEdit_4.setText('')
    patient.lineEdit_5.setText('')
    patient.lineEdit_6.setText('')
    patient.lineEdit_7.setText('')
    patientlogin.close()
    patient.show()


# usertype为0表示医生，1表示病人，2表示管理员，医生的登录需要管理员先审核通过，审核不通过则弹窗提醒
def userLogin(username, usertype, password, widget, nextWidget):
    global login_id
    if usertype == 2:  # 超管没有username，只需检测password
        if password == '123':  # 密码正确
            widget.close()
            nextWidget.show()  # 附加初始界面信息展示
            admin_show_doctor_to_check()
        else:
            messagebox.showerror(title='Error', message='Wrong Password')
    else:
        if len(username) == 0 or len(password) == 0:  # 先检测账户为空和密码为空的错误
            messagebox.showerror(title='Error', message='Password is empty.')
        else:
            sql = ''
            if usertype == 0:  # 医生
                sql = "select * from Doctor where ID = %s and Del = %s" % (username, '0')  # 非逻辑删账户
            elif usertype == 1:  # 病人
                sql = "select * from Patient where ID = %s and Del = %s" % (username, '0')
            results = db.connect_to_fatch(sql)  # 返回二维列表
            if len(results) == 0:
                messagebox.showerror(title='Error', message='No such username.')
            else:  # 账户存在，检查密码
                if usertype == 0 and results[0][7] == 0:  # Infor_review为0表示未审核
                    messagebox.showinfo(title='Information', message='Please wait for qualification.')
                elif password == results[0][3]:  # 等于第四项，即Password属性的值
                    login_id = username  # 登录成功，记录当前账户ID
                    if usertype == 0:
                        doctor_show_patient_info()
                    else:
                        patient_show_treatment()
                    messagebox.showinfo(title='Information', message='Welcome!')
                    widget.close()
                    nextWidget.show()  # 附加初始界面信息展示
                else:
                    messagebox.showerror(title='Error', message='Wrong password!')


def doctor_register_confirm():  # 医生注册界面信息，UI界面的ID框需要删除
    global id_reassign
    username, password = doctor.lineEdit.text(), doctor.lineEdit_2.text()
    name, gender = doctor.lineEdit_3.text(), doctor.comboBox.currentText()
    tel, department = doctor.lineEdit_5.text(), doctor.comboBox_2.currentText()
    widget, next_widget = doctor, login
    if len(password) == 0:
        messagebox.showerror(title='Error', message='Password is empty.')
    else:
        new = {'name': name, 'sex': gender, 'id': username, 'password': password,
               'del': '0', 'telephone_num': tel, 'department': department, 'infor_review': '0'}  # 0表示未审核通过，先写为1方便测试
        # 进行有效性检测，防止插入失败
        if tel.isdigit():
            if id_reassign:  # 是逻辑删账号ID重分配
                db.delete_doctor({'id': username, 'del': '1'})  # 先删除掉该逻辑删账号
            db.insert_doctor(new)  # 插入新项
            messagebox.showinfo(title='Information',
                                message='Successfully registered! '
                                        'Your information is being verified by the administrator.')
            widget.close()
            next_widget.show()
        else:
            messagebox.showerror(title='Error', message='Invalid information!')


def patient_register_confirm():
    username, password = patient.lineEdit.text(), patient.lineEdit_2.text()
    name, gender = patient.lineEdit_3.text(), patient.comboBox.currentText()
    tel, age = patient.lineEdit_4.text(), patient.lineEdit_5.text()
    medical_history, allergy = patient.lineEdit_6.text(), patient.lineEdit_7.text()
    widget, next_widget = patient, patientlogin
    if len(password) == 0:
        messagebox.showerror(title='Error', message='Password is empty.')
    else:
        new = {'name': name, 'sex': gender, 'id': username, 'password': password,
               'del': '0', 'telephone_num': tel, 'age': age, 'ward_num': -1,
               'medical_records': medical_history, 'allergy': allergy}  # 病房号为数字-1表示还没分配病房，后续由医生或管理员分配
        if tel.isdigit() and age.isdigit():
            if id_reassign:
                db.delete_patient({'id': username, 'del': '1'})
            db.insert_patient(new)
            messagebox.showinfo(title='Information',
                                message='Successfully registered!')
            widget.close()
            next_widget.show()
        else:
            messagebox.showerror(title='Error', message='Invalid information!')


def id_assignment(usertype):  # 逻辑删Del属性，若有逻辑删账号，则分配给新用户，没有则计数分配，保证了账号数不会减少，避免了重复ID
    global id_reassign
    if usertype == 0:  # 医生
        sql = "select ID from Doctor where Del = 1"  # 查找逻辑删账号ID
        result = db.connect_to_fatch(sql)
        if len(result) != 0:
            doctor.lineEdit.setText(result[0][2])  # 第三列是ID，也就是Username
            doctor.lineEdit.setEnabled(False)
            id_reassign = True
        else:  # 没有逻辑删账户，计数然后分配新ID
            sql = "select count(ID) from Doctor"  # doctor计数
            result = db.connect_to_fatch(sql)[0][0]  # 二维
            id = str(result)
            zeros = '000000'  # 7位ID
            while result // 10 > 0:
                result //= 10
                zeros = zeros[:-2]  # 每次减一位零
            doctor.lineEdit.setText('%s' % (zeros + id))
            doctor.lineEdit.setEnabled(False)  # 禁止编辑
            id_reassign = False
    elif usertype == 1:  # 病人
        sql = "select ID from Patient where Del = 1"
        result = db.connect_to_fatch(sql)
        if len(result) != 0:  # 有逻辑删账户
            patient.lineEdit.setText(result[0][2])
            patient.lineEdit.setEnabled(False)
            id_reassign = True
        else:
            sql = "select count(ID) from Patient"  # 病人计数
            result = db.connect_to_fatch(sql)[0][0]  # 二维
            id = str(result)
            zeros = '000000000'  # 10位ID
            while result // 10 > 0:
                result //= 10
                zeros = zeros[:-2]  # 每次减一位零
            patient.lineEdit.setText('%s' % (zeros + id))
            patient.lineEdit.setEnabled(False)  # 禁止编辑
            id_reassign = False


# 病人各界面的跳转函数
def patient_show_treatment():
    # 用patient_id查询信息
    global login_id
    key1 = {'name': -1, 'sex': -1, 'id': login_id, 'password': -1, 'del': '0',
            'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}
    key2 = {'patient_id': login_id, 'doctor_id': -1, 'treatment': -1}
    result1 = db.search_patient(key1)[0]
    patientmain.lineEdit_name.setText(result1[0])  # name
    patientmain.lineEdit_ward.setText(str(result1[7]))  # ward_num
    result2 = db.search_treat(key2)
    if len(result2) != 0:  # 医生可能还没分配
        patientmain.textEdit_2.setText(result2[0][2])  # treatment

        doctor_id = result2[0][1]
        key3 = {'name': -1, 'sex': -1, 'id': doctor_id, 'password': -1, 'del': '0',
                'telephone_num': -1, 'department': -1, 'infor_review': -1}
        result3 = db.search_doctor(key3)[0]
        patientmain.lineEdit_doctorname.setText(result3[0])  # doctor name
    patientmain.lineEdit_name.setEnabled(False)  # 不可修改
    patientmain.lineEdit_ward.setEnabled(False)
    patientmain.textEdit_2.setEnabled(False)
    patientmain.lineEdit_doctorname.setEnabled(False)
    patientmain.stackedWidget_2.setCurrentIndex(0)


def patient_show_personal_info():
    key = {'name': -1, 'sex': -1, 'id': login_id, 'password': -1, 'del': '0',
           'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}
    result = db.search_patient(key)[0]
    patientmain.lineEdit.setText(result[0])  # name
    if result[1] == 'Male':  # gender
        patientmain.comboBox.setCurrentIndex(0)
    else:
        patientmain.comboBox.setCurrentIndex(1)
    patientmain.lineEdit_2.setText(str(result[5]))  # telephone number
    patientmain.lineEdit_3.setText(str(result[6]))  # age
    patientmain.textEdit_medicalHistory.setText(result[8])  # medical records
    patientmain.textEdit_allergy.setText(result[9])  # allergy
    patientmain.stackedWidget_2.setCurrentIndex(1)


# 按钮函数
def patient_edit_personal_info_confirm():
    name = patientmain.lineEdit.text()  # name
    gender = patientmain.comboBox.currentText()
    tel = patientmain.lineEdit_2.text()  # telephone number
    age = patientmain.lineEdit_3.text()  # age
    medical_records = patientmain.textEdit_medicalHistory.toPlainText()  # medical records
    allergy = patientmain.textEdit_allergy.toPlainText()  # allergy
    # Patient和Ward表都有Patient_name和Ward_num的可变属性，若Ward中有此项则需要同步修改
    key1 = {'name': name, 'sex': gender, 'id': login_id, 'password': -1, 'del': '0',
            'telephone_num': tel, 'age': age, 'ward_num': -1, 'medical_records': medical_records, 'allergy': allergy}
    db.modify_patient(key1)
    key2 = {'ward_num': -1, 'patient_name': -1, 'patient_id': login_id, 'nurse_name': -1}  # 现查是否有此项
    ward_and_patient = db.search_ward(key2)
    if len(ward_and_patient) != 0:  # 没有就不修改
        key2['patient_name'] = name
        db.modify_ward(key2)
    messagebox.showinfo(title='Infomation', message='Succeed.')


# 医生各界面的跳转函数
def doctor_show_patient_info():  # 绑定到patient_info，doctormain.pushButton_viewPatient
    global login_id
    doctormain.tableWidget.setRowCount(0)  # 清空所有行
    patient_table = db.search_treat({'patient_id': -1, 'doctor_id': login_id, 'treatment': -1})  # 二维列表
    for i in range(len(patient_table)):
        patient_id = patient_table[i][0]  # 提取ID，再找出这些病人的信息
        key = {'name': -1, 'sex': -1, 'id': patient_id, 'password': -1, 'del': '0',
               'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}
        result = db.search_patient(key)[0]
        row_count = doctormain.tableWidget.rowCount()
        doctormain.tableWidget.insertRow(row_count)
        for j in range(0, 3):  # 前三列与表的前三列对应
            doctormain.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[j])))
        doctormain.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[7])))  # ward_num
        doctormain.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[6])))  # age
        doctormain.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(result[5])))  # tel
        doctormain.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(str(result[8])))  # medical history
        doctormain.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(result[9])))  # allergy
    doctormain.stackedWidget.setCurrentIndex(0)


def doctor_show_ward_info():  # 绑定到ward_info，doctormain.pushButton_ward
    doctormain.tableWidget_2.setRowCount(0)  # 清空所有行
    patient_table = db.search_treat({'patient_id': -1, 'doctor_id': login_id, 'treatment': -1})  # 二维列表
    for i in range(len(patient_table)):
        patient_id = patient_table[i][0]  # 提取ID，再找出这些病人的信息，且按ward_num的顺序进行展示
        key = {'ward_num': -1, 'patient_name': -1, 'patient_id': patient_id, 'nurse_name': -1}
        result = db.search_ward(key)[0]  # 二维列表
        row_count = doctormain.tableWidget_2.rowCount()
        doctormain.tableWidget_2.insertRow(row_count)
        for j in range(0, len(result)):
            doctormain.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[j])))  # 跳过password和del属性
    doctormain.stackedWidget.setCurrentIndex(2)


def doctor_show_personal_info():
    key = {'name': -1, 'sex': -1, 'id': login_id, 'password': -1, 'del': '0',
           'telephone_num': -1, 'department': -1, 'infor_review': -1}
    result = db.search_doctor(key)[0]
    # 展示当前值
    doctormain.lineEdit.setText(result[0])
    if result[1] == 'Male':
        doctormain.comboBox.setCurrentIndex(0)
    else:
        doctormain.comboBox.setCurrentIndex(1)
    doctormain.lineEdit_2.setText(str(result[5]))
    doctormain.stackedWidget.setCurrentIndex(3)


def doctor_add_patient():
    doctormain.lineEdit_4.setText('')
    doctormain.lineEdit_4.setEnabled(True)
    doctormain.lineEdit_5.setText('')
    doctormain.lineEdit_5.setEnabled(True)
    doctormain.lineEdit_6.setText('')
    doctormain.lineEdit_7.setText('')
    doctormain.stackedWidget.setCurrentIndex(1)


def doctor_edit_treatment(clicked_item):  # 响应双击事件，获得双击表项的数据
    items = [doctormain.tableWidget.item(clicked_item.row(), i).text() for i in range(8)]  # 获取该病人的数据，8个可见属性值
    doctormain.lineEdit_patient.setText(items[0])  # 名字
    doctormain.lineEdit_patient.setEnabled(False)  # 不能编辑
    doctormain.textEdit.setText(db.search_treat({'patient_id': items[2], 'doctor_id': login_id, 'treatment': -1})[0][2])  # 查找自己负责的病人的治疗方案
    doctormain.lineEdit_3.setText(items[5])  # 病人的病房号
    doctormain.lineEdit_3.setEnabled(False)  # 不能编辑
    doctormain.stackedWidget.setCurrentIndex(4)  # 跳转到编辑治疗方案界面


# 按钮函数
def doctor_add_patient_confirm():  # 绑定到add patient，doctormain.pushButton_add
    name, id, ward_num = doctormain.lineEdit_4.text(), doctormain.lineEdit_5.text(), doctormain.lineEdit_6.text()
    nurse_name = doctormain.lineEdit_7.text()
    if len(name) == 0 or len(id) == 0 or len(ward_num) == 0:
        messagebox.showerror(title='Error', message='Empty inputs!')
    else:
        # 修改ward_num需要重复检测
        key1 = {'name': name, 'sex': -1, 'id': id, 'password': -1, 'del': '0',
                'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}
        key2 = {'ward_num': ward_num, 'patient_name': -1, 'patient_id': -1, 'nurse_name': -1}  # 查找该ward号码是否重复
        patients = db.search_patient(key1)  # 用ID查询未逻辑删的账户，比对名字是否正确，正确则修改ward_num，错误则弹窗提醒
        ward_and_patient = db.search_ward(key2)
        if len(patients) == 0:  # 没有该有效账户
            messagebox.showerror(title='Error', message='Invalid inputs, please check id or name again!')
        elif len(ward_and_patient) != 0 and str(ward_and_patient[0][2]) != id:  # 已有该ward号码且不为当前病人的记录
            messagebox.showerror(title='Error', message='Ward number repeats!')
        else:  # 该账户存在且输入的ward_num未与其他账户的ward_num重复
            key3 = {'name': name, 'sex': -1, 'id': id, 'password': -1, 'del': -1,
                    'telephone_num': -1, 'age': -1, 'ward_num': ward_num, 'medical_records': -1, 'allergy': -1}
            key4 = {'ward_num': ward_num, 'patient_name': name, 'patient_id': id, 'nurse_name': nurse_name}
            # 若病人之前没有ward_num，则修改Patient中的ward_num和添加到Ward中，否则修改Patient和Ward中的ward_num
            # 添加到Treat中
            db.modify_patient(key3)
            db.insert_treat({'patient_id': id, 'doctor_id': login_id, 'treatment': -1})
            if patients[0][7] != None:  # 病人有病房号
                sql = "update Ward set Ward_num = %s, Patient_Name = '%s', Nurse_Name = '%s' " \
                      "where Patient_ID = %s" % (ward_num, name, nurse_name, id)
                db.connect_to_update(sql)  # 修改ward_num
            else:
                db.insert_ward(key4)
            messagebox.showinfo(title='Information', message='Succeed.')


def doctor_edit_treatment_confirm():
    ward_num = doctormain.lineEdit_3.text()  # 用病房号查询病人ID，再用病人ID更新Treat
    result = db.search_ward({'ward_num': ward_num, 'patient_name': -1, 'patient_id': -1, 'nurse_name': -1})[0]
    patient_id = result[2]
    db.modify_treat({'patient_id': patient_id, 'doctor_id': login_id, 'treatment': doctormain.textEdit.toPlainText()})
    messagebox.showinfo(title='Information', message='Succeed.')


def doctor_edit_ward_and_nurse(clicked_item):
    global last_widget_idx
    last_widget_idx = doctormain.stackedWidget.currentIndex()
    items = [doctormain.tableWidget_2.item(clicked_item.row(), i).text() for i in range(4)]  # 4列
    doctormain.lineEdit_4.setText(items[1])  # name
    doctormain.lineEdit_4.setEnabled(False)  # 不能修改病人name
    doctormain.lineEdit_5.setText(items[2])  # id
    doctormain.lineEdit_5.setEnabled(False)  # 不能修改病人id
    doctormain.lineEdit_6.setText(items[0])  # ward_num
    doctormain.lineEdit_7.setText(items[3])  # nurse name
    doctormain.stackedWidget.setCurrentIndex(1)  # 跳转到add patient界面


def doctor_edit_personal_information_confirm():
    name, gender, tel = doctormain.lineEdit.text(), doctormain.comboBox.currentText(), doctormain.lineEdit_2.text()
    if len(name) == 0 or len(gender) == 0 or len(tel) == 0:
        messagebox.showerror(title='Error', message='Empty inputs!')
    else:
        key = {'name': name, 'sex': gender, 'id': login_id, 'password': -1, 'del': '0',
               'telephone_num': tel, 'department': -1, 'infor_review': -1}
        db.modify_doctor(key)  # 修改name，sex和telephone number
        messagebox.showinfo(title='Information', message='Succeed.')


# 管理员的跳转界面
def admin_show_doctor_to_check():  # 展示需要审核的医生信息
    adminmain.tableWidget.setRowCount(0)  # 清空所有行
    key = {'name': -1, 'sex': -1, 'id': -1, 'password': -1, 'del': '0',
           'telephone_num': -1, 'department': -1, 'infor_review': '0'}  # 查找未审核的医生账号
    result = db.search_doctor(key)
    for i in range(len(result)):
        row_count = adminmain.tableWidget.rowCount()
        adminmain.tableWidget.insertRow(row_count)
        adminmain.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][2])))  # doctor_id
        adminmain.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][0])))  # name
        adminmain.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][1])))  # sex
        adminmain.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][5])))  # telephone
        adminmain.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][6])))  # department
    adminmain.stackedWidget.setCurrentIndex(0)


def admin_show_patient_info():  # 展示病人的信息
    adminmain.tableWidget_patient.setRowCount(0)  # 清空所有行
    result = db.show_patient()  # 展示所有病人
    for i in range(len(result)):
        row_count = adminmain.tableWidget_patient.rowCount()
        adminmain.tableWidget_patient.insertRow(row_count)
        adminmain.tableWidget_patient.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))  # name
        adminmain.tableWidget_patient.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))  # sex
        adminmain.tableWidget_patient.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))  # id
        adminmain.tableWidget_patient.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][5])))  # telephone
        adminmain.tableWidget_patient.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][6])))  # age
    adminmain.stackedWidget.setCurrentIndex(1)


def admin_show_doctor_info():  # 展示已审核的医生信息
    adminmain.tableWidget_2.setRowCount(0)  # 清空所有行
    key = {'name': -1, 'sex': -1, 'id': -1, 'password': -1, 'del': '0',
           'telephone_num': -1, 'department': -1, 'infor_review': '1'}  # 查找已审核的医生账号
    result = db.search_doctor(key)
    for i in range(len(result)):
        row_count = adminmain.tableWidget_2.rowCount()
        adminmain.tableWidget_2.insertRow(row_count)
        adminmain.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))  # doctor_id
        adminmain.tableWidget_2.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))  # name
        adminmain.tableWidget_2.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))  # sex
        adminmain.tableWidget_2.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][5])))  # telephone
        adminmain.tableWidget_2.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][6])))  # department
    adminmain.stackedWidget.setCurrentIndex(2)


def admin_edit_doctor_info(clicked_item):
    global modifying_id, last_widget_idx
    if adminmain.stackedWidget.currentIndex() == 0:  # 第一个界面
        doctor_id = adminmain.tableWidget.item(clicked_item.row(), 0).text()  # 获取该医生的id
    else:
        doctor_id = adminmain.tableWidget_2.item(clicked_item.row(), 2).text()
    modifying_id = doctor_id  # 记录当前修改的医生的id
    last_widget_idx = adminmain.stackedWidget.currentIndex()  # 记录cancel后返回的窗口索引
    key = {'name': -1, 'sex': -1, 'id': doctor_id, 'password': -1, 'del': '0',
           'telephone_num': -1, 'department': -1, 'infor_review': -1}  # 用ID查找该医生账号
    result = db.search_doctor(key)[0]
    adminmain.stackedWidget.setCurrentIndex(3)  # 跳转到编辑医生信息方案界面
    adminmain.lineEdit.setText(result[0])  # name
    adminmain.lineEdit_2.setText(result[0])  # name
    if result[1] == 'Male':  # sex
        adminmain.comboBox.setCurrentIndex(0)
    else:
        adminmain.comboBox.setCurrentIndex(1)
    adminmain.lineEdit_9.setText(result[3])  # password
    adminmain.lineEdit_3.setText(str(result[5]))  # telephone
    for i in range(adminmain.comboBox_2.count()):  # 遍历寻找正确的department
        if adminmain.comboBox_2.itemText(i) == result[6]:
            adminmain.comboBox_2.setCurrentIndex(i)
    adminmain.lineEdit_10.setText(str(result[7]))  # infor_review


def admin_edit_patient_info(clicked_item):
    global modifying_id, last_widget_idx
    patient_id = adminmain.tableWidget_patient.item(clicked_item.row(), 2).text()  # 获取该病人id
    modifying_id = patient_id
    last_widget_idx = adminmain.stackedWidget.currentIndex()
    key = {'name': -1, 'sex': -1, 'id': patient_id, 'password': -1, 'del': '0',
           'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}
    result = db.search_patient(key)[0]
    adminmain.lineEdit_4.setText(result[0])  # name
    adminmain.lineEdit_5.setText(result[0])  # name
    if result[1] == 'Male':  # sex
        adminmain.comboBox_3.setCurrentIndex(0)
    else:
        adminmain.comboBox_3.setCurrentIndex(1)
    adminmain.lineEdit_12.setText(result[3])  # password
    adminmain.lineEdit_6.setText(str(result[5]))  # telephone
    adminmain.lineEdit_7.setText(str(result[6]))  # age
    if result[7] != None:
        adminmain.lineEdit_8.setText(str(result[7]))  # ward_num  后端数据为空是None，影响空输入判断以及后端函数sql异常！
    else:
        adminmain.lineEdit_8.setText('')  # 没有ward_num就设为空
    adminmain.textEdit.setText(result[8])  # medical_records
    adminmain.textEdit_2.setText(result[9])  # allergy
    adminmain.stackedWidget.setCurrentIndex(4)


# 按钮函数
def admin_edit_doctor_info_confirm():  # 编辑医生的信息
    name, sex, password = adminmain.lineEdit_2.text(), adminmain.comboBox.currentText(), adminmain.lineEdit_9.text()
    tel, department = adminmain.lineEdit_3.text(), adminmain.comboBox_2.currentText()
    infor_review = adminmain.lineEdit_10.text()
    key = {'name': name, 'sex': sex, 'id': modifying_id, 'password': password, 'del': '0',
           'telephone_num': tel, 'department': department, 'infor_review': infor_review}  # 用ID查找该医生账号
    db.modify_doctor(key)
    messagebox.showinfo(title='Information', message='Succeed.')


def admin_edit_patient_info_confirm():
    name, gender, tel = adminmain.lineEdit_5.text(), adminmain.comboBox_3.currentText(), adminmain.lineEdit_6.text()
    age, medical_records = adminmain.lineEdit_7.text(), adminmain.textEdit.toPlainText()
    password, allergy = adminmain.lineEdit_12.text(), adminmain.textEdit_2.toPlainText()
    ward_num = adminmain.lineEdit_8.text()
    if len(ward_num) != 0:  # 有ward_num输入
        # 修改病房号需要注意是否重复，防止程序崩溃
        key = {'ward_num': ward_num, 'patient_name': -1, 'patient_id': -1, 'nurse_name': -1}  # 查询ward_num是否可用
        result = db.search_ward(key)
        # 允许赋同样的值，则需要判断result是否是该病人的Ward记录
        if len(result) != 0 and str(result[0][2]) != modifying_id:  # 结果不可空且不是当前病人的ward表项
            print(str(result[0][2]), modifying_id)
            messagebox.showerror(title='Error', message='Ward number repeats!')
        else:
            # 病人的ward_num修改时Patient表中的ward_num要修改，若Ward无此项则添加，有此项则修改
            key1 = {'name': name, 'sex': gender, 'id': modifying_id, 'password': password, 'del': '0',
                    'telephone_num': tel, 'age': age, 'ward_num': ward_num, 'medical_records': medical_records,
                    'allergy': allergy}
            key2 = {'ward_num': -1, 'patient_name': -1, 'patient_id': modifying_id, 'nurse_name': -1}
            key3 = {'ward_num': ward_num, 'patient_name': name, 'patient_id': modifying_id, 'nurse_name': -1}
            db.modify_patient(key1)
            ward_and_patient = db.search_ward(key2)
            if len(ward_and_patient) != 0:  # 有此项
                sql = "update Ward set Ward_num = %s, Patient_Name = '%s' " \
                      "where Patient_ID = %s" % (ward_num, name, modifying_id)
                db.connect_to_update(sql)  # 修改该病人在Ward中的ward_num和name
                print(1)
            else:
                db.insert_ward(key3)
            messagebox.showinfo(title='Information', message='Succeed.')
    else:  # 没有ward_num，认为是一开始就没有ward_num而不是把ward_num删除，则不需要管Ward
        key1 = {'name': name, 'sex': gender, 'id': modifying_id, 'password': password, 'del': '0',
                'telephone_num': tel, 'age': age, 'ward_num': -1, 'medical_records': medical_records,
                'allergy': allergy}  # 不修改ward_num
        db.modify_patient(key1)
        messagebox.showinfo(title='Information', message='Succeed.')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # Initialize the widgets
    login = Login()
    login.show()
    admin = Admin()
    doctor = Doctor()
    patient = Patient()
    adminmain = AdminMain()
    doctormain = DoctorMain()
    patientmain = PatientMain()
    doctorlogin = DoctorLogin()
    patientlogin = PatientLogin()

    # Connecting buttons in login
    login.pushButton.clicked.connect(lambda: {patient_entrance()})
    login.pushButton_2.clicked.connect(lambda: {doctor_entrance()})
    login.pushButton_3.clicked.connect(lambda: {admin_entrance()})

    # Connecting buttons in admin_login
    admin.pushButton.clicked.connect(
        lambda: {userLogin('', 2, admin.lineEdit.text(), admin, adminmain)})  # 超管登录确认，不需要username
    admin.pushButton_2.clicked.connect(lambda: {admin.close(), login.show()})  # 超管登录取消

    # Connecting buttons in doctor_login(医生登录)
    doctorlogin.pushButton.clicked.connect(
        lambda: userLogin(doctorlogin.lineEdit.text(), 0, doctorlogin.lineEdit_2.text(), doctorlogin, doctormain))  # 医生登录确认
    doctorlogin.pushButton_2.clicked.connect(lambda: {doctorlogin.close(), login.show()})  # 医生登录取消
    doctorlogin.pushButton_3.clicked.connect(lambda: {doctor_register()})  # 医生登录注册
    # Connecting buttons in doctor(医生注册)
    doctor.pushButton_2.clicked.connect(lambda: {doctor.close(), doctorlogin.show()})  # 医生注册取消
    doctor.pushButton.clicked.connect(
        lambda: doctor_register_confirm())  # 医生注册确认

    # Connecting buttons in patient_login(病人登录)
    patientlogin.pushButton.clicked.connect(
        lambda: userLogin(patientlogin.lineEdit.text(), 1, patientlogin.lineEdit_2.text(), patientlogin, patientmain))  # 病人登录确认
    patientlogin.pushButton_2.clicked.connect(lambda: {patientlogin.close(), login.show()})  # 病人登录取消
    patientlogin.pushButton_3.clicked.connect(lambda: {patient_register()})  # 病人登录注册
    # Connecting buttons in patient(病人注册)
    patient.pushButton_2.clicked.connect(lambda: {patient.close(), patientlogin.show()})  # 病人注册取消
    patient.pushButton.clicked.connect(lambda: patient_register_confirm())  # 病人注册确认

    # Connecting buttons in adminmain(超管主界面)
    # 跳转界面
    adminmain.pushButton_quit.clicked.connect(lambda: {adminmain.close(), login.show()})
    adminmain.pushButton_checkDoc.clicked.connect(lambda: {admin_show_doctor_to_check()})
    adminmain.pushButton_viewPatient.clicked.connect(lambda: {admin_show_patient_info()})
    adminmain.pushButton_viewDoc.clicked.connect(lambda: {admin_show_doctor_info()})
    adminmain.tableWidget.itemDoubleClicked.connect(admin_edit_doctor_info)
    adminmain.tableWidget_2.itemDoubleClicked.connect(admin_edit_doctor_info)
    adminmain.tableWidget_patient.itemDoubleClicked.connect(admin_edit_patient_info)
    # 按钮
    adminmain.pushButton_confirm.clicked.connect(lambda: {admin_edit_doctor_info_confirm()})
    adminmain.pushButton_cancel.clicked.connect(lambda: {adminmain.stackedWidget.setCurrentIndex(last_widget_idx)})
    adminmain.pushButton_confirm_2.clicked.connect(lambda: {admin_edit_patient_info_confirm()})
    adminmain.pushButton_cancel_2.clicked.connect(lambda: {adminmain.stackedWidget.setCurrentIndex(last_widget_idx)})
    # Connecting buttons in doctormain(医生主界面)
    # 跳转界面
    doctormain.pushButton_quit.clicked.connect(lambda: {doctormain.close(), login.show()})  # 退出登录
    doctormain.pushButton_viewPatient.clicked.connect(lambda: {doctor_show_patient_info()})  # 查看病人信息
    doctormain.pushButton_add.clicked.connect(lambda: {doctor_add_patient()})  # 添加负责病人
    doctormain.pushButton_ward.clicked.connect(lambda: {doctor_show_ward_info()})  # 查看病房信息
    doctormain.tableWidget.itemDoubleClicked.connect(doctor_edit_treatment)  # 双击跳转
    doctormain.tableWidget_2.itemDoubleClicked.connect(doctor_edit_ward_and_nurse)  # 双击跳转
    doctormain.pushButton_myProfile.clicked.connect(lambda: {doctor_show_personal_info()})  # 查看个人信息
    doctormain.pushButton_2.clicked.connect(lambda: {doctormain.stackedWidget.setCurrentIndex(last_widget_idx)})
    # 按钮
    doctormain.pushButton.clicked.connect(lambda: {doctor_add_patient_confirm()})
    doctormain.pushButton_confirm.clicked.connect(lambda: {doctor_edit_personal_information_confirm()})
    doctormain.pushButton_confirm_2.clicked.connect(lambda: {doctor_edit_treatment_confirm()})
    doctormain.pushButton_cancel.clicked.connect(lambda: {doctormain.stackedWidget.setCurrentIndex(0)})
    doctormain.pushButton_cancel_2.clicked.connect(lambda: {doctormain.stackedWidget.setCurrentIndex(0)})

    # Connecting buttons in patientmain(病人主界面)
    # 跳转界面
    patientmain.pushButton_quit_2.clicked.connect(lambda: {patientmain.close(), login.show()})
    patientmain.pushButton_viewPatient_2.clicked.connect(lambda: {patient_show_treatment()})
    patientmain.pushButton_myProfile.clicked.connect(lambda: {patient_show_personal_info()})
    # 按钮
    patientmain.pushButton_confirm.clicked.connect(lambda: {patient_edit_personal_info_confirm()})
    patientmain.pushButton_cancel.clicked.connect(lambda: {patientmain.stackedWidget_2.setCurrentIndex(0)})
    sys.exit(app.exec_())
