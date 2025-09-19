from tkinter import *
from PIL import Image, ImageTk
import ADMIN_LOGIN


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Smart parking')

        self.font = ('', 14, 'bold')
        self.maincolor = '#462521'
        self.seccolor = '#006baf'
        self.textcolor = 'white'

        self.root.configure(bg=self.maincolor)

        self.mainlabel = Label(self.root, text='Smart Parking System', font=('Courier New', 35, 'bold'),
                               bg=self.maincolor, fg=self.textcolor)
        self.mainlabel.pack(pady=50)

        self.image = Image.open('innovation.jpg')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.img = self.image.resize((self.width, self.height))
        bg = ImageTk.PhotoImage(self.img)

        c = Canvas(self.root, width=self.width, height=self.height)
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor=NW)

        self.btn = Button(self.root, text='Admin Panel', font=self.font, command=ADMIN_LOGIN.Adminlogin, width=10,
                          height=2, bg='#c7a43a',
                          foreground=self.textcolor, relief=RAISED, highlightcolor="white",
                          highlightthickness=3)
        btn = c.create_window(100, 80, anchor=NW, window=self.btn)


        btn = c.create_window(100, 80, anchor=NW, window=self.btn)



        self.btn2 = Button(self.root, text='Leave', font=self.font, command=lambda: self.root.destroy(), width=7,
                           bg=self.seccolor,
                           foreground=self.textcolor, relief=RAISED)
        btn2 = c.create_window(900, 10, anchor=NW, window=self.btn2)

        self.root.mainloop()


if __name__ == '__main__':
    Main()