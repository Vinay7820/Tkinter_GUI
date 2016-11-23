import Tkinter
import tkMessageBox
from Tkinter import *
import MySQLdb

top = Tkinter.Tk()
top.title("Aricent")

def savepressed():
    name = E1.get()
    mob = E2.get()
    email = E3.get()
    city = E4.get()
    
    print("Please Wait while inserting the data into database")
    import MySQLdb
    # Open database connection
    db = MySQLdb.connect("localhost","testuser","tkinter1","test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    #cursor.execute("DROP TABLE IF EXISTS DETAILS")

     #Create table as per requirement
    #sql = """CREATE TABLE DETAILS(ID INT AUTO_INCREMENT PRIMARY KEY, User_Name VARCHAR(20),
    #Mob_No VARCHAR(20),Email_id VARCHAR(20),
    #City VARCHAR(20) )"""
    #cursor.execute(sql)
    #print("Table Created")


    #sql = """INSERT INTO DETAILS(User_Name, 
    #Mob_No, Email_id, City)
    #VALUES('Vinay', '9036728732', 'vinay.m@aricent.com', 'Bangalore'),
    #('Samana', '123456789', 'samana.m@aricent.com', 'Tumkur'),
    #('Yadu', '9535082227', 'yadu.k@aricent.com', 'Bangalore')"""


    
    sql = "INSERT INTO DETAILS(User_Name, Mob_No, Email_id, City) VALUES ('%s','%s','%s','%s')" %(name, mob, email, city)

    try:
        cursor.execute(sql)
# Commit your changes in the database
        db.commit()
        print("Completed")
    except Exception as e:
# Rollback in case there is any error
        db.rollback()
        print(e)

    db.close()




def newuserpressed():
    global nameVar, mobVar, cityVar, idVar
    global E1, E2, E3, E4
    top1 = Tkinter.Tk()

    
    L1 = Label(top1, text="User Name :")
    nameVar = StringVar()
    L1.grid(row=0, column=0, sticky=E)
    E1 = Entry(top1, textvariable=nameVar, bd=5)
    E1.grid(row=0, column=1)

    L2 = Label(top1, text="Mob-No : ")
    mobVar = StringVar()
    L2.grid(row=1, column=0, sticky=E)
    E2 = Entry(top1, textvariable=mobVar, bd=5)
    E2.grid(row=1, column=1)

    L3 = Label(top1, text="Email Address :")
    idVar = StringVar()
    L3.grid(row=2, column=0, sticky=E)
    E3 = Entry(top1, textvariable=idVar, bd=5)
    E3.grid(row=2, column=1)

    L4 = Label(top1, text="City : ")
    cityVar = StringVar()
    L4.grid(row=3, column=0, sticky=E)
    E4 = Entry(top1, textvariable=cityVar, bd=5)
    E4.grid(row=3, column=1)


    S1 = Tkinter.Button(top1, text="SAVE", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=8,
                    command=savepressed)
    S2 = Tkinter.Button(top1, text="CANCEL", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=8,
                    command=top1.destroy)
    S1.grid(row=4, column=0)
    S2.grid(row=4, column=1)

    
    top1.mainloop()

def whichSelected():
    return int(Lb1.curselection()[0])



def updatepressed():
    #!/usr/bin/python
    
    nameq = nameVar.get()
    mobq = mobVar.get()
    emailq = idVar.get()
    cityq = cityVar.get()

    import MySQLdb
    id = (results[whichSelected()][0])
    print(id)

    # Open database connection
    db = MySQLdb.connect("localhost","testuser","tkinter1","test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = (("""
       UPDATE DETAILS
       SET User_Name='%s', Mob_No='%s', Email_id='%s', City='%s'
       WHERE ID = '%d'""") % (nameq, mobq, emailq, cityq, id))

    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
       print("Database Updated Succesfully")
    except Exception as e:
       # Rollback in case there is any error
       db.rollback()
       print(e)

    # disconnect from server
    db.close()


    
def changepressed():
    global E1, E2, E3, E4
    global nameVar, mobVar, cityVar, idVar
    top3 = Tkinter.Tk()
    L1 = Label(top3, text="User Name :")
    nameVar = StringVar()
    #L1.pack(side=LEFT)
    L1.grid(row=0, column=0, sticky=E)
    E1 = Entry(top3, textvariable=nameVar, bd=5)
    nameVar.set(Name)
    #E1.pack()
    E1.grid(row=0, column=1)

    L2 = Label(top3, text="Mob-No : ")
    mobVar = StringVar()
    #L2.pack(side=LEFT)
    L2.grid(row=1, column=0, sticky=E)
    E2 = Entry(top3, textvariable=mobVar, bd=5)
    mobVar.set(Mob_No)
    #E2.pack()
    E2.grid(row=1, column=1)

    L3 = Label(top3, text="Email Address :")
    idVar = StringVar()
    #L3.pack(side=LEFT)
    L3.grid(row=2, column=0, sticky=E)
    E3 = Entry(top3, textvariable=idVar, bd=5)
    idVar.set(Email_id)
    #E3.pack()
    E3.grid(row=2, column=1)

    L4 = Label(top3, text="City : ")
    cityVar = StringVar()
    #L4.pack(side=LEFT)
    L4.grid(row=3, column=0, sticky=E)
    E4 = Entry(top3, textvariable=cityVar, bd=5)
    cityVar.set(City)
    #E4.pack()
    E4.grid(row=3, column=1)

    p1 = Tkinter.Button(top3, text="UPDATE", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=8,
                    command=updatepressed)
    p2 = Tkinter.Button(top3, text="CANCEL", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=8,
                    command=top3.destroy)
    p1.grid(row=4, column=0)
    p2.grid(row=4, column=1)


    top3.mainloop()
    
def listpressed():
    top2 = Tkinter.Tk()
    global Name, Mob_No, Email_id, City, Lb1

    import MySQLdb
    global results
    # Open database connection
    db = MySQLdb.connect("localhost","testuser","tkinter1","test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    sql = "SELECT * FROM DETAILS"
    try:
        cursor.execute(sql)
    
        results = cursor.fetchall()
        for row in results:
            
            Name = row[1]
            Mob_No = row[2]
            Email_id = row[3]
            City = row[4]


            Lb1 = Listbox(top2, height = 2)
            Lb1.insert(1, Name)
            Lb1.pack()
            
        
# Now print fetched result
            print "Name=%s, Mob_No=%s, Email_id =%s, City=%s" % (Name, Mob_No, Email_id, City)

        
    except Exception as e:
        print(e)
        print "Error: unable to fecth data"

# disconnect from server
    db.close()

    A1 = Tkinter.Button(top2, text="CHANGE", activebackground="Blue", activeforeground="red", bd=5, relief="ridge",
                        width=8, command=changepressed)
    A2 = Tkinter.Button(top2, text="CANCEL", activebackground="Blue", activeforeground="red", bd=5, relief="ridge",
                        width=8, command=top2.destroy)
    A1.pack(side=LEFT, padx=10)
    A2.pack(side=LEFT, padx=10)

    



B1 = Tkinter.Button(top, text="LIST_USERS", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=15,
                    command=listpressed)
B2= Tkinter.Button(top, text="NEW_USER", activebackground="Blue", activeforeground="red", bd=5, relief="ridge", width=15,
                    command=newuserpressed)

l2 = Label(top, text="Click Me! to Insert new account-->")
l1 = Label(top, text="Click Me! to show Customer Details -->")

B1.grid(row=0, column=1)
B2.grid(row=1, column=1)
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

top.mainloop()
