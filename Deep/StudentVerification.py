import re

class Verification:

    def verifyemail(self):

        pattern=re.compile(r"[a-z0-9_]+@[a-z]+\.(com|edu|in)")

        while 1:
            email=input("Enter Email: ")
            
            if pattern.match(email):

                return email
            
            print("Invalid Email ") 

    def verifyenrollment(self):

        pattern=re.compile(r"[1-9][1-9]SOECE|SOEIT[1-9][1-9][1-9][1-9][1-9]")

        while 1:
            
            enr=input("Enrollmnt No: ")

            if pattern.match(enr):

                return enr
            print("Invalid Enrollment")