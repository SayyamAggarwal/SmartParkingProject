import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *


class Add_Category:
    def __init__(self):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('Add Category')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='ADD Category',fg=self.framebackground,font=('Helvetica 12 bold',26,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form,text='Enter Name',font=('Helvetica 12 bold',14,'bold'))
        self.lb1.grid(row=1,column=0,padx=10,pady=10)

        self.txt1=tkinter.Entry(self.form,width=40,font=('Helvetica 12 bold',12,'bold'))
        self.txt1.grid(row=1,column=1,padx=10,pady=10)

        self.lb2 = tkinter.Label(self.form, text='Enter Description', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=3, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=3, column=1, padx=10, pady=10)


        self.btn=tkinter.Button(self.root,text='Submit', font=('Helvetica 12 bold', 12, 'bold'),command=self.AddCategory)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def AddCategory(self):
            conn = Connect()
            cr = conn.cursor()
            Name=self.txt1.get()
            Description=self.txt2.get()

            q = f"insert into category values('{Name}','{Description}')"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo('Success', 'Added Succesfully')
            self.reset()


    def reset(self):
        self.txt1.delete(0,'end')
        self.txt2.delete(0,'end')

#object=Add_Category()

