from register import *;
class Login(Registration):
    def __init__(self):
        print("Welcome to Login page".center(50, '*'))
        # super().__init__()
        # regis=Registration()

    def input(self):
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")

    # def check(self, listreg):
    #
    #     for i in listreg:
    #         if self.email == i['email'] and self.password == i['password']:
    #             return True
    #         else:
    #             return False
    def dbcheck(self):
        mycursor.execute("select * from regidata where email='{}'".format(self.email))
        result = mycursor.fetchone()
        if result!=None:

            if self.email ==result[1] and self.password==result[2]:
                return True
            else:
                return False
        else:
            print("Enter Valid Details...")
if __name__=="__main__":
    login=Login()
    login.input()
    login.dbcheck()