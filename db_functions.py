import mariadb
import sys
import pandas as pd
import os

from config import config


# Connection to database
def connect_ddbb():
    try:
        params = config()
        myconnection = mariadb.connect(**params)
        return myconnection
    except (Exception, mariadb.DatabaseError) as error:
        print(error)


# Upload students data (subjects and groups) to DB
def load_data_to_DB(lista):
    miConexion = connect_ddbb()
    miCursor = miConexion.cursor()
    for data in lista:
        try:
            # print(str(data))
            miCursor.execute("INSERT INTO registration VALUES(?,?,?)", data)
        except mariadb.IntegrityError:
            print("Duplicado :" + str(data))
    miCursor.execute('''
        INSERT INTO subjects (id_group, subject)
        SELECT id_group, subject
        FROM registration 
        WHERE NOT EXISTS(select id_group, subject from subjects)
        GROUP BY (id_group)
    ''')

    miConexion.commit()
    miConexion.close()


# Upload students to DB from a students list
def load_students_to_db(students_list):
    myConnection = connect_ddbb()
    myCursor = myConnection.cursor()
    for student in students_list:
        try:
            myCursor.execute("INSERT INTO students (student_id, student_name, student_last_name) VALUES (%s,%s,%s)",
                             student)
        except mariadb.IntegrityError:
            print("Student duplicated, skipped")
    myConnection.commit()
    myConnection.close()


# Query groups in DB
def get_groups():
    conexion = connect_ddbb()
    mycursor = conexion.cursor()
    sql = "SELECT id_group FROM subjects"
    mycursor.execute(sql)
    grupos = mycursor.fetchall()
    conexion.close()
    return grupos


# Query subject from a specific group in DB
def get_subjets(grupo):
    conexion = connect_ddbb()
    mycursor = conexion.cursor()
    sql = "SELECT subject FROM subjects WHERE id_group = %s"
    val = (grupo,)
    mycursor.execute(sql, val)
    subjects = mycursor.fetchall()
    conexion.close()
    return subjects


# Query active events from DB
def get_record_dates():
    conexion = connect_ddbb()
    mycursor = conexion.cursor()
    sql = "SELECT id_event, description, date_time FROM record_dates"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    conexion.close()
    values = []
    for i in range(len(data)):
        values.append(str(data[i][0]) + '···' + data[i][1] + '···' + str(data[i][2]))
    return values


# Convert to excel a list of students
def get_students_records(id_e, name):
    conexion = connect_ddbb()
    sql = "SELECT * FROM students_attendance WHERE id_event = " + id_e
    df = pd.read_sql_query(sql, con=conexion)
    excel_name = name + ' registros.xlsx'
    df.to_excel(excel_name)


# Insert new event date to DB
def insert_new_event_date(description, datetime, groups, subjects, email):
    try:
        conexion = connect_ddbb()
        mycursor = conexion.cursor()

        month, day, rest = datetime.split('/')
        year, hour = rest.split()
        date = '20' + year + '-' + month + '-' + day + ' ' + hour

        # Insert Event date and details into DB
        sql = "INSERT INTO record_dates (description, email, date_time) VALUES (%s,%s,%s)"
        var = (description, email, date,)
        mycursor.execute(sql, var)
        sql = "SELECT id_event FROM record_dates WHERE description = %s AND email = %s AND date_time = %s"
        mycursor.execute(sql, var)
        id_event = mycursor.fetchall()

        # Insert groups of event to record
        group = groups.split()
        subject = subjects.split('\n')
        for i in range(len(group)):
            sql = "INSERT INTO examn_groups (id_event, id_group, subject) VALUES (%s,%s,%s)"
            val = (id_event[0][0], group[i], subject[i],)
            mycursor.execute(sql, val)
            conexion.commit()
        conexion.close()
        return True
    except:
        return False


# Delete data from table
def delete_from_table(table):
    conexion = connect_ddbb()
    mycursor = conexion.cursor()
    mycursor.execute("DELETE FROM " + table)
    conexion.commit()
    conexion.close()


# Upload new students in database from CSV file
def new_students_to_db(file):
    name, ext = os.path.splitext(file)
    if ext == ".csv":
        df = pd.read_csv(file, index_col=None)
    else:
        df = pd.read_excel(file, index_col=None)
    df_list = []
    for row in df.to_numpy():
        df_list.append(tuple(row))
    load_students_to_db(df_list)


# Upload students data from CSV or EXCEL to DB
def apolo_file_to_ddbb(file):
    name, ext = os.path.splitext(file)
    if ext == ".csv":
        df = pd.read_csv(file, index_col=None)
    else:
        df = pd.read_excel(file, index_col=None)
    new_df = df[['GRUPO DE MATRICULA', 'NUM. EXPEDIENTE CENTRO', 'ASIGNATURA']].copy()
    # Turn dataframe to sql writtable data
    df_list = []
    for row in new_df.to_numpy():
        df_list.append(tuple(row))
    load_data_to_DB(df_list)
