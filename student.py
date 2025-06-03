from db import connect
def student_menu(roll_no):
    while True:
        print("""\nStudent menu:
1.view details
2.view marks
3.view time table
4.Logout""")
        choice =int("enter choice:")

        if choice == '1':
            view_details(roll_no)
        elif choice == '2':
            view_marks(roll_no)
        elif choice == '3':
            view_timetable(roll_no)
        elif choice == '4':
            change_password(roll_no)
        else:
            print("inavlid choice.")

def view_details(roll):
    con=get_connection()
    cur=con.cursor
    cur.execute("SELECT * FROM students roll_no=%s",(roll,))
    print("Student Details:")
    print(cur.fetchdone())
    con.close()
    print("password changed.")
def view marks(roll):
    con=get_coonection()
    cur=con.cursor()
    cur.execute("SELECT subject,marks FROM marks WHERE roll_no=%s",(roll_no,))
    for row in cur.fetchall():
        print(row)
    con.close() 

    def view_timetable(roll):
        con=get_connection()

        

    
    
    
    
    
    
    
    
 