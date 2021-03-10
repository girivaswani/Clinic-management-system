from tkinter import *
from PIL import Image,ImageTk
from Components.table import SimpleTable
from sms import *
#from appointments import Appointment
from tkinter import messagebox
#from display1 import Display
import sqlite3


class Appointment:
    def __init__(self, master):
        #super().__init__(master)
        self.root = master
        self.root.state('zoomed')
        self.root.title("View Patients")
        self.root.geometry("720x620+20+20")
        #self.resizable(False, False)

        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        #self.top = Frame(self, height=120)
        #self.top.pack(fill=X)

        self.bottom = Frame(self.root, height=500)
        self.bottom.pack(fill=X)
        self.raw_image=Image.open('icons/bckgrnd.png')
        self.raw_image=self.raw_image.resize((1600,900))
        self.img=ImageTk.PhotoImage(self.raw_image)
        self.panel=Label(self.bottom,image=self.img)
        self.panel.pack()
        self.panel.grid_propagate(0)

        self.register_icon = PhotoImage(file='icons/blood-pressure.png')
        self.icon_label = Label(self.panel, bg='#ebe6d8', image=self.register_icon)
        self.icon_label.place(x=220, y=30)

        self.home_icon = PhotoImage(file='icons/home-run.png')
        self.top_label = Message(self.panel, width=600, font=("Monotype Corsiva",20,"bold italic"),text="My Patients", bg="#ebe6d8", relief=SOLID, borderwidth=2)
        self.top_label.place(x=290, y=40)

        self.scroll = Scrollbar(self.panel,orient='vertical')
        self.listbox = Listbox(self.panel, width=30, height=20, font=('arial', 16))

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        # self.listbox.grid_propagate(False)

        #self.listbox.grid(row=0, column=0, padx=(30, 0))
        #self.scroll.grid(row=0, column=1, sticky=N + S)
        self.listbox.place(x=100,y=150)
        self.scroll.place(x=462,y=150,relheight=0.635)
        #self.scroll.pack(side="right",fill="y")
        self.display_button = Button(self.panel, text='Display', padx=30, font=('arial', 16),
                                     command=lambda: self.display(self.listbox.get(ACTIVE).split(':')[0],0))
        root=self.root
        self.home_button = Button(self.panel, image=self.home_icon, command=lambda:self.Homepage(root), bg='#ebe6d8', padx=30,
                                  font=('arial'))
        self.refresh_button = Button(self.bottom, text='Refresh', command=self.refersh, padx=30,
                                     font=('arial', 16))
        self.appoint_button = Button(self.bottom, text='Appointments', command=self.appoint, padx=30,
                                     font=('arial', 16))

        self.display_button.place(x=500,y=250)
        self.home_button.place(x=1450, y=30)
        self.refresh_button.place(x=500,y=300)
        self.appoint_button.place(x=500,y=350)
        self.footer = Label(self.panel, bg="ivory3", height=1,text="@Copyright 2020 Alokanand. All rights reserved")
        self.footer.pack(side=BOTTOM, fill=X)
        self.panel.pack_propagate(0)
        sql = "select * from 'patients' where status = 1"
        dataset = c.execute(sql)

        self.count = 0
        for data in dataset:
            self.listbox.insert(self.count, f"{data[0]:{2}} : {data[1]:{20}}")
            self.count += 1
        conn.commit()

        conn.close()


