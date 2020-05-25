import pymysql
#estableshing connection
conn = pymysql.connect(host='remotemysql.com', port=3306, user='7i3TTuLar2', passwd = 'a7vQj4sTDI',db = '7i3TTuLar2')     #conect to ewmotemysql
conn.autocommit(True)
#getting a cursor from DB
cursor = conn.cursor()

#Delete DATA from table
cursor.execute("INSERT into 7i3TTuLar2.Situator(Name,ID) VALUES ('Rom',304)")
cursor.execute("INSERT into 7i3TTuLar2.Situator(Name,ID) VALUES ('An',478)")

cursor.close()
conn.close()