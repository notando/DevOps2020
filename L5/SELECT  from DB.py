import pymysql
#estableshing connection
conn = pymysql.connect(host='remotemysql.com', port=3306, user='7i3TTuLar2', passwd = 'a7vQj4sTDI',db = '7i3TTuLar2')     #conect to ewmotemysql
#getting a cursor from DB
cursor = conn.cursor()

#Geting ALL DATA from table ID
cursor.execute("SELECT * FROM 7i3TTuLar2.Situator;")


#Iterating table and print all users
for row in cursor:
    print(row)

cursor.close()
conn.close()