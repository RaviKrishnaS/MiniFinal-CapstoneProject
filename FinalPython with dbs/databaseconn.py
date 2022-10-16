# import mysql.connector
#
# mydb=mysql.connector.connect(host='localhost',port=3306, user='root',password='pass@word1',database='ITCPROJECT',auth_plugin='mysql_native_password')
# mycursor=mydb.cursor()
# #mycursor.execute("CREATE DATABASE ITCPROJECT") database creation
# #mycursor.execute("SHOW DATABASES")
# #mycursor.execute("CREATE TABLE REGDATA(fullname varchar(20),email varchar(20),password varchar(20),phnumber varchar(20))")
# # sql="INSERT INTO REGDATA(fullname,email) VALUES(%s,%s)"
# # val=("ravikrishna","krishna@gmail.com")
# # mycursor.execute(sql,val)
# # #mycursor.execute("SHOW TABLES")
# # mydb.commit()
# mycursor.execute("UPDATE regdata set password='krishna', phnumber='8143305085' where fullname='ravikrishna'")
# mycursor.execute("select * from regdata where fullname='ravikrishna' ")
# result=mycursor.fetchone()
# print(result)