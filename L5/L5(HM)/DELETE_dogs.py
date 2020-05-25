import pymysql
#estableshing connection
conn = pymysql.connect(host='remotemysql.com', port=3306, user='7i3TTuLar2', passwd = 'a7vQj4sTDI',db = '7i3TTuLar2')     #conect to ewmotemysql
conn.autocommit(True)
#getting a cursor from DB
cursor = conn.cursor()

#Delete DATA from table
cursor.execute("DELETE  FROM 7i3TTuLar2.dogs WHERE name = 'Reks'")

cursor.close()
conn.close()