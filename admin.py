'''
1.add student
2.delete student
3.update student
4.time table
5.marks

'''
from db import connect

def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""\nAdmin Menu:
    1.Add student
    2.update student details
    3.reset student password
    4.update marks
    5.view all students
    6.update time table
    7.logout""")
    ch=int(input("enter your choice:"))
    if ch==1:
        add_student()
    elif ch==2:
        update_student()
    elif ch==3:
        reset_student_password()
    elif ch==4:
        update_marks()
    elif ch==5:
        view_all_students()
    else:
        print("invalid choice.please try again")
def add_student():
    con=connect()
    cursor=con.cursor()
    roll_no=input("enter roll no:")        
    name=input("enter name:")
    class_name=input("enter class:")
    section=input("enter section")
    password="password@123"
    email=input("enter email:")
    query="INSERT INTO students(roll_no,name,class,section,password,email) values(%s,%s,%s,%s,%s,%s)"
    values=(roll_no,name,class_name,section,password,email)
    cursor.execute(query,values)
    con.commit()
def update_student():
    con=connect()
    cursor=con.cursor()
    roll_no=input("enter roll no:")        
    name=input("enter name:")
    class_name=input("enter class:")
    section=input("enter section")
    password="password@123"
    email=input("enter email:")
    query="UPDATE students SET name=%s,class=%s,section=%s,email=%s WHERE roll_no=%s"
    values=(name,class_name,section,email,roll_no)
    cursor.execute(query,values)
    con.commit()    
    print("student details updated successfully.")
def reset_student_password():
    pass
def update_marks():
    conn=connect()
    cursor=con.cursor()
    roll_no=input("enter roll no of the studemt to update")
    subject=input("enter subject:")
    marks=input("enter marks:")
    query="UPDATE students SET ,marks=%s WHERE roll_no=%s AND subject=%s"
    values=(marks,roll_no,subject)
    cursor.execute(query,values)
    conn.commit()
    print ("Marks updated successfully")
def view_all_students():
    con=connect()
    cursor=con.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
def update_timetable():
    pass
def logout():
    print("logging out...")
    #here you can add any additional logout logic
    return 
if __name__=="__main__":
    admin()                              