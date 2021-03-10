from tkinter import *
from PIL import Image,ImageTk
from Components.table import SimpleTable
from sms import *
#from appointments import Appointment
from tkinter import messagebox
#from display1 import Display
import sqlite3


class DoctorPage:
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

        sql = "select * from 'patients' where status = 0"
        dataset = c.execute(sql)
        self.count = 0
        for data in dataset:
            self.listbox.insert(self.count, str(data[0]) + " : " + data[1])
            self.count += 1
        conn.commit()

        conn.close()

        mainloop()
    def refersh(self):
        self.menu_frame.destroy()
        accept_button.destroy()

        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()
        self.scroll = Scrollbar(self.panel, orient='vertical')
        self.listbox = Listbox(self.panel, width=30, height=20, font=('arial', 16))

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.listbox.place(x=100, y=150)
        self.scroll.place(x=462, y=150, relheight=0.635)

        sql="select * from 'patients' where status = 0"
        dataset=c.execute(sql)

        for i in range(self.count):
            self.listbox.delete(0)

        count=0
        for data in dataset:
            self.listbox.insert(count,f"{data[0]:{2}} : {data[1]:{20}}")
            count+=1
        conn.commit()

        conn.close()
        self.display_button = Button(self.panel, text='Display', padx=30, font=('arial', 16),
                                     command=lambda: self.display(self.listbox.get(ACTIVE).split(':')[0], 0))
        self.home_button = Button(self.panel, image=self.home_icon, command=lambda: self.Homepage(self.root),
                                  bg='#ebe6d8', padx=20,
                                  font=('arial'))
        self.display_button.place(x=500, y=250)
        self.home_button.place(x=1450, y=30)

        #self.display_button = Button(self.panel, text='Display', padx=30, font=('arial', 16),
                                     #command=lambda: self.display(self.listbox.get(ACTIVE).split(':')[0], 0))
        #self.display_button.place(x=500, y=250)

    def appoint(self):
        accept_button.destroy()
        self.menu_frame.destroy()
        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        self.scroll = Scrollbar(self.panel, orient='vertical')
        self.listbox = Listbox(self.panel, width=30, height=20, font=('arial', 16))

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.listbox.place(x=100,y=150)
        self.scroll.place(x=462,y=150,relheight=0.635)

        sql = "select * from 'patients' where status = 1"
        dataset = c.execute(sql)

        self.count = 0
        for data in dataset:
            self.listbox.insert(self.count, f"{data[0]:{2}} : {data[1]:{20}}")
            self.count += 1
        conn.commit()

        conn.close()
        self.display_button = Button(self.panel, text='Display', padx=30, font=('arial', 16),
                                     command=lambda: self.display(self.listbox.get(ACTIVE).split(':')[0],1))
        self.home_button = Button(self.panel, image=self.home_icon, command=lambda:self.Homepage(self.root), bg='#ebe6d8', padx=20,
                                  font=('arial'))
        self.display_button.place(x=500, y=250)
        self.home_button.place(x=1450, y=30)


    def display(self, ID,flag):
        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        sql = "SELECT * FROM 'patients' WHERE ID = " + str(ID)
        c.execute(sql)
        patient = c.fetchall()[0]
        self.menu_frame = SimpleTable(self.bottom, rows=8, columns=2, height=390, width=650)
        self.menu_frame.place(x=800, y=100)
        self.menu_frame.grid_propagate(0)
        self.menu_frame.set(row=0,column=0,value='First Name')
        self.menu_frame.set(row=1, column=0, value='Last Name')
        self.menu_frame.set(row=2, column=0, value='Date Of Birth')
        self.menu_frame.set(row=3, column=0, value='Address')
        self.menu_frame.set(row=4, column=0, value='Gender')
        self.menu_frame.set(row=5, column=0, value='Blood Group')
        self.menu_frame.set(row=6, column=0, value='Phone Number')
        self.menu_frame.set(row=7, column=0, value='E-Mail')
        self.menu_frame.set(row=0, column=1, value=patient[1])
        self.menu_frame.set(row=1, column=1, value=patient[2])
        self.menu_frame.set(row=2, column=1, value=patient[5])
        self.menu_frame.set(row=3, column=1, value=patient[3])
        self.menu_frame.set(row=4, column=1, value=patient[6])
        self.menu_frame.set(row=5, column=1, value=patient[7])
        self.menu_frame.set(row=6, column=1, value=patient[8])
        self.menu_frame.set(row=7, column=1, value=patient[4])
        if flag == 0:
            global accept_button
            accept_button = Button(self.bottom, text='Accept',font=('arial'),padx=10,command=lambda : self.accept(ID))
            accept_button.place(x=1350,y=500)

        conn.commit()

        conn.close()

    def accept(self, ID):
        # print(ID)
        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        SMS(ID)

        # sql = "UPDATE 'patients' SET Status=1 where ID = "+str(ID)

        accept_button.config(state=DISABLED)


    def Homepage(self,root):
        #self.destroy()
        self.bottom.destroy()
        self.panel.destroy()
        import register
        register.ViewPage(self.root)
        #mainloop()
if __name__=="__main__":
    root=Tk()
    DoctorPage(root)
    root.mainloop()