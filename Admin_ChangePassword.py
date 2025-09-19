import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *


class AdminChangePassword:
    def __init__(self,email):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('ADMIN Login')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='ADMIN CHANGE PASSWORD',fg=self.framebackground,font=('Helvetica 12 bold',22,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form, text='Enter Email', font=('Helvetica 12 bold', 14, 'bold'))
        self.lb1.grid(row=1, column=0, padx=10, pady=10)

        self.txt1 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt1.grid(row=1, column=1, padx=10, pady=10)
        self.txt1.insert(0, email)
        self.txt1.config(state='readonly')
        self.lb2 = tkinter.Label(self.form, text='Enter Old Password', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=3, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=3, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text='Enter New Password', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb3.grid(row=5, column=0, padx=10, pady=10)

        self.txt3 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt3.grid(row=5, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text='Enter Confirm Password', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb4.grid(row=7, column=0, padx=10, pady=10)

        self.txt4 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt4.grid(row=7, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text='SUBMIT', font=('Helvetica 12 bold', 16, 'bold'),command=self.changepssword)

        self.btn.pack(pady=20)

        self.root.mainloop()

    def changepssword(self):
        email = self.txt1.get()
        password = self.txt2.get()
        newPassword = self.txt3.get()
        confirmPassword = self.txt4.get()

        q = f"select id,name,email,mobile,role from admin_table where email='{email}' and password='{password}'"
        self.cr.execute(q)
        result=self.cr.fetchone()
        if result is None:
            msg.showwarning(title='Warning',message='Invalid Email or Password',parent=self.root)
        else:
            if newPassword =="":
                msg.showerror(title='Error',message='Please fill new password',parent=self.root)
            elif password == newPassword:
                msg.showwarning(title='Warning',message='Password is same',parent=self.root)
            elif newPassword == confirmPassword:
                sql = f"update admin_table set password='{newPassword}' where email='{email}'"
                self.cr.execute(sql)
                self.conn.commit()
                msg.showinfo(title='Success',message='Password changed successfully',parent= self.root)
                self.root.destroy()

            else:
                msg.showerror(title='Error',message='Password not same',parent=self.root)







#object=AdminChangePassword()

