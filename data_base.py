import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host='localhost', port='3306', user='root', password='your password', database='hospital',
            auth_plugin='mysql_native_password')
        query = 'create table if not exists patient(patient_id int primary key,' \
                'patient_name varchar(1000),patient_age int,admin_date char,patient_reason varchar(100),' \
                'patient_bill int,patient_eid varchar(100))'
        cur = self.con.cursor()
        cur.execute(query)

    # inserting
    def insert_patient(self, patientid, patientname, patientage, admissiondate, patientresion, patientbill, patienteid):

        query = "insert into patient(patient_id,patient_name,patient_age,admin_date,patient_reason,patient_bill," \
                "patient_eid)" \
                "values({},'{}',{},'{}','{}',{},'{}')".format(patientid, patientname, patientage, admissiondate,
                                                              patientresion, patientbill, patienteid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # Fetch
    def fetch_patient(self, patientid):
        query = f"select * from patient"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            if patientid == row[0]:
                return row

    # delete
    def delete_patient(self, patientid):
        query = "delete from patient where patient_id={}".format(patientid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # update
    def update_patient(self, patientid, newname, newage, newdate, newresion, patientbill, patienteid):
        query = "update patient set patient_name='{}',patient_age={},admin_date='{}',patient_reason='{}'," \
                "patient_bill={},patient_eid='{}'where patient_id={}".format(
            newname, newage, newdate, newresion, patientbill, patienteid, patientid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # quit
    def quit_server(self):
        quit()
d = DBHelper()
