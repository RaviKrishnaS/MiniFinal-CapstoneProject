class CustomException(Exception):
    def __init__(self):
        print("Search Not Found Exception")

class Courses:
    def __init__(self):
        print("Welcome to Course Details".center(45, "#"))

        self.courseCategory=None
        self.listofcourseCategory=None
        self.dictofcourse=None
        self.dictcoursedet=None
        self.cartdetails=None
        self.coursecheck=None
    def courseDetails(self,cinp=False):
        self.courseCategory=["Web Development","Business","IT&Software","Design"]
        self.listofcourseCategory=[["Java Script","React JS"],["Business Fundamentals","Communication"],["Python","C","Java",],["Graphic Design","Photoshop"]]
        self.dictofcourse=dict(zip(self.courseCategory,self.listofcourseCategory))
        self.dictcoursedet={"Java Script":{"Course Name":"learn Java Script for Beginners","School":"Dollar Design","Rating":"****","Price":"400/- Rs"},
                            "React JS":{"Course Name":"React JS for Beginners","School":"john purcel","Rating":"*****","Price":"600/- Rs"},
                            "Business Fundamentals": {" Course Name": " Bussiness Fundamentals for Beginners", "School": " purcel", "Rating": "*****","Price": "660/- Rs"},
                            "Communication": {"Course Name": "Business Communication for Beginners", "School": "Mark Purcel", "Rating": "*****","Price": "700/- Rs"},
                            "Python": {"Course Name": "Python from Scratch  ", "School": "John Purcel",
                                              "Rating": "*****", "Price": "650/- Rs"},
                            "C": {"Course Name": "C Programming  for Beginners ", "School": "john purcel",
                                       "Rating": "*****", "Price": "450/- Rs"},
                            "Java": {"Course Name": " Java Full Stack for Beginners ", "School": "john don",
                                       "Rating": "****", "Price": "500/- Rs"},
                            "Graphic Design": {"Course Name": "Graphic Design from Scratch ", "School": "john purcel don",
                                       "Rating": "*****", "Price": "850/- Rs"},
                            "Photoshop": {"Course Name": "Simple Photoshop ", "School": "Joe purcel",
                                       "Rating": "****", "Price": "700/- Rs"},

                            }

        if cinp==True:
            def fun():
                for i in self.courseCategory:
                    print(".* " + i)
                search=input("Enter a category:")
                if search in (self.courseCategory):
                    for i in self.dictofcourse[search]:
                        print(" *."+i)
                    searchcourse=input("Enter Course From Following: ")

                    for i in self.listofcourseCategory:
                        for j in i:
                            if searchcourse in j:
                                self.coursecheck=True
                                print("-__".center(50,"*"))
                                k=self.dictcoursedet[searchcourse]
                                for m in k:
                                    print(m+"::"+k[m])

                                print("__-".center(50,"*"))
                                print("Press yes[y] to Add to cart No[N] to Cancel :")
                                inp=input()

                                if inp.lower()=="yes" or inp.lower()=="y":
                                    self.cartdetails=k
                                    filesd = open('cartdetails.txt', 'a')
                                    filesd.writelines(str(k))
                                    filesd.close()
                                elif inp.lower()=="no" or inp.lower()=="n":
                                     fun()
                                else :
                                    print("Wrong Input....Loading back")
                                    fun()
                            else:

                                self.coursecheck=False
                        #
                        # if self.coursecheck==False:
                        #     try:
                        #         raise CustomException()
                        #
                        #     except CustomException as ex:
                        #         print(ex)
                        #     return fun()
                elif search not in self.courseCategory:
                    try:
                        raise CustomException()

                    except CustomException as ex:
                        print(ex)
                    fun()
            fun()



    def getallCourses(self):
        k=self.dictcoursedet
        for i in k:
            print("-__".center(50, "*"))

            description=k[i]
            for j in description:
                print(j+"::"+description[j])
            print("-__".center(50, "*"))
            print()
if __name__=="__main__":
    course=Courses()
    course.courseDetails(True)
    # course.getallCourses()
