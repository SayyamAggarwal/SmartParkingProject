from tkinter import *
import tkinter.ttk as ttk
import  tkinter.messagebox as msg
from connection import *

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('PARKING PLAZA')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainbackground = '#462521'
        self.root.configure(background=self.mainbackground)

        self.mainLabel = Label(self.root, text="View Parking Plaza", font=('Arial', 26, 'bold'))
        self.mainLabel.pack(pady=20)

        self.font = ('Arial', 14)

        self.searchFrame = Frame(self.root)

        self.lb0 = Label(self.searchFrame, text="Enter Text", font=self.font)
        self.txt0 = Entry(self.searchFrame, font=self.font, width=40)
        self.searchBtn = Button(self.searchFrame, text="Search", font=self.font, command=self.searchAdmin)
        self.resetBtn = Button(self.searchFrame, text="Reset", font=self.font, command=self.resetSearchForm)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=10)
        self.resetBtn.grid(row=0, column=3, padx=10, pady=10)

        self.searchFrame.pack(pady=20)

        self.adminTable = ttk.Treeview(self.root, columns=['id','name', 'email','password','mobile','location','status'])
        self.adminTable.pack(pady=20, expand=True, fill='both', padx=30)
        self.adminTable.heading('id', text='ID')
        self.adminTable.heading('name', text='Name')
        self.adminTable.heading('email', text='Email')
        self.adminTable.heading('password', text='PASSWORD')
        self.adminTable.heading('mobile', text='MOBILE')
        self.adminTable.heading('location', text='LOCATION')
        self.adminTable.heading('status', text='STATUS')
        self.adminTable['show'] = 'headings'

        style = ttk.Style()
        style.configure('Treeview', font=self.font, rowheight=40)
        style.configure('Treeview.Heading', font=self.font)

        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.getValues()

        self.root.mainloop()

    def getValues(self):
        q = "select id, name, email, password, mobile, location ,status from parking_plaza"
        self.cr.execute(q)
        result = self.cr.fetchall()
        for item in self.adminTable.get_children():
            self.adminTable.delete(item)
        index = 0
        for i in result:
            self.adminTable.insert('', index=index, values=i)
            index += 1

    def searchAdmin(self):
        text = self.txt0.get()
        q0 = f"select id, name, email,password, mobile, location, status from parking_plaza where name like '%{text}%' or email like '%{text}%' or mobile like '%{text}%'"
        self.cr.execute(q0)
        result = self.cr.fetchall()
        for item in self.adminTable.get_children():
            self.adminTable.delete(item)
        index = 0
        for i in result:
            self.adminTable.insert('', index=index, values=i)
            index += 1

    def resetSearchForm(self):
        self.txt0.delete(0, END)
        self.getValues()

    def openUpdateWindow(self, e):
        id = self.adminTable.selection()[0]
        metadata = self.adminTable.item(id)
        data = metadata['values']
        print(data)

        self.root1 = Toplevel()
        self.root1.geometry('700x500')

        self.mainLabel2 = Label(self.root1, text="Update/Delete Admin", font=('Arial', 24, 'bold'))
        self.mainLabel2.pack(pady=20)

        self.formFrame = Frame(self.root1)
        self.formFrame.pack(pady=20)

        self.font = ("Arial", 14)

        self.lb1 = Label(self.formFrame, text="Enter Name", font=self.font)
        self.txt1 = Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.formFrame, text="Enter Email", font=self.font)
        self.txt2 = Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.formFrame, text="Enter Password", font=self.font)
        self.txt3 = Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.formFrame, text="Enter Mobile", font=self.font)
        self.txt4 = Entry(self.formFrame, font=self.font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[4])

        self.lb5 = Label(self.formFrame, text=" ID", font=self.font)
        self.txt5 = Entry(self.formFrame, font=self.font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[0])
        self.txt5.config(state='readonly')

        self.lb6 = Label(self.formFrame, text=" Enter Location", font=self.font)
        self.txt6 = Entry(self.formFrame, font=self.font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])


        self.lb7 = Label(self.formFrame, text="Select Status", font=self.font)
        self.txt7 = ttk.Combobox(self.formFrame, font=self.font, values=['Super Admin', 'Admin'], state='readonly')
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.set(data[6])

        self.updateBtn = Button(self.root1, text="Update", font=self.font, command=self.updateAdmin)
        self.deleteBtn = Button(self.root1, text="Delete", font=self.font, command=self.deletAdmin)
        self.updateBtn.pack(pady=10)
        self.deleteBtn.pack(pady=10)

        self.root1.mainloop()

    def updateAdmin(self):
        id = self.txt5.get()
        name = self.txt1.get()
        email = self.txt2.get()
        password = self.txt3.get()
        mobile = self.txt4.get()
        location = self.txt6.get()
        status = self.txt7.get()

        if name == "" or email == "" or mobile == "" or password == "" or location =="" or status =="":
            msg.showwarning("Warning", "Please fill all fields", parent=self.root1)
        else:
            if verifyMobile(mobile) == True and verifyEmail(email) == True:
                q2 = f"update parking_plaza set name='{name}', email='{email}',password='{password}', mobile='{mobile}', location='{location}',status='{status}' where id={id}"
                self.cr.execute(q2)
                self.conn.commit()
                self.root1.destroy()
                msg.showinfo("Success", "Admin successfully updated")
                self.getValues()
            else:
                msg.showwarning("Warning", "Invalid Email or Mobile Number", parent=self.root1)

    def deletAdmin(self):
        id = self.txt4.get()
        q4 = f"delete from parking_plaza where id='{id}'"
        self.cr.execute(q4)
        self.conn.commit()
        self.root1.destroy()
        msg.showinfo("Success", "Admin successfully deleted")
        self.getValues()

#obj = Main()