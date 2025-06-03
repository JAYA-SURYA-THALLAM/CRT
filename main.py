from db import connection
conn=connection()
if conn:
    print("Connection established succesfully")
else:
    print("Connection failed") 

    roll_no=int(input("enter roll.no:"))       
    name=int(input("enter name:"))
    branch=input(("enter branch:"))

    cursor=conn.cursor()
    query="insert into Student(roll_no,name,branch) values(%s,%s,%s)"
    values =(roll_no,name,branch)
    cursor.execute(query,values)
    conn.commit()
    print("Data inserted succesfully")
def fetch_data():
    cursor=conn.cursor()
    query="select * from Student"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)

def update_data():
    roll_no=int(input("enter roll.no:"))       
    name=int(input("enter name:"))
    branch=input(("enter branch:")) 
    cursor=conn.cursor()
    query="update Student set name=%s,branch=%s where roll_no=%s"
    values=(name,branch,roll_no)
    cursor.execute(query,values)
    conn.commit()
    print("Data updated succesfully") 

    #while loop to perform operations

    print("1.Insert Data")
    print("2.Fetch Data")
    print("3.update Data")
    print("enter 4 to exit")
    while True:
        choice=int(input("enter yor choice(1-4):")) 
        if choice ==1:
            insert_data()
        elif choice ==2:
            fetch_data()
        elif choice==3:
            update_data()
        elif choice==4:
            print("Exiting...") 
            

            













    
   