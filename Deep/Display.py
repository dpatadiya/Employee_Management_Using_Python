
import os
import StudentVerification as SV
from Database import Record

class Employee:

    def __init__(self):

        e=SV.Verification()
        
        #self.studentEnrollment = e.verifyenrollment()
        self.first=input("Enter First name: ")
        self.last=input("Enter Last name: ")
        self.branch=input("Enter Branch: ")
        self.studentEmail = e.verifyemail()
        

while(1):

    print("\n 1. Add Student: ")
    print("2. Get Students By First Name: ")
    print("3. Remove Student By First Name:  ")
    #print("4. Update Employee Detail.")
     #print("5. ")
    print("5. Display Records")
    print("6. Exit..")


    ch=int(input("\n Enter ur choice no: "))

    if(ch==1):
        e=Employee()
        rec=Record()
        rec.add_record(e.first,e.last,e.branch,e.studentEmail)
        print("Insert Data Successfully...\n")

    elif(ch==2):
        rec=Record()
        first=input("Enter First Name: ")
        rec.get_student_by_name(first)

    elif(ch==3):
        rec=Record()
        first=input("Enter First Name: ")
        rec.Delete(first)
        print("Data Successfully Deleted...\n")

    elif(ch==5):
        rec=Record()
        rec.display()

    elif(ch==6):
        break

    else:
        print("Please Enter Valid Input!....")
       
        os.system('cls')

        
        



