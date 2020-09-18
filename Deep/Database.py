import random
import sqlite3


class Record:

    def __init__(self):

        try:
            self.con=sqlite3.connect("Student.db")
        except:
            pass

        self.cur=self.con.cursor()

        try:
            self.cur.execute("Create table Student (Firstname text,Lastname text,Branch text,Email text)")
            self.con.commit()
        except:
            pass

    def add_record(self,efirst,elast,ebranch,eemail):

        self.cur.execute("Insert into Student (Firstname,Lastname,Branch,Email) Values (?,?,?,?)",(efirst,elast,ebranch,eemail))
        self.con.commit()

    def display(self):

        self.cur.execute("select * from Student")
        self.lst=self.cur.fetchall()
       
        if(len(self.lst)==0):
            print("Record is not foundd ")
            return False
        
        else:
            self.Employee=self.lst[0]
            print("==========================================")
            #print("Enrollment :",self.Employee[0])
            print("First Name :",self.Employee[1])
            print("Last Name :",self.Employee[2])
            print("Branch :",self.Employee[3])
            print("Email :",self.Employee[4])
            #print("Monile Number :",self.Employee[3])
            #print("City :",self.Employee[4])
            print("==========================================")
            return True
        


    def Delete(self,Email):

        self.cur.execute("Delete from Student Where Email= ?",(Email,))      
        self.con.commit()

  

    def get_student_by_name(self,Email):

        self.cur.execute("Select * From Student where Email= ? ",(Email,))
        
        rec=self.cur.fetchall()
        for i in rec:
            print(i)







            