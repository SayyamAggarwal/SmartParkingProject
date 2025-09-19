from tkinter import *
import tkinter.ttk as ttk
import  tkinter.messagebox as msg
from connection import *

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('ENTRY')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainbackground = '#462521'
        self.root.configure(background=self.mainbackground)

        self.mainLabel = Label(self.root, text="View Entry", font=('Arial', 26, 'bold'))
        self.mainLabel.pack(pady=20)

        self.font = ('Arial', 14)

        self.searchFrame = Frame(self.root)

        self.lb0 = Label(self.searchFrame, text="SEARCH:", font=self.font)
        self.txt0 = Entry(self.searchFrame, font=self.font, width=40)
        self.searchBtn = Button(self.searchFrame, text="Search", font=self.font, command=self.searchAdmin)
        self.resetBtn = Button(self.searchFrame, text="Reset", font=self.font, command=self.resetSearchForm)
        self.lb0.grid(row=0, column=0, padx=10, pady=10)
        self.txt0.grid(row=0, column=1, padx=10, pady=10)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=10)
        self.resetBtn.grid(row=0, column=3, padx=10, pady=10)

        self.searchFrame.pack(pady=20)

        self.adminTable = ttk.Treeview(self.root, columns=['id','vehicle_number','vehicle_id','date','time', 'admin_id','amount'])
        self.adminTable.pack(pady=20, expand=True, fill='both', padx=30)
        self.adminTable.heading('id', text='ID')
        self.adminTable.heading('vehicle_number', text='Vehicle No.')
        self.adminTable.heading('vehicle_id', text='VEHICLE ID')
        self.adminTable.heading('date', text='DATE')
        self.adminTable.heading('time', text='TIME')
        self.adminTable.heading('admin_id', text='ADMIN ID')
        self.adminTable.heading('amount', text='AMOUNT')

        self.adminTable['show'] = 'headings'

        style = ttk.Style()
        style.configure('Treeview', font=self.font, rowheight=40)
        style.configure('Treeview.Heading', font=self.font)

        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.getValues()

        self.root.mainloop()

    def getValues(self):
        q = "select id,vehicle_number, vehicle_id, date, time, admin_id, amount from entry"
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
        q0 = f"select id,vehicle_number, vehicle_id, date, time, admin_id, amount from entry where vehicle_id like '%{text}%' or admin_id like '%{text}%' or date like '%{text}%'"
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

        self.mainLabel2 = Label(self.root1, text="Update/Delete Admin", font=('Arial', 18, 'bold'))
        self.mainLabel2.pack(pady=20)

        self.formFrame = Frame(self.root1)
        self.formFrame.pack(pady=20)

        self.font = ("Arial", 14)

        self.lb1 = Label(self.formFrame, text="Enter Vehicle ID", font=self.font)
        self.txt1 = Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, padx=1, pady=1)
        self.txt1.grid(row=0, column=1, padx=1, pady=1)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.formFrame, text="Enter Date", font=self.font)
        self.txt2 = Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, padx=1, pady=1)
        self.txt2.grid(row=1, column=1, padx=1, pady=1)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.formFrame, text="Enter Time", font=self.font)
        self.txt3 = Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, padx=1, pady=1)
        self.txt3.grid(row=2, column=1, padx=1, pady=1)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.formFrame, text="Enter Admin ID", font=self.font)
        self.txt4 = Entry(self.formFrame, font=self.font)
        self.lb4.grid(row=3, column=0, padx=1, pady=1)
        self.txt4.grid(row=3, column=1, padx=1, pady=1)
        self.txt4.insert(0, data[4])

        self.lb5 = Label(self.formFrame, text=" ID", font=self.font)
        self.txt5 = Entry(self.formFrame, font=self.font)
        self.lb5.grid(row=4, column=0, padx=1, pady=1)
        self.txt5.grid(row=4, column=1, padx=1, pady=1)
        self.txt5.insert(0, data[0])
        self.txt5.config(state='readonly')

        self.lb6 = Label(self.formFrame, text=" Enter Amount", font=self.font)
        self.txt6 = Entry(self.formFrame, font=self.font)
        self.lb6.grid(row=5, column=0, padx=1, pady=1)
        self.txt6.grid(row=5, column=1, padx=1, pady=1)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.formFrame, text=" Enter Vehicle No.", font=self.font)
        self.txt7 = Entry(self.formFrame, font=self.font)
        self.lb7.grid(row=5, column=0, padx=1, pady=1)
        self.txt7.grid(row=5, column=1, padx=1, pady=1)
        self.txt7.insert(0, data[6])



        self.updateBtn = Button(self.root1, text="Update", font=self.font, command=self.updateAdmin)
        self.deleteBtn = Button(self.root1, text="Delete", font=self.font, command=self.deletAdmin)
        self.updateBtn.pack(pady=1)
        self.deleteBtn.pack(pady=1)

        self.root1.mainloop()

    def updateAdmin(self):
        id = self.txt5.get()
        vehicle_number=self.txt7.get()
        vehicle_id = self.txt1.get()
        date = self.txt2.get()
        time = self.txt3.get()
        admin_id = self.txt4.get()
        amount = self.txt6.get()


        if vehicle_id == "" or date == "" or time == "" or admin_id == "" or amount =="" :
            msg.showwarning("Warning", "Please fill all fields", parent=self.root1)
        else:

            q2 = f"update entry set vehicle_number='{vehicle_number}', vehicle_id='{vehicle_id}', date='{date}',time='{time}', admin_id='{admin_id}',amount='{amount}' where id={id}"
            self.cr.execute(q2)
            self.conn.commit()
            self.root1.destroy()
            msg.showinfo("Success", "Admin successfully updated")
            self.getValues()

    def deletAdmin(self):
        id = self.txt4.get()
        q4 = f"delete from entry where id='{id}'"
        self.cr.execute(q4)
        self.conn.commit()
        self.root1.destroy()
        msg.showinfo("Success", "Admin successfully deleted")
        self.getValues()

#obj = Main()