import sqlite3 as lite
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

cur = lite.connect('register.db') # This is used to determine the section needed in the database
con=cur.cursor() # This is used to add data to the selected section


def customeradd():
        customeradd=Tk() #Sets the name of the window
        customeradd.title("Add a customer") #Sets the window heading
        customeradd.geometry("500x500") #Sets the window size

        #These two lines create a label to describe the first textbox
        lbl2=Label(customeradd, text="Surname?", font=("Arial", 12))
        lbl2.place(x=40, y=30, height=75, width=200)

        #These two lines create a textbox to enter the Surname
        txt1=Entry(customeradd, font=("Arial", 12))
        txt1.place(x=270, y=55, height=50, width=200)

        #These two lines create a label to describe the second textbox
        lbl3=Label(customeradd, text="First name?", font=("Arial", 12))
        lbl3.place(x=40, y=105, height=75, width=200)

        txt2=Entry(customeradd, font=("Arial", 12))
        txt2.place(x=270, y=120, height=50, width=200)

        tree=ttk.Treeview(customeradd) #States that the tree is a Treeview type to be used in this window
        tree["columns"]=("two","three") #Creates the columns for the tree

        #Each column has to specify its size and the heding of the column
        tree.column("two", width=90)
        tree.column("three", width=90)
        tree.column("#0", width=90)
        tree.heading("#0", text="MembershipID")
        tree.heading("two", text="Membership")
        tree.heading("three",text="Cost")
        tree.place(x=60, y=180, height=100, width=360) # Determines the overall size of the tree and where it will be placed

        itemlist=[]
        item=1
        for row in con.execute("SELECT * FROM Memberships"):
                item+=1
                itemlist.append(item-1)


        for i in range(1, item):
                con.execute("SELECT MembershipName FROM Memberships WHERE MembershipID=?", (i,))
                Name=con.fetchone()[0]
                con.execute("SELECT MembershipCost FROM Memberships WHERE MembershipID=?", (i,))
                cost=con.fetchone()[0]

                tree.insert("", i, text=i, values=(Name, cost))
        
        lbl4=Label(customeradd, text="Membership?", font=("Arial", 12))
        lbl4.place(x=40, y=280, height=75, width=200)

        combo2 = ttk.Combobox(customeradd, font=("Arial", 12), state='normal', value=itemlist)
        combo2.place(x=270, y=290, height=50, width=200)
        

        lbl6=Label(customeradd, text="Select Session", font=("Arial", 12))
        lbl6.place(x=40, y=375, height=50, width=200)

        listsessionName=[]
        item=1
        
        for row in con.execute("SELECT * FROM Sessions"):
                item+=1
                
        for i in range(1, item):
                con.execute("SELECT SessionName FROM Sessions WHERE SessionID =?", (i,))
                name = con.fetchone()[0]
                listsessionName.append(name)
                
        print(listsessionName)
        combo = ttk.Combobox(customeradd, font=("Arial", 12), state='normal', value=listsessionName)
        combo.place(x=270, y=375, height=50, width=200)

        def confirm():

                #A recursive process that finds the length of the entity, to be used as the latest id
#                 x = con.execute("SELECT LAST(CustomerID) FROM Customers")

                # Always define Primary Keys with AUTOINCREMENT option!!
                item = con.execute("SELECT * FROM Customers ORDER BY CustomerID DESC LIMIT 1;")
                item = item.fetchone()
                try:
                    item = item[0]+1
                except:
                    item = 0
                Id=item 
                Surname=txt1.get() #Retrieves the first textbox value
                Firstname=txt2.get() #retrieves the second textbox vallue
                MembershipID=combo2.get() #Retrieves the third textbox value
                SessionID = combo.get()

                con.execute("SELECT SessionID from Sessions WHERE SessionName =?", (SessionID,))
                sesh = con.fetchone()[0]
                new=[Id, Surname, Firstname, MembershipID, sesh] #All the data retrieved is placed into a list to make it easier to enter
                con.execute("INSERT INTO Customers VALUES(?,?,?,?,?)" ,new) #The list is entered into the database
                cur.commit() # This saves the data from the previous SQLite code into the database
                messagebox.showinfo(customeradd, "Customer added") #Alerts the user that the data has been entered
                customeradd.destroy()

        #The code for the back button is the same as last time, except the button leads to the previous window
        # insted of logging out of the program
        btn1=Button(customeradd, justify=LEFT)
        btn1.place(bordermode=OUTSIDE, height=50, width=50)
        
        #These three lines create and place a silver confirm button, which leads to confirming the data
        btn2=Button(customeradd, text="Confirm", font=("Arial", 12), background="Silver", foreground="Red", command=confirm)
        btn2.place(x=200, y=450, height=50, width=100)

customeradd()

class CustomerImplementation:
    connection = None
    c = None
    def __init__(self, master):
        # construct of the main window
        self.text = Label(master, text="Delete Session")
        self.text.pack()
        self.text["text"] = "       DELETE Customer AND BOOKING"

