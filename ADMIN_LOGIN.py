import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *
import AdminDashboard


class Adminlogin:
    def __init__(self):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('LOGIN')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='LOGIN',fg=self.framebackground,font=('Helvetica 12 bold',26,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form, text='Enter Email', font=('Helvetica 12 bold', 14, 'bold'))
        self.lb1.grid(row=1, column=0, padx=10, pady=10)

        self.txt1 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt1.grid(row=1, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.form, text='Enter Password', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=3, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=3, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text='Login', font=('Helvetica 12 bold', 16, 'bold'),command=self.login)

        self.btn.pack(pady=20)

        self.root.mainloop()

    def login(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        if self.email == "" or self.password == "":
            msg.showerror(title='Error',message='Please fill all the fields',parent=self.root)

        else:
            q=f"select * from admin_table where password ='{self.password}' and email ='{self.email}'"
            self.cr.execute(q)
            result=self.cr.fetchall()
            if len(result)!=0:
                #msg.showinfo(title='Success',message='Admin login successfully',parent=self.root)
                self.root.destroy()
                AdminDashboard.Main(result)
            else:
                msg.showerror(title='Error',message='Wrong Information',parent=self.root)



        self.root.mainloop()


#object=Adminlogin()