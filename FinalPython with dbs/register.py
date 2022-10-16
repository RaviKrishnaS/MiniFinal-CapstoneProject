import re
import mysql.connector
from mysql.connector import IntegrityError
import os
import time
listreg = []
dictreg = {}
result=None
mydb=mysql.connector.connect(host='localhost',port=3306, user='root',password='pass@word1',database='ITCPROJECT',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE ITCPROJECT") database creation
# mycursor.execute("SHOW DATABASES")
# # mycursor.execute("CREATE TABLE REGIDATA(fullname varchar(20),email varchar(20),password varchar(20),phnumber varchar(20))")
# sql="INSERT INTO REGDATA(fullname,email) VALUES(%s,%s)"
# val=("ravikrishna","krishna@gmail.com")
# mydb.commit()
# mycursor.execute("select * from regdata where fullname='ravikrishna' ")
# result=mycursor.fetchone()

class Registration:

    def __init__(self):
        print("Welcome to Registration page".center(30, "-"))

        global listreg
        global dictreg
        global result

    def input(self):
        self.fullname = str(input("Enter Full Name:"))
        self.email = input("Enter Email address:")
        self.password = input("Enter Password:")
        self.phnumber = (input("Enter Phone Number:"))

    def emailcheck(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # regexpass="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$ "
        # password = self.password

        t = True
        while t:
            e_mail = self.email

            if (re.fullmatch(regex, e_mail)):
                # list.append(e_mail)
                print("Email  and password are valid")
                Registration.store(self)

                t=False
                break
            else:
                print("Not a valid email or password")
                print("Enter Valid email again")
                # return False
                self.email=input("Enter Email again:")
                Registration.emailcheck(self)
                break

    def store(self):
        dictreg["fullname"] = self.fullname
        dictreg["email"] = self.email
        dictreg["password"] = self.password
        dictreg["phnumber"] = self.phnumber
        listreg.append(dictreg)
        filesd=open('storedetails.txt','a')
        filesd.writelines(str(listreg))
        filesd.close()

        sql = "INSERT INTO REGIDATA(fullname,email,password,phnumber) VALUES(%s,%s,%s,%s)"
        val=(self.fullname,self.email,self.password,self.phnumber)
        try :
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.execute("select * from regidata where email='{}'".format(self.email))
            result = mycursor.fetchone()
            print(result)
        except IntegrityError as err:
            print("Email already Registered..." )
            print("Enter New ONE")
            regis.input()
            regis.emailcheck()




if __name__=="__main__":
    regis = Registration()
    regis.input()
    regis.emailcheck()