#         name_label = Label(master, text = "Name")
#         name_label.pack()
#         
#         self.nameField = Entry(master, text = "Name", width=50)
#         self.nameField.insert(0, "Enter Name")
#         self.nameField.pack()
# 
#         name_label = Label(master, text = "Details")
#         name_label.pack()
# 
#         self.ageField = Entry(master, text = "age", width=30)
#         self.ageField.insert(0, "Enter Age")
#         self.ageField.pack()
# 
# 
#         self.dayOfVisit = Entry(master, text = "Day of Visit", width=30)
#         self.dayOfVisit.insert(0, "Day of Visit")
#         self.dayOfVisit.pack()
#         
#         self.dayOfLeave = Entry(master, text = "Day of leave", width=30)
#         self.dayOfLeave.insert(0, "Day of leave")
#         self.dayOfLeave.pack()
# 
#         self.btn=Button(master, text='Add', command=self.add_customer_info)
#         self.btn.pack()
# 
        self.reloadbtn = Button(master, text='Reload list', command=self.reload_list)
        self.reloadbtn.pack()
#         
#         self.showbtn = Button(master, text='Update selected', command=self.update_selected)
#         self.showbtn.pack()

        self.delbtn = Button(master, text='Delete all', command=self.del_all_notes)
        self.delSelectedbtn = Button(master, text='Delete selected', command=self.del_selected)

        self.delbtn.pack()
        self.delSelectedbtn.pack()
       
        self.content=Listbox(master, width=50)
        self.content.pack()

        # open database
        self.connect_db(db_name = 'register.db')
        self.initial_listBox()

    def connect_db(self, db_name):
        self.conn = lite.connect(db_name)
        self.c = self.conn.cursor()
        # create table
#         self.c.execute('''CREATE TABLE IF NOT EXISTS people(name TEXT primary key, age TEXT, dayOfVisit TEXT, dayOfLeave TEXT)''')
        self.conn.commit()

    def initial_listBox(self):
        # read people
        c = self.conn.cursor()
        people = c.execute("SELECT * FROM Customers")
        self.conn.commit()

        # add to list
        for person in people:
            self.content.insert(END, person)
        self.c.close()
        
    def reload_list(self):
        self.content.delete(0,END)
        self.initial_listBox()

    def clearNameField(self, event):
        self.nameField.delete(0,END)

    def clearAgeField(self, event):
        self.ageField.delete(0,END)

    def cleardayOfVisit(self, event):
        self.dayOfVisit.delete(0,END)

    def clearFbField(self, event):
        self.fbField.delete(0,END)
        
    def add_customer_info(self):
        if self.nameField.get() == "":
            self.text["text"] = "Please type something"
        else:
            name = self.nameField.get()
            age = self.ageField.get()
            dayOfVisit = self.dayOfVisit.get()
            dayOfLeave = self.dayOfLeave.get()
            self.nameField.delete(0, END)
            self.ageField.delete(0, END)
            self.dayOfVisit.delete(0, END)
            self.dayOfLeave.delete(0, END)

            c = self.conn.cursor()

            c.execute("INSERT INTO people VALUES (?, ?, ?, ?)", (name, age, dayOfVisit, dayOfLeave))
            self.conn.commit()
            c.close()

            # add to list
            self.content.insert(END, (name, age, dayOfVisit, dayOfLeave))

    def update_selected(self):
        person = self.content.get(ACTIVE)
        name_search, age_search, dayOfVisit_search, dayOfLeave_search = self.content.get(ACTIVE)
        if self.nameField.get() == "":
            self.text["text"] = "Please type something"
        else:
            name = self.nameField.get()
            age = self.ageField.get()
            dayOfVisit = self.dayOfVisit.get()
            dayOfLeave = self.dayOfLeave.get()
            self.nameField.delete(0, END)
            self.ageField.delete(0, END)
            self.dayOfVisit.delete(0, END)
            self.dayOfLeave.delete(0, END)

        # delete in database
        c = self.conn.cursor()
        c.execute("UPDATE people SET name = ? ,age = ? WHERE name= ? and dayOfVisit=? and dayOfLeave=? ", (name, age, name, dayOfVisit, dayOfLeave))
        self.conn.commit()
        c.close()
        self.reload_list()

    def del_all_notes(self):
        # get selected person       
        c = self.conn.cursor()

        people = self.content.get(0, END)
        if len(people):
            for customerID,surname,firstname,membershipid, sessionid in people:
                # delete all from database
                c.execute("DELETE FROM Customers WHERE  CustomerID=? and Surname=? and FirstName=? and MembershipID=? and SessionID=?", (customerID, surname, firstname, membershipid, sessionid))
                self.conn.commit()
        c.close()
        
        # delete on list
        self.content.delete(0,END)
        
    def del_selected(self):
        # get selected person       
        person = self.content.get(ACTIVE)
        customerID,surname,firstname,membershipid, sessionid = self.content.get(ACTIVE)
        # delete in database
        c = self.conn.cursor()
        c.execute("DELETE FROM Customers WHERE CustomerID=? and Surname=? and FirstName=? and MembershipID=? and SessionID=?", (customerID, surname, firstname, membershipid, sessionid))
        self.conn.commit()
        c.close()
        

        # delete on list
        self.content.delete(ANCHOR)



root = Tk()
CustomerImplementation(root)
root.mainloop()