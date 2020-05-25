import pymysql
#estableshing connection
conn = pymysql.connect(host='remotemysql.com', port=3306, user='7i3TTuLar2', passwd = 'a7vQj4sTDI',db = '7i3TTuLar2')     #conect to ewmotemysql
conn.autocommit(True)
#getting a cursor from DB
cursor = conn.cursor()

#Delete DATA from table
cursor.execute("INSERT into 7i3TTuLar2.dogs(name,age,breed) VALUES ('Tiffy',9,'west highland white terrier')")
cursor.execute("INSERT into 7i3TTuLar2.dogs(name,age,breed) VALUES ('Baks',11,'spaniel')")
cursor.execute("INSERT into 7i3TTuLar2.dogs(name,age,breed) VALUES ('Reks',2,'alabay')")


cursor.close()
conn.close()