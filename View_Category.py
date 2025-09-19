from tkinter import *
import tkinter.ttk as ttk
import  tkinter.messagebox as msg
from connection import *

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('View Category')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainbackground = '#462521'
        self.root.configure(background=self.mainbackground)

        self.mainLabel = Label(self.root, text="View Category", font=('Arial', 26, 'bold'))
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

        self.adminTable = ttk.Treeview(self.root, columns=['Name', 'Description'])
        self.adminTable.pack(pady=20, expand=True, fill='both', padx=30)
        self.adminTable.heading('Name', text='Name')
        self.adminTable.heading('Description', text='Description')
        self.adminTable['show'] = 'headings'

        style = ttk.Style()
        style.configure('Treeview', font=self.font, rowheight=40)
        style.configure('Treeview.Heading', font=self.font)

       

        self.getValues()

        self.root.mainloop()

    def getValues(self):
        q = "select Name, Description from category"
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
        q0 = f"select Name,Description from category where Name like '%{text}%' or Description like '%{text}%'"
        self.cr.execute(q0)
        result = self.cr.fetchall()
        for item in self.adminTable.get_children():
            self.adminTable.delete(item)
        index = 0
        for i in result:
            self.adminTable.insert('', index=index, values=i)
            index += 1

    def resetSearchForm(self):
        self.txt0.delete(0, 'end')
        self.getValues()




#object=Main()


