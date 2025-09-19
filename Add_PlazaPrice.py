import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *


class Add_ParkingPlaza:
    def __init__(self):
        self.mainbackground = '#462521'
        self.framebackground = '#8A6552'
        self.root=tkinter.Tk()
        self.root.title('PLAZA PRICE')
        self.root.state('zoomed')

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.root.configure(background=self.mainbackground)

        self.mainLabel = tkinter.Label(self.root,text='PLAZA PRICE',fg=self.framebackground,font=('Helvetica 12 bold',16,'bold'))

        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.framebackground)
        self.form.pack()

        self.lb1 = tkinter.Label(self.form,text='Enter Price',font=('Helvetica 12 bold',12,'bold'))
        self.lb1.grid(row=0,column=0,padx=10,pady=10)

        self.txt1=tkinter.Entry(self.form,width=40,font=('Helvetica 12 bold',12,'bold'))
        self.txt1.grid(row=0,column=1,padx=10,pady=10)

        self.lb2 = tkinter.Label(self.form, text='Enter Description', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb2.grid(row=1, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        self.txt2.grid(row=1, column=1, padx=10, pady=10)


        self.lb3 = tkinter.Label(self.form, text='CATEGORY NAME', font=('Helvetica 12 bold', 12, 'bold'))
        self.lb3.grid(row=2, column=0, padx=10, pady=10)

        # self.txt3 = tkinter.Entry(self.form, width=40, font=('Helvetica 12 bold', 12, 'bold'))
        # self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.cb1 = tkinter.ttk.Combobox(self.form, state='readonly', values=self.getValusCategory(),width=40, height=2, font=('Helvetica 12 bold', 12, 'bold'))
        self.cb1.grid(row=2,column=1,padx=10,pady=10)

        self.btn=tkinter.Button(self.root,text='Submit', font=('Helvetica 12 bold', 12, 'bold'),command=self.AddParkingPlaza)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def getValusCategory(self):
        q=f"select * from category"
        self.cr.execute(q)
        reult=self.cr.fetchall()
        list=[]
        for i in reult:
            list.append(i[0])
        return list

    def AddParkingPlaza(self):
            conn = Connect()
            cr = conn.cursor()
            description=self.txt2.get()
            price=self.txt1.get()
            category_name=self.cb1.get()



            q = f"insert into plaza_price values (null,'{category_name}','{price}','{description}')"
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo('Success', 'Added Succesfully')
            self.reset()



    def reset(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.cb1.set('')


#object=Add_ParkingPlaza()