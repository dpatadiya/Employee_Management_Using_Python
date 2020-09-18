import sqlite3

class Record:
    
    def __init__(self):

        try:
            self.con=sqlite3.connect("stud.db")
        except:
            pass

        self.cur=self.con.cursor()

        try:
            self.cur.execute("Create table Student(roll integer primary key autoincrement,enrollment text,Firstname text,Lastname text,Branch text,enrollmentyear text,email text)")
            self.con.commit()
        except:
            pass

  
    def add_record(self,eenrollment,efname,elname,ebranch,eenrollmentyear,eemail):

        self.cur.execute("Insert into Student(enrollment,Firstname,Lastname,Branch,enrollmentyear,email) values (?,?,?,?,?,?)",(eenrollment,efname,elname,ebranch,eenrollmentyear,eemail)) 
        self.con.commit()


    def display_all(self):
        self.cur.execute("select * from Student")
    
        rec = self.cur.fetchall()
        for i in rec:
            print(i)

    def get_student_by_name(self,last):

        self.cur.execute("Select * From Student where lastname= ? ",(last,))
        
        rec=self.cur.fetchall()
        for i in rec:
            print(i)

    def remove_by_enrollment(self,enroll):

        self.cur.execute("DELETE From Student where enrollment=?", (enroll,))
        self.con.commit()