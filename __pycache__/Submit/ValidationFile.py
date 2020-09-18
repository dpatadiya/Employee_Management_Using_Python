import re

class Validation:
    def __init__(self):
        self.EmailPattern=re.compile(r'[a-zA-z]+[.0-9+-]+[a-zA-z0-9]*@[a-zA-z]+[0-9-]*\.[a-zA-z]+[0-9-.]*')
        self.MobileNumberPattern=re.compile(r'\d{10}')

    #Validation To Check Enrollment Number Is Valid Or Not...
    def MobileNumberValidation(self):
        while(True):
            self.MobileNumber=input("Enter Mobile Number :")
            self.match=self.MobileNumberPattern.findall(self.MobileNumber)
            if(len(self.match)==0):
                print("<<<<     Please Enter Valid Enrollment Number!...     >>>>")
            else:
                return self.MobileNumber

    #Validation To Check Email Is Valid Or Not...
    def EmailValidation(self):
         while(True):
            self.Email=input("Enter Email :")
            self.match=self.EmailPattern.findall(self.Email)
            if(len(self.match)==0):
                print("<<<<     Please Enter Valid Email!...     >>>>")
            else:
                return self.Email   
