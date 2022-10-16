from courses import *;
from feepayment import *;
class Enrollment(FeePayment):
    def __init__(self):
        print("Welcome to Enrollment Page".center(50,"*"))
        self.cartdetailsstore=None

    def viewCourses(self):
        course = Courses()
        course.courseDetails(False)
        course.getallCourses()

    def enrollment(self):
        print("Choose Courses to enroll".center(30,"*"))
        course = Courses()
        course.courseDetails(True)
        self.cartdetailsstore=course.cartdetails

    def viewcart(self):
        if self.cartdetailsstore!=None:
            for i in self.cartdetailsstore:
                print(i+":"+self.cartdetailsstore[i])
            print("Sub total is :"+self.cartdetailsstore["Price"])
            print("Continue to Checkout...")
            print("press Yes[Y] to pay..")
            inz=input()
            if inz.lower()=="yes" or inz.lower()=="y":
                print("...Redirecting to payment Page...");
                feepaymentt=FeePayment();
                feepaymentt.paymentDetails(self.cartdetailsstore)

        else:
            print("You are not enrolled to any courses....Search for new Courses");


if __name__=="__main__":
    enroll=Enrollment();
    enroll.enrollment();
    enroll.viewcart();