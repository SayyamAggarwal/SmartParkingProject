from tkinter import *
import Add_Admin
import Admin_ChangePassword
import View_Admin
import ADD_Category
import View_Category
import Add_Vehicle
import View_Vehicle
import Add_MonthlyPass
import View_MonthlyPass
import ADD_ParkingPlaza
import View_ParkingPlaza
import Add_PlazaPrice
import View_PlazaPrice
import View_Entry
import View_transaction
# import Recognise 
from Recognise import Window
class Main:
    def __init__(self,adminInfo):


        print(adminInfo)
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('---------')
        self.admindetail = adminInfo
        print(self.admindetail)

        self.mainMenu = Menu(self.root)
        self.root.configure(menu=self.mainMenu)

        if adminInfo[-1]=="Super-Admin":
            self.adminMenu = Menu(self.mainMenu,tearoff=False)
            self.mainMenu.add_cascade(label='Manage Admin',menu=self.adminMenu)
            self.adminMenu.add_command(label='Add Admin',command=Add_Admin.Add_Admin)
            self.adminMenu.add_command(label='View Admin',command=View_Admin.Main)

        self.categoryMenu=Menu(self.mainMenu,tearoff=False)
        self.mainMenu.add_cascade(label='Manage Category',menu=self.categoryMenu)
        self.categoryMenu.add_command(label='Add Category',command=ADD_Category.Add_Category)
        self.categoryMenu.add_command(label='View Category',command=View_Category.Main)

        self.categoryMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Profile', menu=self.categoryMenu)
        self.categoryMenu.add_command(label='Change Password',command=lambda : Admin_ChangePassword.AdminChangePassword(adminInfo[2]))
        self.categoryMenu.add_command(label='Logout',command=self.root.destroy)

        self.vehicleMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Vehicle', menu=self.vehicleMenu)
        self.vehicleMenu.add_command(label='Add Vehicle', command=Add_Vehicle.Add_Vehicle)
        self.vehicleMenu.add_command(label='View Vehicle', command=View_Vehicle.Main)

        self.monthlypassMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Monthly Pass', menu=self.monthlypassMenu)
        self.monthlypassMenu.add_command(label='Add Monthly Pass', command=Add_MonthlyPass.Add_ParkingPlaza)
        self.monthlypassMenu.add_command(label='View Monthy Pass', command=View_MonthlyPass.Main)

        self.parkingplazaMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Parking Plaza', menu=self.parkingplazaMenu)
        self.parkingplazaMenu.add_command(label='Add Parking Plaza', command=ADD_ParkingPlaza.Add_ParkingPlaza)
        self.parkingplazaMenu.add_command(label='View Parking Plaza', command=View_ParkingPlaza.Main)

        self.plazapriceMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Plaza Price', menu=self.plazapriceMenu)
        self.plazapriceMenu.add_command(label='Add Plaza Price', command=Add_PlazaPrice.Add_ParkingPlaza)
        self.plazapriceMenu.add_command(label='View Plaza Price', command=View_PlazaPrice.Main)

        self.paymentMenu = Menu(self.mainMenu, tearoff=False)
        self.mainMenu.add_cascade(label='Manage Payment', menu=self.paymentMenu)
        self.paymentMenu.add_command(label=' Online Transaction', command=View_transaction.Main)
        self.paymentMenu.add_command(label=' Cash payment', command=View_Entry.Main)

        self.recognizeSubmenu = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Recognize', menu=self.recognizeSubmenu)
        self.recognizeSubmenu.add_command(label='Recognize Number Plate', command=lambda: Window(self.admindetail[0]))

        self.font = ('', 14, 'bold')
        self.maincolor = '#462521'
        self.seccolor = '#006baf'
        self.textcolor = 'white'

        self.root.configure(bg=self.maincolor)

        self.mainlabel = Label(self.root, text='Smart Parking System', font=('Courier New', 35, 'bold'),
                               bg=self.maincolor, fg=self.textcolor)
        self.mainlabel.pack(pady=50)

#        self.image = Image.open('innovation.jpg')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
 #       self.img = self.image.resize((self.width, self.height))
  #      bg = ImageTk.PhotoImage(self.img)

        c = Canvas(self.root, width=self.width, height=self.height)
        c.pack(fill='both', expand=True)
       # c.create_image(0, 0, image=bg, anchor=NW)

        # self.btn = Button(self.root, text='Recognise', 
        #                   font=self.font, command=Window(self.toll_id),
        #                    width=10,
        #                   height=2, bg='#c7a43a',
        #                   foreground=self.textcolor, relief=RAISED, highlightcolor="white",
        #                   highlightthickness=3)
        # btn = c.create_window(100, 80, anchor=NW, window=self.btn)

        self.root.mainloop()


adminInfo = [1,'ANIKET MAHAJAN','mahajananiket96@gmail.com']

# object=Main(adminInfo)