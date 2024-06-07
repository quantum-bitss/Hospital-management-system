import sqlite3


class DataBase(object):

    def __init__(self):
        self.path = "Database.db"
        self.create_table()

    def create_table(self):
        sql_patient = '''CREATE TABLE IF NOT EXISTS Patient
                                (Name Varchar NOT NULL,
                                Sex Varchar NOT NULL,
                                ID INT(10) NOT NULL,
                                Password Varchar NOT NULL,
                                Del Bool NOT NULL,
                                Telephone_num INT(11) NOT NULL,
                                Age INT NOT NULL,
                                Ward_num INT,
                                Medical_records Varchar,
                                Allergy Varchar,
                                PRIMARY KEY(ID));'''

        sql_doctor = '''CREATE TABLE IF NOT EXISTS Doctor
                                (Name Varchar NOT NULL,
                                Sex Varchar NOT NULL,
                                ID INT(7) NOT NULL,
                                Password Varchar NOT NULL,
                                Del Bool NOT NULL,
                                Telephone_num INT(11) NOT NULL,
                                Department Varchar NOT NULL,
                                Infor_review Bool NOT NULL,
                                PRIMARY KEY(ID));'''

        sql_ward = '''CREATE TABLE IF NOT EXISTS Ward
                                (Ward_num INT NOT NULL,
                                Patient_name Varchar NOT NULL,
                                Patient_ID INT(10) NOT NULL,
                                Nurse_name Varchar,
                                PRIMARY KEY(Ward_num));'''

        sql_treat = '''CREATE TABLE IF NOT EXISTS Treat
                                    (Patient_ID INT(10) NOT NULL,
                                    Doctor_ID INT(7) NOT NULL,
                                    Treatment Varchar,
                                    PRIMARY KEY(Patient_ID, Doctor_ID))'''

        self.connect_to_update(sql_patient)
        self.connect_to_update(sql_doctor)
        self.connect_to_update(sql_ward)
        self.connect_to_update(sql_treat)

    # 此函数用来执行sql语句，无返回值
    def connect_to_update(self, do):
        with sqlite3.connect(self.path) as conn:
            cur = conn.cursor()
            try:
                cur.execute(do)
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
        pass

    # 查看表的结构
    def show_structure(self, name):
        do = 'PRAGMA table_info(' + name + ')'
        with sqlite3.connect(self.path) as conn:
            cur = conn.cursor()
            try:
                cur.execute(do)
                print(cur.fetchall())
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        pass

    # 此函数用来执行sql语句并获得返回值，返回值为二维列表
    def connect_to_fatch(self, do):
        with sqlite3.connect(self.path) as conn:
            cur = conn.cursor()
            try:
                cur.execute(do)
                text = cur.fetchall()
                if type(text) == list:
                    return text
                else:
                    return []
            except Exception as e:
                print(e)
                raise e
        pass

    # 此函数用来获取Patient表的所有值，返回值为二维列表
    def show_patient(self):
        sql = "select * from Patient"
        return self.connect_to_fatch(sql)

    # 此函数用来获取Doctor表的所有值，返回值为二维列表
    def show_doctor(self):
        sql = "select * from Doctor"
        return self.connect_to_fatch(sql)

    # 此函数用来获取Ward表的所有值，返回值为二维列表
    def show_ward(self):
        sql = 'select * from Ward'
        return self.connect_to_fatch(sql)

    def show_treat(self):
        sql = 'select * from Treat'
        return self.connect_to_fatch(sql)

    # insert函数返回bool值
    def insert_patient(self, patient):  # 数字-1表示无此项输入，正常输入均为string类型，插入前先检测ID是否重复
        name = patient['name']
        sex = patient['sex']
        id = patient['id']
        password = patient['password']
        delete = patient['del']
        telephone_num = patient['telephone_num']
        age = patient['age']
        ward_num = patient['ward_num']  # 可以为Null，即-1
        medical_records = patient['medical_records']  # 可以为Null，即-1
        allergy = patient['allergy']  # 可以为Null，即-1
        sql1 = "insert into Patient(Name, Sex, ID, Password, Del, Telephone_num, Age"
        sql2 = "values('%s', '%s', %s, '%s', %s, %s, %s" % (name, sex, id, password, delete, telephone_num, age)
        if ward_num != -1:
            sql1 += ", Ward_num"
            sql2 += ", %s" % ward_num
        if medical_records != -1:
            sql1 += ", Medical_records"
            sql2 += ", '%s'" % medical_records
        if allergy != -1:
            sql1 += ", Allergy"
            sql2 += ", '%s'" % allergy
        sql = sql1 + ") " + sql2 + ")"
        # sql = ("insert into Patient(Name, Sex, ID, Password, Del, "
        #        "Telephone_num, Age, Ward_num, Medical_records, Allergy) "
        #        "values('%s', '%s', %s, '%s', %s, %s, %s, %s, '%s', '%s')")
        # sql = sql % (name, sex, id, password, delete, telephone_num, age, ward_num, medical_records, allergy)
        sql3 = "select * from Patient where ID = %s"
        try:
            results = self.connect_to_fatch(sql3 % id)
            if len(results) == 0:
                print(sql)
                self.connect_to_update(sql)
                return True
            else:
                print('ID repeats.')
                return False
        except Exception as e:
            print(e)
            return False

    def insert_doctor(self, doctor):  # 都是Not Null
        sql = ("insert into Doctor(Name, Sex, ID, Password, "
               "Del, Telephone_num, Department, Infor_review) "
               "values('%s', '%s', %s, '%s', %s, %s, '%s', %s)")
        name = doctor['name']
        sex = doctor['sex']
        id = doctor['id']
        password = doctor['password']
        delete = doctor['del']
        telephone_num = doctor['telephone_num']
        department = doctor['department']
        infor_review = doctor['infor_review']
        sql = sql % (name, sex, id, password, delete, telephone_num, department, infor_review)
        sql1 = "select * from Doctor where ID = %s"
        try:
            results = self.connect_to_fatch(sql1 % id)
            if len(results) == 0:
                print(sql)
                self.connect_to_update(sql)
                return True
            else:
                print('ID repeats.')
                return False
        except Exception as e:
            print(e)
            return False

    def insert_ward(self, ward):  # 都是Not Null
        ward_num = ward['ward_num']
        patient_name = ward['patient_name']
        patient_id = ward['patient_id']
        nurse_name = ward['nurse_name']
        sql1 = "insert into Ward(Ward_num, Patient_name, Patient_ID"
        sql2 = "values(%s, '%s', %s" % (ward_num, patient_name, patient_id)
        if nurse_name != -1:
            sql1 += ", Nurse_name"
            sql2 += ", '%s'" % nurse_name
        sql = sql1 + ") " + sql2 + ")"
        sql3 = "select * from Ward where Ward_num = %s"
        try:
            results = self.connect_to_fatch(sql3 % ward_num)
            if len(results) == 0:
                print(sql)
                self.connect_to_update(sql)
                return True
            else:
                print('Ward_num repeats.')
                return False
        except Exception as e:
            print(e)
            return False

    def insert_treat(self, treat):
        patient_id = treat['patient_id']
        doctor_id = treat['doctor_id']
        treatment = treat['treatment']
        sql1 = "insert into Treat(Patient_ID, Doctor_ID"
        sql2 = "values(%s, %s" % (patient_id, doctor_id)
        if treatment != -1:
            sql1 += ", Treatment"
            sql2 += ", '%s'" % treatment
        sql = sql1 + ") " + sql2 + ")"
        sql3 = "select * from Treat where Patient_ID = %s and Doctor_ID = %s"
        try:
            results = self.connect_to_fatch(sql3 % (patient_id, doctor_id))
            if len(results) == 0:
                print(sql)
                self.connect_to_update(sql)
                return True
            else:
                print('Treatment repeats.')
                return False
        except Exception as e:
            print(e)
            return False

    # def delete_patient(self, patient):  # 不支持批量删除，只支持用Key删除，删除前检查对象不存在错误
    #     id = patient['id']  # 空输入错误由前端检测
    #     sql = "select * from Patient where ID = %s" % id
    #     results = self.connect_to_fatch(sql)  # 删除前先检查有没有这一项
    #     if len(results) == 0:
    #         return False  # 对象不存在
    #     sql = "delete from Patient where ID = %s" % id
    #     try:
    #         print(sql)
    #         self.connect_to_update(sql)
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False

    # delete函数返回bool值，病人和医生的删除改为逻辑删，设置Del属性为1表示逻辑上的已删除，配合ID分配，前端分配逻辑删账号时应调用modify函数
    # 当用户重新注册逻辑删账户后，将此账户id记下来，先删除此项再用该id创建新项，避免可能为null的属性值不一致
    def delete_patient(self, patient):
        id = patient['id']  # 空输入错误由前端检测
        delete = patient['del']
        if delete == '0':  # 对未逻辑删的账号是逻辑删操作
            sql = "select * from Patient where ID = %s and Del = %s" % (id, '0')  # 找到未逻辑删的账号，防止重复删除
            results = self.connect_to_fatch(sql)
            if len(results) == 0:
                return False  # 对象已删除
            else:
                key = {'name': -1, 'sex': -1, 'id': id, 'password': -1, 'del': '1',
                       'telephone_num': -1, 'age': -1, 'ward_num': -1, 'medical_records': -1, 'allergy': -1}  # 只修改del属性
                self.modify_patient(key)  # modify函数需要有-1输入检测
                return True
        elif delete == '1':  # 对逻辑删账号是删除操作
            sql = "select * from Patient where ID = %s and Del = %s" % (id, '1')  # 找到逻辑删的账号，删除原来的账号
            results = self.connect_to_fatch(sql)  # 删除前先检查有没有这一项
            if len(results) == 0:
                return False  # 对象不存在
            sql = "delete from Patient where ID = %s" % id
            try:
                print(sql)
                self.connect_to_update(sql)
                return True
            except Exception as e:
                print(e)
                return False

    def delete_doctor(self, doctor):
        id = doctor['id']
        delete = doctor['del']
        if delete == '0':  # 对未逻辑删的账号是逻辑删操作
            sql = "select * from Doctor where ID = %s and Del = %s" % (id, '0')
            results = self.connect_to_fatch(sql)
            if len(results) == 0:
                return False  # 对象已删除
            else:
                key = {'name': -1, 'sex': -1, 'id': id, 'password': -1, 'del': '1',
                       'telephone_num': -1, 'department': -1, 'infor_review': -1}  # 将del属性置为1
                self.modify_doctor(key)
                return True
        elif delete == '1':
            sql = "select * from Doctor where ID = %s and Del = %s" % (id, '1')  # 找到逻辑删的账号，删除原来的账号
            results = self.connect_to_fatch(sql)  # 删除前先检查有没有这一项
            if len(results) == 0:
                return False  # 对象不存在
            sql = "delete from Doctor where ID = %s" % id
            try:
                print(sql)
                self.connect_to_update(sql)
                return True
            except Exception as e:
                print(e)
                return False

    def delete_ward(self, ward):
        ward_num = ward['ward_num']
        sql = "select * from Ward where Ward_num = %s" % ward_num
        results = self.connect_to_fatch(sql)
        if len(results) == 0:
            return False  # 对象不存在
        sql = "delete from Ward where Ward_num = %s" % ward_num
        try:
            print(sql)
            self.connect_to_update(sql)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_treat(self, treat):
        patient_id = treat['patient_id']
        doctor_id = treat['doctor_id']
        sql = "select * from Treat where Patient_ID = %s and Doctor_ID = %s" % (patient_id, doctor_id)
        results = self.connect_to_fatch(sql)
        if len(results) == 0:
            return False  # 对象不存在
        sql = "delete from Treat where Patient_ID = %s and Doctor_ID = %s" % (patient_id, doctor_id)
        try:
            print(sql)
            self.connect_to_update(sql)
            return True
        except Exception as e:
            print(e)
            return False

    # modify函数返回bool值，需要检测-1空输入，modify函数输入的每一项都可能取-1，表示不修改，除了id之外至少还有一个属性
    def modify_patient(self, patient):
        name = patient['name']
        sex = patient['sex']
        id = patient['id']  # id一定不为空
        password = patient['password']
        delete = patient['del']
        telephone_num = patient['telephone_num']
        age = patient['age']
        ward_num = patient['ward_num']
        medical_records = patient['medical_records']
        allergy = patient['allergy']
        sql = "update Patient set "
        if name != -1:
            sql += "Name = '%s', " % name
        if sex != -1:
            sql += "Sex = '%s', " % sex
        if password != -1:
            sql += "Password = '%s', " % password
        if delete != -1:
            sql += "Del = %s, " % delete
        if telephone_num != -1:
            sql += "Telephone_num = %s, " % telephone_num
        if age != -1:
            sql += "Age = %s, " % age
        if ward_num != -1:
            sql += "Ward_num = %s, " % ward_num
        if medical_records != -1:
            sql += "Medical_records = '%s', " % medical_records
        if allergy != -1:
            sql += "Allergy = '%s', " % allergy
        sql = sql[:-2] + " where ID = %s" % id
        print(sql)
        self.connect_to_update(sql)
        return True
        # sql = ("update Patient set Name = '%s', Sex = '%s', Password = '%s', Del = %s, "
        #        "Telephone_num = %s, Age = %s, Ward_num = %s, Medical_records = '%s', "
        #        "Allergy = '%s' where ID = %s")  # 数据类型是数字的就不用单引号
        # self.connect_to_update(sql % (name, sex, password, delete, telephone_num,
        #                               age, ward_num, medical_records, allergy, id))

    def modify_doctor(self, doctor):
        name = doctor['name']
        sex = doctor['sex']
        id = doctor['id']
        password = doctor['password']
        delete = doctor['del']
        telephone_num = doctor['telephone_num']
        department = doctor['department']
        infor_review = doctor['infor_review']
        sql = "update Doctor set "
        if name != -1:
            sql += "Name = '%s', " % name
        if sex != -1:
            sql += "Sex = '%s', " % sex
        if password != -1:
            sql += "Password = '%s', " % password
        if delete != -1:
            sql += "Del = %s, " % delete
        if telephone_num != -1:
            sql += "Telephone_num = %s, " % telephone_num
        if department != -1:
            sql += "Department = '%s', " % department
        if infor_review != -1:
            sql += "Infor_review = %s, " % infor_review
        sql = sql[:-2] + " where ID = %s" % id
        self.connect_to_update(sql)
        return True
        # sql = ("update Doctor set Name = '%s', Sex = '%s', Password = '%s', Del = %s, "
        #        "Telephone_num = %s, Department = '%s', Infor_review = %s where ID = %s")
        # self.connect_to_update(sql % (name, sex, password, delete,
        #                               telephone_num, department, infor_review, id))

    def modify_ward(self, ward):  # 锁定了ward_num不能修改！
        ward_num = ward['ward_num']
        patient_name = ward['patient_name']
        patient_id = ward['patient_id']
        nurse_name = ward['nurse_name']
        sql = "update Ward set "
        if patient_name != -1:
            sql += "Patient_Name = '%s', " % patient_name
        if patient_id != -1:
            sql += "Patient_ID = %s, " % patient_id
        if nurse_name != -1:
            sql += "Nurse_name = '%s', " % nurse_name
        sql = sql[:-2] + " where Ward_num = %s" % ward_num
        self.connect_to_update(sql)
        return True
        # sql = ("update Ward set Patient_name = '%s', Patient_ID = %s,"
        #        " Nurse_name = '%s' where Ward_num = %s")
        # self.connect_to_update(sql % (patient_name, patient_id, nurse_name, ward_num))

    def modify_treat(self, treat):
        patient_id = treat['patient_id']
        doctor_id = treat['doctor_id']
        treatment = treat['treatment']
        sql = "update Treat set Treatment = '%s' where Patient_ID = %s and Doctor_ID = %s"
        self.connect_to_update(sql % (treatment, patient_id, doctor_id))
        return True

    # search函数返回二维数列
    def search_patient(self, patient):
        name = patient['name']
        sex = patient['sex']
        id = patient['id']
        password = patient['password']
        delete = patient['del']
        telephone_num = patient['telephone_num']
        age = patient['age']
        ward_num = patient['ward_num']
        medical_records = patient['medical_records']
        allergy = patient['allergy']
        sql = "select * from Patient where "
        if name != -1:
            sql += "Name = '%s' and " % name
        if sex != -1:
            sql += "Sex = '%s' and " % sex
        if id != -1:
            sql += "ID = %s and " % id
        if password != -1:
            sql += "Password = '%s' and " % password
        if delete != -1:
            sql += "Del = %s and " % delete
        if telephone_num != -1:
            sql += "Telephone_num = %s and " % telephone_num
        if age != -1:
            sql += "Age = %s and " % age
        if ward_num != -1:
            sql += "Ward_num = %s and " % ward_num
        if medical_records != -1:
            sql += "Medical_records = '%s' and " % medical_records
        if allergy != -1:
            sql += "Allergy = '%s' and " % allergy
        # if id == -1 and name == -1 and sex == -1 and telephone_num == -1 and age == -1 and ward_num == -1 and medical_records == -1 and allergy == -1:
        #     return []
        # else:
        sql = sql[:len(sql)-4]
        print(sql)
        return self.connect_to_fatch(sql)

    def search_doctor(self, doctor):
        name = doctor['name']
        sex = doctor['sex']
        id = doctor['id']
        password = doctor['password']
        delete = doctor['del']
        telephone_num = doctor['telephone_num']
        department = doctor['department']
        infor_review = doctor['infor_review']
        sql = "select * from Doctor where "
        if name != -1:
            sql += "Name = '%s' and " % name
        if sex != -1:
            sql += "Sex = '%s' and " % sex
        if id != -1:
            sql += "ID = %s and " % id
        if password != -1:  # 密码不可以设为-1，可以引入密码设置规则，大小写字母加数字？
            sql += "Password = '%s' and " % password
        if delete != -1:
            sql += "Del = %s and " % delete
        if telephone_num != -1:
            sql += "Telephone_num = %s and " % telephone_num
        if department != -1:
            sql += "Department = '%s' and " % department
        if infor_review != -1:
            sql += "Infor_review = %s and " % infor_review
        # else:  # 都等于'-1'，相当于全空输入，但实际不可能，因为-1是手动设置的
        #     return []
        sql = sql[:len(sql)-4]
        print(sql)
        return self.connect_to_fatch(sql)

    def search_ward(self, ward):
        ward_num = ward['ward_num']
        patient_name = ward['patient_name']
        patient_id = ward['patient_id']
        nurse_name = ward['nurse_name']
        sql = "select * from Ward where "
        if ward_num != -1:
            sql += "Ward_num = %s and " % ward_num
        if patient_id != -1:
            sql += "Patient_ID = %s and " % patient_id
        if patient_name != -1:
            sql += "Patient_name = '%s' and " % patient_name
        if nurse_name != -1:
            sql += "Nurse_name = '%s' and " % nurse_name
        # else:
        #     return []
        sql = sql[:len(sql)-4]
        print(sql)
        return self.connect_to_fatch(sql)

    def search_treat(self, treat):
        patient_id = treat['patient_id']
        doctor_id = treat['doctor_id']
        treatment = treat['treatment']
        sql = "select * from Treat where "
        if patient_id != -1:
            sql += "Patient_ID = %s and " % patient_id
        if doctor_id != -1:
            sql += "Doctor_ID = %s and " % doctor_id
        if treatment != -1:
            sql += "Treatment = '%s' and " % treatment
        sql = sql[:len(sql)-4]
        print(sql)
        return self.connect_to_fatch(sql)

    # 测试函数
    def test(self):
        x = {'name': 'lihua', 'sex': 'Male', 'id': '12345', 'password': '123', 'del': '0',
             'telephone_num': '1234', 'age': '21', 'ward_num': -1, 'medical_records': -1, 'allergy': -1}  # 默认从前端获得的数据类型都是string
        print(self.show_patient())
        print(self.insert_patient(x))
        print(self.show_patient())
        print(self.delete_patient(x))
        print(self.show_patient())
        self.insert_ward({'ward_num': 2, 'patient_name': 'lihua', 'patient_id': '0000000200', 'nurse_name': -1})
        print(self.show_ward())


if __name__ == '__main__':
    x = DataBase()
    x.test()
