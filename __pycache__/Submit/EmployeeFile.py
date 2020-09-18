import os
import DatabaseFile
import ValidationFile
class Employee:

    #Init Method to initialize Employee Object and Insert Data Into DataBase...
    def __init__(self,Flag=True):
       
        self.FirstName=input("Enter First Name :")
        self.LastName=input("Enter Last Name :")

        if(Flag):
            v=ValidationFile.Validation()
            self.Email=v.EmailValidation()

        v=ValidationFile.Validation()
        self.MobileNumber=v.MobileNumberValidation()
        
        self.City=input("Enter City Name :")

 
while(True):
    print("1. Insert Employee Detail.\n2. Update Employee Detail.\n3. Delete Employee Detail.\n4. Display Employee Detail.\n5. Exit.")
    
    try:
        ch=int(input("Enter your choice :"))
        if(ch==1):
            E=Employee()
            D=DatabaseFile.Database()
            D.InsertRecord(E.FirstName,E.LastName,E.MobileNumber,E.Email,E.City)

        elif(ch==2):
            Employee.Email=input("Enter Email :")
            Employee.Flag=False   
            D=DatabaseFile.Database()
            D.DataExists=D.DisplayEmployee(Employee.Email)
            if(D.DataExists):
                print("Enter Details where you have to Update it.")
                E=Employee(Employee.Flag)
                D.UpdateEmployee(E.FirstName,E.LastName,E.MobileNumber,Employee.Email,E.City)

        elif(ch==3):
            Employee.Email=input("Enter Email :")
            D=DatabaseFile.Database()
            D.DeleteEmployee(Employee.Email)
        elif(ch==4):
            Employee.Email=input("Enter Email :")
            D=DatabaseFile.Database()
            D.DisplayEmployee(Employee.Email)
        elif(ch==5):
            break
        else:
            print("Please Enter Valid Input!....")
        
    except Exception as e:
        print(str(e))

    finally:
        input("Press Any Key To Continue...")
        os.system('cls')
