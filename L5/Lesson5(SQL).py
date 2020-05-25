import pymysql
conn = pymysql.connect(host = 'remotemysql.com', port = 3306, user = ' 7i3TTuLar2', passwd = '', ab = '7i3TTuLar2')     #conect to ewmotemysql
cursor = conn.cusror()                                                          #pointer to space in DB to read or write data                                                                                               #
cursor.execute()
cursor.close()                                                                  #close cursos
conn.close ()