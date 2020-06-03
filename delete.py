
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from PIL import ImageDraw,Image,ImageFont,ImageTk
import socket 
import requests
import tkinter as tk
import os

from tkinter import PhotoImage 


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


def validate_no(user_no):
	if user_no.isdigit():
		return True
	elif user_no is "":
		return True 
	else:
		messagebox.showerror('Oops..','Dear User, Please enter valid  no ')
		return False



#DeleteSave btn 

def f11():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entDeleteRno.get())
		cursor=con.cursor()
		if rno < 0:
			messagebox.showerror('Oops..','Dear User, Please enter valid rno to proceed ...Please enter all the details and then click REGISTER ')
			con.rollback()
			
		else:
			sql="delete from student where rno='%d' "
			args=(rno)
			cursor.execute(sql % args)
			con.commit()
			if (cursor.rowcount==0):
				messagebox.showerror('Oops..','Dear User,Kindly enter your valid ROLLNO to proceed ...Please enter all the details and then click REGISTER')
				con.rollback()
			msg=str(cursor.rowcount)+ " record deleted "
			messagebox.showinfo("Sahi Kiya ",msg)
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
	
	
	except ValueError as e :
		con.rollback()
		msg= "Enter valid details and then click save  " + "\n" + "Hint: " + str(e) 
		messagebox.showerror("Galat Kiya ",msg)
	
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("Galat Kiya ",e)
	finally:
		if con is not None:
			con.close()

def callPreviousScreen():
	dest.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python prj.py')

#DELETE Stu.
dest=Tk()
dest.title("Delete Stu.")
dest.geometry("1280x970+0+0")

C = Canvas(dest, bg="blue", height=120, width=120)
filename = PhotoImage(file = "stu1.gif")
background_label = Label(dest, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
lb_heading=Label(dest,text="   Delete Student Details ",width=27,font=('Beauty Mountains Personal Use',56),bg='light green')
lb_heading.place(x=90,y=20)  

lblDeleteRno=Label(dest,text="Enter rno: ",font=('Beauty Mountains Personal Use',28))
entDeleteRno=Entry(dest,bd=5,font=('arial',18,'bold'))
btnDeleteSave=HoverButton(dest,text="Delete",font=('Beauty Mountains Personal Use',28),bg='white',activebackground='light green',command=f11)
btnDeleteBack=HoverButton(dest,text="Back",font=('Beauty Mountains Personal Use',28),bg='white',activebackground='light green',command=callPreviousScreen)

lblDeleteRno.pack(pady=5)
entDeleteRno.pack(pady=5)
btnDeleteSave.pack(pady=5)
btnDeleteBack.pack(pady=5)
dest.mainloop()