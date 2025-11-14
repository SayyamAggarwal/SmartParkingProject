from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import *
from tkinter.filedialog import askopenfilename
import cv2
from PIL import ImageTk, Image
from datetime import datetime
import numpy as np
import easyocr

from Email import sendEmail
import Add_Vehicle


class Window:
    def __init__(self,tollId):
        self.toll_id = tollId[0]
        self.root = Toplevel()
        self.root.title("Smart parking || Pay Parking Price")
        self.root.state("zoomed")
        self.maincolor = '#63b8f8'
        self.seccolor = '#006baf'
        self.textcolor = '#f1f2f4'

        self.ml = Label(self.root, text="Number Plate Scanning", font=('Courier New', 35, 'bold'), anchor='center',
                        bg=self.seccolor, fg=self.textcolor)
        self.ml.pack(pady=20, padx=20)

        self.font = ('', 8, 'bold')

        self.root.configure(background=self.seccolor)
        self.conn = Connect()
        self.cr = self.conn.cursor()

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())

        # Main Frame
        self.updateForm = Frame(self.root, pady=10, padx=10, width=width, height=height, bg='white')
        self.updateForm.pack()

        # Left Frame
        self.frame1 = Frame(self.updateForm, width=width / 2, height=height-100, bg='white', highlightthickness=3,highlightcolor='white')
        self.frame1.grid(row=0, column=0, padx=10, pady=10)
        self.frame1.grid_propagate(0)

        self.mainLabel = Label(self.frame1, text="PAY PARKING PRICE", font=('Courier New', 20, 'bold'), background='white',
                               fg=self.seccolor, anchor='center')
        self.mainLabel.grid(row=0, column=1,padx=30,pady=30)

        self.l2 = Label(self.frame1, text="Vehicle Number", font=self.font, background='white',
                        fg=self.seccolor)
        self.l2.grid(row=1, column=0, pady=10, padx=10,sticky='w')
        self.entry = Entry(self.frame1, font=self.font, width=32,background=self.seccolor,fg=self.textcolor)
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        self.b = Button(self.frame1, text="Search", font=self.font, command=self.search,fg=self.textcolor,bg=self.seccolor)
        self.b.grid(row=1, column=2,padx=10)
        self.btn = Button(self.frame1, text="Register", font=self.font, command=Add_Vehicle.Add_Vehicle, fg=self.textcolor,
                        bg=self.seccolor)
        self.btn.grid(row=2, column=2, padx=10)

        self.l1 = Label(self.frame1, text="Vehicle Id", font=self.font, background='white', fg=self.seccolor)
        self.l1.grid(row=2, column=0, pady=10, padx=10,sticky='w')
        self.entry1 = Entry(self.frame1, font=self.font, width=32,bg=self.seccolor,fg=self.textcolor)
        self.entry1.grid(row=2, column=1, padx=10, pady=10)

        self.l3 = Label(self.frame1, text="Date", font=self.font, background='white', fg=self.seccolor)
        self.l3.grid(row=3, column=0, pady=10, padx=10,sticky='w')
        self.entry2 = Entry(self.frame1, font=self.font, width=32,bg=self.seccolor,fg=self.textcolor)
        self.entry2.grid(row=3, column=1, padx=10, pady=10)

        self.l4 = Label(self.frame1, text="Time", font=self.font, background='white', fg=self.seccolor)
        self.l4.grid(row=4, column=0, pady=10, padx=10,sticky='w')
        self.entry3 = Entry(self.frame1, font=self.font, width=32,bg=self.seccolor,fg=self.textcolor)
        self.entry3.grid(row=4, column=1, padx=10, pady=10)

        self.l5 = Label(self.frame1, text="Payment Mode", font=self.font, background='white',
                        fg=self.seccolor)
        self.l5.grid(row=5, column=0, pady=10, padx=10,sticky='w')
        self.t4 = ttk.Combobox(self.frame1, values=['Cash', 'Online'], font=self.font, width=30)
        self.t4.grid(row=5, column=1, padx=10, pady=10)

        self.l5 = Label(self.frame1, text="Amount", font=self.font, background='white',
                        fg=self.seccolor)
        self.l5.grid(row=6, column=0, pady=10, padx=10,sticky='w')
        self.t5 = Entry(self.frame1, font=self.font, width=32,bg=self.seccolor,fg=self.textcolor)
        self.t5.grid(row=6, column=1, padx=10, pady=10)

        self.l6 = Label(self.frame1, text="Admin Id", font=self.font, background='white', fg=self.seccolor)
        self.l6.grid(row=7, column=0, pady=10, padx=10,sticky='w')
        self.t6 = Entry(self.frame1, font=self.font, width=32,readonlybackground=self.seccolor,fg=self.textcolor)
        self.t6.grid(row=7, column=1, padx=10, pady=10)
        self.t6.insert(0,self.toll_id)
        self.t6.configure(state='readonly')

        self.b1 = Button(self.frame1, text='Submit', font=self.font, width=10, command=self.insert,fg=self.textcolor,bg=self.seccolor)
        self.b1.grid(row=8, column=1, pady=40, padx=20)
        #self.fetch_current_datetime()
