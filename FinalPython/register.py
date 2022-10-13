import re
import os
import time
listreg = []
dictreg = {}
class Registration:

    def __init__(self):
        print("Welcome to Registration page".center(30, "-"))

        global listreg
        global dictreg

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
                print("----You are Registered----")
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
        for i in listreg:
            print("Your Details...")
            for j in i:
                print(j+":"+i[j])
        filesd=open('storedetails.txt','a')
        filesd.writelines(str(listreg))
        filesd.close()








