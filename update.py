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

#UpdateSave btn 

def f8():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entUpdateRno.get())
		fname=entUpdateFName.get()
		lname=entUpdateLName.get()
		marks=int(entUpdateMarks.get())
		cursor=con.cursor()
		if rno < 0:
			messagebox.showerror('Oops..','Dear User, Please enter valid rno to proceed ...Please enter all the details and then click REGISTER ')
			con.rollback()
		elif fname == "" or lname=="":
			messagebox.showerror('Oops..','Dear User,Kindly enter name to proceed ...Please enter all the details and then click REGISTER')
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

			sql="update student set fname='%s' ,lname='%s',marks='%d' where rno='%d' "
			args=(fname,lname,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			if (cursor.rowcount==0):
				messagebox.showerror('Oops..','Dear User,Kindly enter your valid ROLLNO to proceed ...Please enter all the details and then click REGISTER')
				con.rollback()
			msg=str(cursor.rowcount)+ " record updated "
			messagebox.showinfo("Sahi Kiya ",msg)
			entUpdateRno.delete(0,END)
			entUpdateFName.delete(0,END)
			entUpdateLName.delete(0,END)
			entUpdateMarks.delete(0,END)
			entUpdateRno.focus()
	
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
	upst.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python prj.py')







#UPDATE Stu.

upst=Tk()
upst.title("Update Stu.")
upst.geometry("1280x970+0+0")

C = Canvas(upst, bg="blue", height=120, width=120)
filename = PhotoImage(file = "children.gif")
background_label = Label(upst, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
#Register Callback function validate_name
valid_name = upst.register(validate_name)
valid_no = upst.register(validate_no)

lb_heading=Label(upst,text="   Update Student Details ",width=27,font=('Beauty Mountains Personal Use',56),bg='red',fg='white')
lb_heading.place(x=90,y=20)  
lblUpdateRno=Label(upst,text="Enter rno: ",font=('Beauty Mountains Personal Use',17))
lblUpdateFName=Label(upst,text="Enter First Name: ",font=('Beauty Mountains Personal Use',17))
lblUpdateLName=Label(upst,text="Enter Last Name: ",font=('Beauty Mountains Personal Use',17))
lblUpdateMarks=Label(upst,text="Enter marks: ",font=('Beauty Mountains Personal Use',17))
entUpdateRno=Entry(upst,bd=5,font=('arial',15,'bold'))
entUpdateRno.config(validate="key",validatecommand=(valid_no,'%P'))
entUpdateFName=Entry(upst,bd=5,font=('arial',15,'bold'))
entUpdateLName=Entry(upst,bd=5,font=('arial',15,'bold'))
         #Pass option value to call back function - validate %P is specifier used to pass to call back function
entUpdateFName.config(validate="key",validatecommand=(valid_name,'%P'))
entUpdateLName.config(validate="key",validatecommand=(valid_name,'%P'))
entUpdateMarks=Entry(upst,bd=5,font=('arial',15,'bold'))
entUpdateMarks.config(validate="key",validatecommand=(valid_no,'%P'))

btnUpdateSave=HoverButton(upst,text="Save",font=('Beauty Mountains Personal Use',19),activebackground='red',command=f8)
btnUpdateBack=HoverButton(upst,text="Back",font=('Beauty Mountains Personal Use',19),activebackground='red',command=callPreviousScreen)

lblUpdateRno.pack(pady=5)
entUpdateRno.pack(pady=5)
lblUpdateFName.pack(pady=5)
entUpdateFName.pack(pady=5)
lblUpdateLName.pack(pady=5)
entUpdateLName.pack(pady=5)
lblUpdateMarks.pack(pady=5)
entUpdateMarks.pack(pady=5)
btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)


upst.mainloop()