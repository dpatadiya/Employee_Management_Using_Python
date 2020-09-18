import sqlite3

class Database:
    def __init__(self):
        try:
            self.Connection=sqlite3.connect("EmoloyeeDatabase.db")
        except:
            print("Connection Error...")
       
            
        self.Curcer=self.Connection.cursor()
        try:
            self.Curcer.execute("CREATE TABLE EmoloyeeDetails (First_Name text,Last_Name text,Email text PRIMARY KEY,Mobile_Number text,City text)")
        except:
            pass

    def InsertRecord(self,FirstName,LastName,MobileNumber,Email,City):
        self.Curcer.execute("Insert into EmoloyeeDetails Values(?,?,?,?,?)",(FirstName,LastName,Email,MobileNumber,City))
        self.Connection.commit()
        print("Your Data Inserted Successfully")
        
    def DisplayEmployee(self,Email):
        self.Curcer.execute("SELECT * FROM EmoloyeeDetails WHERE Email=?",(Email,))
        self.lst=self.Curcer.fetchall()
        if(len(self.lst)==0):
            
            print("<<<<     Record is not exists!...     >>>>")
            return False
        else:
            self.Employee=self.lst[0]
            print("==========================================")
            print("First Name :",self.Employee[0])
            print("Last Name :",self.Employee[1])
            print("Email :",self.Employee[2])
            print("Monile Number :",self.Employee[3])
            print("City :",self.Employee[4])
            print("==========================================")
            return True

    def DeleteEmployee(self,Email):
        self.Curcer.execute("DELETE FROM EmoloyeeDetails WHERE Email=?",(Email,))
        self.deleted_rows=self.Curcer.rowcount
        if(self.deleted_rows==1):
            self.Connection.commit()
            print("Record Deleted Succesfully.")
        else:
            print("Record Not Found...")
    

    def UpdateEmployee(self,FirstName,LastName,MobileNumber,Email,City):
        self.Curcer.execute("update EmoloyeeDetails set First_Name=?,Last_Name=?,Mobile_Number=?,City=? where Email=?",(FirstName,LastName,MobileNumber,City,Email,))
        self.Connection.commit()
        print("Your Data Updated Successfully")
