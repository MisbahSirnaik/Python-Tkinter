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

def validate_name(user_name):
	if user_name.isalpha():
		return True
	elif user_name is "":
		return True 
	else:
		msg="Dear User, Please enter valid user name " +"\n"+ "Hint: Use Alphabets to fill this field  " 
		messagebox.showerror('Oops..',msg)
		return False

def f5():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entAddRno.get())
		fname=entAddFName.get()
		lname=entAddLName.get()
		marks=int(entAddMarks.get())
		cursor=con.cursor()
		if rno < 0:
			messagebox.showerror('Oops..','Dear User, Please enter valid rno to proceed ...Please enter all the details and then click REGISTER ')
			con.rollback()
		elif fname == "" or lname== "" :
			messagebox.showerror('Oops..','Dear User,Kindly enter Fullname to proceed ...Please enter all the details and then click REGISTER')
			con.rollback()
		elif (not fname.strip().isalpha()):
			messagebox.showerror('Oops..','Dear User,Kindly enter valid name (only alphabets) to proceed ...Please enter all the details and then click REGISTER')
			con.rollback()
		elif (not lname.strip().isalpha()):
			messagebox.showerror('Oops..','Dear User,Kindly enter valid last name (only alphabets) to proceed ...Please enter all the details and then click REGISTER')
			con.rollback()
		elif len(fname) <2 :
			messagebox.showerror('Oops..','Dear User, Please enter valid name to proceed ...Please enter all the details and then click REGISTER ')
			con.rollback()
		elif len(lname) <2 :
			messagebox.showerror('Oops..','Dear User, Please enter valid last name to proceed ...Please enter all the details and then click REGISTER ')
			con.rollback()
		elif marks== '' :
			messagebox.showerror('Oops..','Dear User,Kindly enter your marks to proceed ...Please enter all the details and then click REGISTER')
			con.rollback()
		elif (marks<0 or marks > 100) :
			messagebox.showerror('Oops..','Dear User,Kindly enter your valid marks to proceed ...Please enter all the details and then click REGISTER')
			con.rollback()
		else:

			sql="insert into student values('%d','%s','%s','%d')"
			args=(rno,fname,lname,marks)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+ " record inserted "
			messagebox.showinfo("Sahi Kiya ",msg)
			entAddRno.delete(0,END)
			entAddFName.delete(0,END)
			entAddLName.delete(0,END)
			entAddMarks.delete(0,END)
			entAddRno.focus()
	
	except IntegrityError:
		con.rollback()
		messagebox.showerror("Galat Kiya ","Primary Key")
	
	except ValueError as e :
		con.rollback()
		msg= "Enter all the valid details and then click save  " + "\n" + "Hint: " + str(e) 
		messagebox.showerror("Galat Kiya ",msg)
	
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("Galat Kiya ",e)
	finally:
		if con is not None:
			con.close()



def callPreviousScreen():
	adst.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python prj.py')



adst =Tk()
adst.title("Add Stu.")
#adst.geometry("500x500+300+100")
adst.geometry("1280x970+0+0")

C = Canvas(adst, bg="blue", height=120, width=120)
filename = PhotoImage(file = "p2.gif")
background_label = Label(adst, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()


#Register Callback function validate_name
valid_name = adst.register(validate_name)
valid_no = adst.register(validate_no)

lb_heading=Label(adst,text="   Add Student Details ",width=27,font=('Beauty Mountains Personal Use',56),bg='powder blue')
lb_heading.place(x=90,y=20)  

lblAddRno=Label(adst,text="Enter rno: ",font=('Beauty Mountains Personal Use',25),bg='pink')
lblAddFName=Label(adst,text="Enter First Name: ",font=('Beauty Mountains Personal Use',25),bg='pink')
lblAddLName=Label(adst,text="Enter Last Name: ",font=('Beauty Mountains Personal Use',25),bg='pink')
lblAddMarks=Label(adst,text="Enter marks: ",font=('Beauty Mountains Personal Use',25),bg='pink')
entAddRno=Entry(adst,bd=5,font=('arial',18,'bold'))
entAddRno.config(validate="key",validatecommand=(valid_no,'%P'))
entAddFName=Entry(adst,bd=5,font=('arial',18,'bold'))
entAddLName=Entry(adst,bd=5,font=('arial',18,'bold'))
#Pass option value to call back function - validate %P is specifier used to pass to call back function

entAddFName.config(validate="key",validatecommand=(valid_name,'%P'))
entAddLName.config(validate="key",validatecommand=(valid_name,'%P'))

entAddMarks=Entry(adst,bd=5,font=('arial',18,'bold'))
entAddMarks.config(validate="key",validatecommand=(valid_no,'%P'))
btnAddSave=HoverButton(adst,text="Save",font=('Beauty Mountains Personal Use',28),bg='pink',activebackground='powder blue',command=f5)
btnAddBack=HoverButton(adst,text="Back",font=('Beauty Mountains Personal Use',28),bg='pink',activebackground='powder blue',command=callPreviousScreen)

lblAddRno.pack(pady=3)
entAddRno.pack(pady=3)
lblAddFName.pack(pady=3)
entAddFName.pack(pady=3)
lblAddLName.pack(pady=3)
entAddLName.pack(pady=3)
lblAddMarks.pack(pady=3)
entAddMarks.pack(pady=3)

btnAddSave.place(x=550,y=550)
btnAddBack.place(x=650,y=550)

adst.mainloop()