# ______________________________________________________________________________________________________________________________
        #  Right Frame
        self.frame2 = Frame(self.updateForm, width=width, height=height - 100, bg='white', highlightthickness=3,highlightcolor='white')
        self.frame2.grid(row=0, column=2, padx=10, pady=10)
        self.frame2.grid_propagate(0)

        # Right Frame-- Top Frame
        self.frame3=Frame(self.frame2,bg='white',width=int(self.frame2.winfo_screenwidth())/3, height=int(self.frame2.winfo_screenheight()))
        self.frame3.pack(padx=10,pady=10)
        self.frame3.pack_propagate(0)
        # print("hello")
        self.ml = Label(self.frame3, text="Video Capture", font=('', 20, 'bold'), fg=self.seccolor, bg='white',
                        anchor='center')
        self.ml.grid(row=0, column=0)

    # Default camera display size (pixels). Change these to resize the camera window.
        self.cam_width = 400
        self.cam_height = 240

        self.frame4 = Frame(self.frame2, width=int(self.frame2.winfo_screenwidth()) / 3,
                            height=int(self.frame2.winfo_screenheight()))
        self.frame4.pack(padx=10, pady=10)
        self.frame4.pack_propagate(0)
        self.btn = Button(self.frame4, text="Open Camera", font=self.font, width=12, command=self.startVideo,
                          fg=self.textcolor, bg=self.seccolor)
        self.btn.grid(row=5, column=0, pady=20, padx=20)
        self.btn1 = Button(self.frame4, text="stop", font=self.font, width=12, command=self.stopVideo, fg=self.textcolor,
                           bg=self.seccolor)
        self.btn1.grid(pady=20, row=5, column=1, padx=20)
        self.imageBtn = Button(self.frame4, text='Capture', font=self.font, width=12,fg=self.textcolor,
                           bg=self.seccolor,command=self.capture)
        self.imageBtn.grid(row=6, column=0, padx=10, pady=10)

        self.btn3 = Button(self.frame4, text="Select Image", font=self.font, width=12, command=self.selectImage,
                           fg=self.textcolor, bg=self.seccolor)
        self.btn3.grid(row=6,column=1,pady=20, padx=20)


        self.root.mainloop()

    def selectImage(self):
        file = askopenfilename(parent=self.root)

        # Read input image
        img = cv2.imread(file)

        # Convert input image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Load the XML file containing the license plate cascade classifier
        # cascade = cv2.CascadeClassifier('assets/indian_license_plate.xml')
        # cascade=cv2.CascadeClassifier("../assets/indian_license_plate.xml")
        cascade=cv2.CascadeClassifier("assets/indian_license_plate.xml")
        # Detect license number plates
        plates = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7)
        print('Number of detected license plates:', len(plates))

        # Initialize easyocr reader
        reader = easyocr.Reader(['en'])
        kernel = np.ones((3, 3), np.uint8)
        plate_text = ''

        # Loop over all plates
        for (x, y, w, h) in plates:
            # Draw bounding rectangle around the license number plate
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract region of interest (ROI) for OCR
            plate_roi = gray[y:y + h, x:x + w]
            _, plate_roi = cv2.threshold(plate_roi, 64, 255, cv2.THRESH_BINARY_INV)
            # plate_roi = cv2.erode(plate_roi, kernel, iterations=1)
            plate_roi = cv2.dilate(plate_roi, kernel, iterations=1)

            # Perform OCR on the plate ROI
            result = reader.readtext(plate_roi)

            # Extract text from OCR result
            if result:
                plate_text = result[0][1]
                plate_text = "".join(i for i in plate_text if i.isalnum())
                # print(result)
                print('Detected Plate Text:', plate_text)

                # Display detected text on image
                cv2.putText(img, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the image with detected license plates
        self.entry.delete(0,'end')
        self.entry.insert(0, plate_text)
        cv2.imshow('plate', img)
        cv2.waitKey(0)
        try:
            cv2.destroyAllWindows()
        except:
            pass

        # plt.imshow(img)
        # plt.show()
        # cv2.destroyAllWindows()

    def startVideo(self):
        self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.show_frames()


    def show_frames(self):
        flag, self.img_frame = self.video.read()
        if flag is True:
            # Convert BGR (OpenCV) to RGB (PIL/Tk)
            self.img_frame = cv2.cvtColor(self.img_frame, cv2.COLOR_BGR2RGB)

            # Resize frame to target camera display size (keep aspect if you prefer by calculating dims)
            try:
                frame_resized = cv2.resize(self.img_frame, (int(self.cam_width), int(self.cam_height)))
            except Exception:
                # If resize fails for any reason, fall back to original frame
                frame_resized = self.img_frame

            image = Image.fromarray(frame_resized)
            imageTk = ImageTk.PhotoImage(image)

            self.ml.configure(image=imageTk)
            self.ml.image = imageTk
            self.ml.after(5, self.show_frames)

    def capture(self):

        img = self.img_frame

        # Convert input image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Load the XML file containing the license plate cascade classifier
        cascade = cv2.CascadeClassifier('assets/indian_license_plate.xml')

        # Detect license number plates
        plates = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=7)
        print('Number of detected license plates:', len(plates))

        # Initialize easyocr reader
        reader = easyocr.Reader(['en'])
        kernel = np.ones((3, 3), np.uint8)
        plate_text = ''

        # Loop over all plates
        for (x, y, w, h) in plates:
            # Draw bounding rectangle around the license number plate
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract region of interest (ROI) for OCR
            plate_roi = gray[y:y + h, x:x + w]
            _, plate_roi = cv2.threshold(plate_roi, 64, 255, cv2.THRESH_BINARY_INV)
            # plate_roi = cv2.erode(plate_roi, kernel, iterations=1)
            plate_roi = cv2.dilate(plate_roi, kernel, iterations=1)

            # Perform OCR on the plate ROI
            result = reader.readtext(plate_roi)

            # Extract text from OCR result
            if result:
                plate_text = result[0][1]
                plate_text = "".join(i for i in plate_text if i.isalnum())

                # print(result)
                print('Detected Plate Text:', plate_text)

                # Display detected text on image
                cv2.putText(img, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            self.entry.delete(0, 'end')
            self.entry.insert(0, plate_text)


    def search(self):
            vehno = self.entry.get()

            if len(vehno) == 0:
                msg.showwarning('Warning', 'Please Enter Vehicle Number', parent=self.root)
            else:

                q = f"select id, category_name from vehicle where vehicle_number like '{vehno}'"
                self.cr.execute(q)
                result = self.cr.fetchall()
                if len(result) == 0:
                    msg.showwarning("Warning", "No vehicle of this number is registered",parent=self.root)

                else:
                    self.entry1.delete(0, 'end')
                    self.entry1.insert(0, result[0][0])
                    now = datetime.today().date()
                    now1 = datetime.today().time()
                    current_time = now1.strftime("%H:%M:%S")
                    current_date = now.strftime("%y-%m-%d")

                    self.entry2.insert(0, current_date)
                    self.entry3.insert(0, current_time)

                    # v_id = self.entry1.get()
                    # q = f'select issue_date,issue_time from issuemonthly_pass where vehicle_id ="{v_id}"'
                    # self.cr.execute(q)
                    # passData = self.cr.fetchall()
                    # if len(passData) == 0:
                    #     msg.showwarning('Warning', f"{vehno} is not Registered.", parent=self.root)
                    # else:
                    #     self.entry2.delete(0,'end')
                    #     self.entry2.insert(0, str(passData[0][0]))
                    #     self.entry3.delete(0,'end')
                    #     self.entry3.insert(0,passData[0][1])
    def stopVideo(self):
        self.video.release()
        cv2.destroyAllWindows()
        self.ml.configure(image='')


    def insert(self):
        vehicle_number = self.entry.get()
        vehicle_id = self.entry1.get()
        date = self.entry2.get()
        time = self.entry3.get()
        type = self.t4.get()
        amount = self.t5.get()
        # q = "Select * from toll"
        # self.cr.execute(q)
        # res = self.cr.fetchall()
        #self.t6.insert(0, res[0][0])
        admin_id = self.t6.get()
        if type == 'Cash':
            q = "insert into entry values(null,'" + vehicle_number + "','" + date + "','" + time + "','" + vehicle_id + "','" +admin_id+ "','" + amount +"')"
            self.cr.execute(q)
            self.conn.commit()
            self.emailRemark(admin_id,vehicle_number)

            msg.showinfo("Success", "Entry has been inserted",parent=self.root)
            self.reset()
        elif type == 'Online':
            sql = "insert into transaction values(null,'" + vehicle_id + "','" + date + "','" + time + "','" + vehicle_number + "','" + admin_id + "','"+amount+"')"
            self.cr.execute(sql)
            self.conn.commit()
            self.emailRemark(admin_id, vehicle_number)
            msg.showinfo("Success", "Entry has been inserted",parent=self.root)
            self.reset()
        else:
            msg.showwarning('Warning', 'Please Select Method for payment',parent=self.root)

    def reset(self):
        self.entry.delete(0, 'end')
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        self.t6.delete(0, 'end')




    def emailRemark(self, id,vehicle_number):
        id = id
        date = self.entry2.get()
        time = self.entry3.get()

        vehicle_id = self.entry1.get()
        q = f"Select * from admin_table where id = {id}"
        self.cr.execute(q)
        res = self.cr.fetchall()
        q1 = f"Select * from vehicle where id ={vehicle_id} "
        # print(q1)
        self.cr.execute(q1)
        result1 = self.cr.fetchall()
        # print(result1)

        message = f'''Toll Name - {res[0][1]},{result1[0][8]} has been identified at {time} on {date} in {res[0][5]}.

                    Here are Details - 
                     Toll Name - {res[0][1]}
                     Toll Mobile no- {res[0][4]}
                     Vehicle Number -{vehicle_number}
                     Owner's Name - {result1[0][2]}
                     Owner's Email - {result1[0][4]}
                     Owner's Mobile Number - {result1[0][3]}

                 '''
        subject = "Toll Payment Report"

        x = sendEmail(to=res[0][2], message=message, subject=subject)
        print(x)
        if x:
            msg.showinfo("Sent", "Vehicle Identification mail has been sent!!",parent=self.root)
        else:
            msg.showwarning('Warn', 'Mail not sent',parent=self.root)


if __name__ == "__main__":
    Window(tollId=1)
