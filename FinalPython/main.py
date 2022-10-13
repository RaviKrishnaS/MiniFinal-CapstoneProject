
from login import *
from register import *
import os
import time

from enrollment import *
def welcome():
    print()
    print("Welcome to EONLINE Course".center(70,"-"))

def main():
    print("Loading",end="")
    for i in range(0,3):
        print(".",end="")
        time.sleep(1)
    print()
    os.system('cls')
    print(" MAIN PAGE ".center(45,"*"))
    print("1.Register/Signup")
    print("2.Login")
    print("3.Terms")
    print("Select Option:")
    choice=(input())
    match (choice):
        case '1':
            regis = Registration()
            regis.input()
            regis.emailcheck()
            inp=input("Press Back to main page [y/n]:")
            time.sleep(2)

            if inp.lower()=="y" or "yes" :
                main()
            elif inp.lower()=="n":
                print("You are already Registered ...")
                print("press back to main page..")
                time.sleep(2)

        case '2':

            login = Login()
            login.input()
            z=listreg
            # print(z)
            if listreg!=[]:
                k = login.check(z)
            else :
                k=False
            if k == True:
                print("Loading", end="")
                for i in range(0, 3):
                    print(".", end="")
                    time.sleep(1)
                print("")
                def homepage():
                    print("Welcome to Homepage".center(50,"*"))
                    print("1.Enroll For a Course...")
                    print("2.View All Courses...")
                    print("3.View Cart ")
                    print("4.Logout")
                    inp = (input("Enter Any option :"))
                    if inp == "1":
                        enroll=Enrollment()
                        print("1.Press one to View List of Courses..")
                        print("2.Press two to Enroll Course.. ")
                        enrp = input("Enter any choice:")
                        if enrp=="1":
                            enroll.viewCourses()
                            print("Enter Yes[y] to Enroll or No[N] to back:",end="")
                            inpp=input()
                            if inpp.lower()=="yes" or inpp.lower()=="y":
                                enroll.enrollment()
                                print("View Cart.......")
                                print("Enter yes [y] to go to cart")
                                cartinp=input()
                                if cartinp.lower()=="yes" or cartinp.lower()=="y":
                                    enroll.viewcart()
                                    homepage()
                            else :
                                print("Back...")
                                homepage()
                        elif enrp=="2":
                            enroll.enrollment()
                            print("View Cart.......")
                            print("Enter yes [y] to go to cart")
                            cartinp = input()
                            if cartinp.lower() == "yes" or cartinp.lower() == "y":
                                enroll.viewcart()
                                homepage()
                    elif inp == "2":
                        enroll=Enrollment()
                        enroll.viewCourses()
                        print("Enter yes to come back...or No to Logout:")
                        cartinppp = input()
                        if cartinppp.lower() == "yes" or cartinppp.lower() == "y":
                            homepage()
                        else:
                            main()

                    elif inp == "3":
                        print("View Cart...")
                        enroll=Enrollment()
                        enroll.viewcart()
                        print("Enter yes to come back...or No to Logout:")
                        cartinpp=input()
                        if cartinpp.lower()=="yes" or cartinpp.lower()=="y":
                            homepage()
                        else:
                            main()


                    elif inp == "4":
                        main()
                    else:
                        print("Invalid Option")
                        main()
                homepage()
            else:
                print("Invalid Email OR Password")
                main()
        case '3':
            filepp=open('Terms.txt','r')
            print(filepp.read())
            filepp.close()
            print()
            print("click on Back Enter yes[y]:")
            inp=input()
            if inp.lower()=="yes" or inp.lower()=="y":
                main()


        case default:
            print("INVALID OPTION")
            main()


if __name__=="__main__":
    welcome()
    main()






    # for i in range(0,40):
    #     print("_",end="")
    # print()
    # print("hai")
    # print("hello")
    # for j in range(0,40):
    #     print("_",end="")