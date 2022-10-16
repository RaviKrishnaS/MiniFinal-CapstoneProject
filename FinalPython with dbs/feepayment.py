import string
import random
import time
#from main import main
# define the random module
# S = 10  # number of characters in the string.
# # call random.choices() string module to find the string in Uppercase + numeric data.
# ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
# print("The randomly generated string is : " + str(ran)) # print the random data




class FeePayment():
    def __init__(self):
        print()
        print("PAYMENT PAGE".center(50,"*"))
        print("".center(70,"_"))
        self.randomsize=10
        self.paymentID=''.join(random.choices(string.ascii_uppercase + string.digits, k=self.randomsize))
    def paymentDetails(self,cartdetails):

        print("Choose Payment Method ")
        print("1.Upi")
        print("2.Debit card / Credit Card")
        payinp=input("Choose One from Above payment Method:")
        if payinp=="1":
            print("Enter UPI ID, UPi Pin to proceed..")
            upiinp=input("Enter UPI ID:")
            inpp=input("UPI PIN:")
            if bool(inpp)==(True):
                print("Payment Successfully Done...")
                print("Rupees "+cartdetails["Price"].rstrip("Rs")+"got debited from your  Bank account for "+"\"%s\""%cartdetails["Course Name"]+"Course..")
                print("Payment ID:"+self.paymentID)
                print("Payment Cost:"+cartdetails["Price"])
                print("Payment Date:"+"14-10-2022")
                print("Thank you.... Enroll for more")
                print("Loading Back to Mainpage..", end="")
                for i in range(0, 3):
                    print(".", end="")
                    time.sleep(2)
                print("")

            else:
                print("Payment Error Redirecting to Back......")