from register import *;
class Login(Registration):
    def __init__(self):
        print("Welcome to Login page".center(50, '*'))
        # super().__init__()
        # regis=Registration()

    def input(self):
        self.email = input("Enter Email:")
        self.password = input("Enter Password:")

    def check(self, listreg):

        for i in listreg:
            if self.email == i['email'] and self.password == i['password']:
                return True
            else:
                return False

if __name__=="__main__":
    login=Login()
    login.input()
    login.check([{'fullname': 'ravikrishna', 'email': 'ravi@gmail.com', 'password': 'Krishna@50', 'phnumber': '97486667859'}])