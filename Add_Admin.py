import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *


class Add_Admin:
    def __init__(self):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('Add Admin')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='ADD Admin',fg=self.framebackground,font=('Helvetica 12 bold',16,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form,text='Enter Name',font=('Helvetica 12 bold',12,'bold'))
        self.lb1.grid(row=0,column=0,padx=10,pady=10)

        self.txt1=tkinter.Entry(self.form,width=40,font=('Helvetica 12 bold',12,'bold'))
        self.txt1.grid(row=0,column=1,padx=10,pady=10)

        self.lb2 = tkinter.Label(self.form, text='Enter Email', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=1, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text='Enter Mobile', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb3.grid(row=2, column=0, padx=10, pady=10)

        self.txt3 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text='Enter Password', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb4.grid(row=3, column=0, padx=10, pady=10)

        self.txt4 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.form, text='Enter Role', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb5.grid(row=4, column=0, padx=10, pady=10)

        self.txt5 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.cb1=tkinter.ttk.Combobox(self.form,state='readonly',values=["Admin","Super-Admin"],width=40,height=2,font=('Helvetica 12 bold', 12, 'bold'))
        self.cb1.grid(row=4,column=1,padx=10,pady=10)

        self.btn=tkinter.Button(self.root,text='Submit', font=('Helvetica 12 bold', 12, 'bold'),command=self.AddAdmin)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def AddAdmin(self):
            conn = Connect()
            cr = conn.cursor()
            name=self.txt1.get()
            email=self.txt2.get()
            mobile=self.txt3.get()
            password=self.txt4.get()
            role=self.cb1.get()




            if verifyEmail(email) == True and verifyMobile(mobile)==True:
                q1=f"select*from admin_table where email='{email}'or mobile='{mobile}'"
                self.cr.execute(q1)
                result=self.cr.fetchall()
                print(result)
                if len(result)==0:

                    q = f"insert into admin_table values(null,'{name}','{email}','{mobile}','{password}','{role}')"
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo('Success','Added Succesfully')
                    self.reset()
                else:
                    msg.showwarning('Warning',' Email/Mobile Number already exists')
            else:
                msg.showwarning('Warning','Invalid Email/Mobile Number')



    def reset(self):
        self.txt1.delete(0,'end')
        self.txt2.delete(0,'end')
        self.txt3.delete(0,'end')
        self.txt4.delete(0,'end')
        self.cb1.set('')


#object=Add_Admin()

