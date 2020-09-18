import StudentVerification as sv

from StudentRecords import Record

class Student:

    _student_sem = 1
    _studentRollno =""
    _studentEnrollment =""
    _studentFirstName =""
    _studentLastName = ""
    _studentBranch = ""
    _studentEnrollmentyear = ""
    _studentEmail=""

    def __init__(self):

        e=sv.Verification()

        self._studentEnrollment = e.verifyenrollment()
        self._studentFirstName = input("Enter First name :")
        self._studentLastName =  input("Enter Last Name :")
        self._studentBranch = input("Enter Ur Branch: ")
        self._studentEnrollmentyear = input("Enter Ur EnrollmentYear: ")
        self._studentEmail = e.verifyemail()
        

print("1. Add Student ")
print("2. Display Records")
#print("3. Set ")
#print("4. ")
print("5. Get Students By Last Name")
print("6. Remove Student By Enrollment")


choice = int(input("Enter Ur Choice : "))

if(choice==1):
    s = Student()
    rec = Record()
    rec.add_record(s._studentEnrollment,s._studentFirstName,s._studentLastName,s._studentBranch,s._studentEnrollment,s._studentEmail)

    print("Student Record Addedd ")


elif(choice==2):
    rec = Record()
    rec.display_all()
    

elif(choice==5):

    rec =Record()
    last = input("Enter Last Name: ")
    rec.get_student_by_name(last)

elif(choice==6):
    
    rec =Record()
    enroll=input("enter Enrolllment No: ")
    rec.remove_by_enrollment(enroll)

    print("Record Deleted ")

else:
    print("Invalid Choice... ")