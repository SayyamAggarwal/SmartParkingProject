import tkinter
import tkinter.ttk as ttk
import  tkinter.messagebox as msg
from connection import *

class Main:
    def __init__(self):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('Monthly Pass')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='Issue Monthly Pass',fg=self.framebackground,font=('Helvetica 12 bold',16,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form,text='Vehicle No.',font=('Helvetica 12 bold',12,'bold'))
        self.lb1.grid(row=0,column=0,padx=10,pady=10)

        self.txt1=tkinter.Entry(self.form,width=40,font=('Helvetica 12 bold',12,'bold'))
        self.txt1.grid(row=0,column=1,padx=10,pady=10)


        self.lb2 = tkinter.Label(self.form, text='Vehicle ID', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=1, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=1, column=1, padx=10, pady=10)


        self.lb3 = tkinter.Label(self.form, text='Pass ID', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb3.grid(row=2, column=0, padx=10, pady=10)

        self.txt3 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text='Issue Date of Pass', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb4.grid(row=3, column=0, padx=10, pady=10)

        self.txt4 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.form, text='Select Days For Pass', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb5.grid(row=4, column=0, padx=10, pady=10)

        self.txt5 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.cb1 = tkinter.ttk.Combobox(self.form, state='readonly', values=["10","20","30","40"], width=40, height=2,
                                        font=('Helvetica 12 bold', 12, 'bold'))
        self.cb1.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = tkinter.Label(self.form, text='Expiry Date of Pass', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb6.grid(row=5, column=0, padx=10, pady=10)

        self.txt7 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt7.grid(row=5, column=1, padx=10, pady=10)

        self.lb8 = tkinter.Label(self.form, text='Time of Pass Issue', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb8.grid(row=6, column=0, padx=10, pady=10)

        self.txt8 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt8.grid(row=6, column=1, padx=10, pady=10)

        self.btn2=tkinter.Button(self.root,text='Submit', font=('Helvetica 12 bold', 12, 'bold'))
        self.btn2.pack(pady=20)

        self.btn1 = tkinter.Button(self.form, text='Search', font=('Helvetica 12 bold', 12, 'bold'))
        self.btn1.grid(row=0, column=2, padx=20, pady=20)

        self.root.mainloop()

object=Main()

