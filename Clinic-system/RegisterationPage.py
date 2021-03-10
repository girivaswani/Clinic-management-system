from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3


class Register:
    def __init__(self, master):
        #Toplevel.__init__(self)

        global master_root
        #master_root = master
        self.root=master
        #self.root.state('zoomed')
        self.root.title("Registeration")
        self.root.geometry("720x620+20+20")
        self.root.resizable(False, False)

        #self.top = Frame(self, height=120, bg='orange')
        #self.top.pack(fill=X)

        self.bottom = Frame(self.root, height=500, bg='lightblue')
        self.bottom.pack(fill=X)
        self.raw_image = Image.open('icons/bckgrnd.png')
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)
        self.panel = Label(self.bottom, image=self.img)
        self.panel.pack()
        self.panel.grid_propagate(0)

        self.register_icon = PhotoImage(file='icons/patient.png')
        self.icon_label = Label(self.panel, bg='#ebe6d8', image=self.register_icon)
        self.icon_label.place(x=200, y=30)

        self.top_label = Message(self.panel, width=600, font=("Monotype Corsiva", 20, "bold italic"),text="Registeration", bg="#ebe6d8", relief=SOLID, borderwidth=2)
        self.top_label.place(x=290, y=40)

        self.Gender = StringVar(value='@')
        self.Gender.set(value='Others')

        self.bottom.grid_propagate(0)

        self.home_icon = PhotoImage(file='icons/home-run.png')

        self.l_fname = Label(self.bottom, text='First Name', bg='#ebe6d8', font=('arial'))
        self.l_lname = Label(self.bottom, text='Last Name', bg='#ebe6d8', font=('arial'))
        self.l_dob = Label(self.bottom, text='Date Of Birth', bg='#ebe6d8', font=('arial'))
        self.l_yr = Label(self.bottom, text='(YYYY-MM-DD)', bg='#ebe6d8', font=('arial 10 bold'))
        self.l_address = Label(self.bottom, text='Address:', bg='#ebe6d8', font=('arial'))
        self.l_gender = Label(self.bottom, text='Gender:', bg='#ebe6d8', font=('arial'))
        self.l_bgroop = Label(self.bottom, text='BLood Group', bg='#ebe6d8', font=('arial'))
        self.l_phone = Label(self.bottom, text='Contact No.', bg='#ebe6d8', font=('arial'))
        self.l_email = Label(self.bottom, text='Email Address', bg='#ebe6d8', font=('arial'))

        self.firstname = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.lastname = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.dob = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.address = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.bgroop = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.phone = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))
        self.email = Entry(self.bottom, width=30, bg='white', fg='black', font=('arial'))

        self.submit = Button(self.bottom, text='Submit', command=self.submit, bg='#ebe6d8', padx=20, font=('arial'))
        self.home_button = Button(self.bottom, image=self.home_icon, command=self.Homepage, bg='#ebe6d8', padx=20,
                                  font=('arial'))

        self.r1 = Radiobutton(self.bottom, variable=self.Gender, value='Male', bg='white', text='Male',
                              font=('arial'))
        self.r2 = Radiobutton(self.bottom, variable=self.Gender, value='Female', bg='white', text='Female',
                              font=('arial'))
        self.r3 = Radiobutton(self.bottom, variable=self.Gender, value='Others', bg='white', text='Others',
                              font=('arial'))

        self.l_lname.place(x=40, y=200)
        self.l_fname.place(x=40, y=160)

        self.l_dob.place(x=40, y=240)
        self.l_yr.place(x=40, y=270)
        self.l_address.place(x=40, y=300)
        self.l_gender.place(x=40, y=340)
        self.l_bgroop.place(x=40, y=380)
        self.l_phone.place(x=40, y=420)
        self.l_email.place(x=40, y=460)

        self.firstname.place(x=200, y=160)
        self.lastname.place(x=200, y=200)
        self.dob.place(x=200, y=240)
        self.address.place(x=200, y=300)
        self.r1.place(x=200, y=340)
        self.r2.place(x=320, y=340)
        self.r3.place(x=440, y=340)
        self.bgroop.place(x=200, y=380)
        self.phone.place(x=200, y=420)
        self.email.place(x=200, y=460)

        self.home_button.place(x=670, y=30)
        self.submit.place(x=475, y=525)
        self.footer = Label(self.panel, bg="ivory3", height=1, text="@Copyright 2020 Alokanand. All rights reserved")
        self.footer.pack(side=BOTTOM, fill=X)
        self.panel.pack_propagate(0)

        mainloop()

    def submit(self):

        self.val1 = self.firstname.get()
        self.val2 = self.lastname.get()
        self.val3 = self.dob.get()
        self.val4 = self.address.get()
        self.val5 = self.bgroop.get()
        self.val6 = self.phone.get()
        self.val7 = self.email.get()
        self.val8 = self.Gender.get()

        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        if self.val1 == '' or self.val2 == ' ' or self.val3 == ' ' or self.val4 == ' ' or self.val5 == ' ' or self.val6 == ' ' or self.val7 == ' ':
            messagebox.showinfo('Warning!', 'Please fill all entries !!!')
        elif len(self.val6) != 10:
            messagebox.showinfo('Mobile No. has 10 digits !', 'Please fill proper Mobile No. !!!')
        elif '@' not in self.val7 or '.com' not in self.val7 or '@.com' in self.val7 or ' ' in self.val7:
            messagebox.showinfo('Suggestion !!', 'Please fill proper E-mail ID !!!')
        else:
            sql = "INSERT INTO  'patients' (first_name ,last_name ,address ,email ,DOB,Gender,Blood_group,mobile_no) VALUES (?,?,?,?,?,?,?,?) "
            c.execute(sql, (self.val1, self.val2, self.val4, self.val7, self.val3, self.val8, self.val5, self.val6))

            conn.commit()

            conn.close()

            messagebox.showinfo('Success!', 'Your Data is Registered')

            self.firstname.delete(0, END)
            self.lastname.delete(0, END)
            self.dob.delete(0, END)
            self.address.delete(0, END)
            self.bgroop.delete(0, END)
            self.phone.delete(0, END)
            self.email.delete(0, END)

    def Homepage(self):
        self.bottom.destroy()
        self.panel.destroy()
        import register
        register.ViewPage(self.root)

        #master_root.deiconify()
        #mainloop()


# app=Register()
# app.mainloop()
if __name__ == "__main__":
    root = Tk()
    Register(root)
    root.mainloop()