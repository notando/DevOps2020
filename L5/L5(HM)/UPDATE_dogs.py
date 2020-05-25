import pymysql
#estableshing connection
conn = pymysql.connect(host='remotemysql.com', port=3306, user='7i3TTuLar2', passwd = 'a7vQj4sTDI',db = '7i3TTuLar2')     #conect to ewmotemysql
conn.autocommit(True)
#getting a cursor from DB
cursor = conn.cursor()

#Delete DATA from table
cursor.execute("UPDATE  7i3TTuLar2.dogs SET age='4' WHERE name = 'Baks'")

cursor.close()
conn.close()
