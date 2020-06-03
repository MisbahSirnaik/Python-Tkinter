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

#Callback function for validating  No

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

# VIEW COMMANDS

def f4():
	vist.withdraw()
	root.deiconify()
def f3():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,fname,lname,marks from  student "
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+ "Roll No.=  "+ "    "+ str(d[0]) +"    "+ " Name=  " + str(d[1]).strip() + "   "  + str(d[2]).strip() +"    "+ " marks=   " + str(d[3]) + "\n" +"\n"
		stdata.insert(INSERT,msg)	
	except DatabaseError as e:
		messagebox.showerror(" Galat Kiya ",e)
	
	finally:
		if con is not None:
			con.close()
			


#GRAPH commands
def f12():
	root.withdraw()
	graph.deiconify()

def f13():
	graph.withdraw()
	root.deiconify()


def f14():
	
	try:
	
		con=connect("system/abc123")
		cursor=con.cursor()

		df=pd.read_sql("select  fname,marks from(select fname,marks from student order by marks DESc) where rownum<=5",con);
	
		n1=df['FNAME'].tolist()
		n2=df['MARKS'].tolist()
		plt.title("TOP 5 RANKERS")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.bar(n1,n2,width=0.3,color='r')
		plt.grid()
		plt.show()
	except Exception as e:
		messagebox.showerror("Oops",e)


def f15():

	os.system('python code.py')
	

def callAddScreen():
	root.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python add.py')


def callUpdateScreen():
	root.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python update.py')

def callDeleteScreen():
	root.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python delete.py')


def callLoginScreen():
	root.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python LoginScreen.py')
#################################################################################################################################################################################################

root =Tk()
root.title("Student Management System")
#root.geometry("500x500+300+100")
root.geometry("1280x970+0+0")

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "abc.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()



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

lb_heading=Label(root,text="   Student Management System ",width=27,font=('Beauty Mountains Personal Use',56),bg='maroon',foreground = "white")
lb_heading.place(x=90,y=20)  

btnAdd=HoverButton(root,text="Add Student Details ",width=15,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=callAddScreen) # add.py
btnView=HoverButton(root,text="View Student Details",width=15,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=f3) # view root
btnUpdate=HoverButton(root,text="Update Student Details",width=15,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=callUpdateScreen)# update.py
btnDelete=HoverButton(root,text="Delete Student Details",width=15,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=callDeleteScreen) # delete.py
btnGraph=HoverButton(root,text="Watch whose at the TOP",width=18,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=f12) # graph root
btnInfo=HoverButton(root,text="How's the mausam!",width=15,font=('Beauty Mountains Personal Use',25),activebackground='orange',bg='yellow',foreground = "black",command=f15)# info root
btnLogOut=HoverButton(root,text="Bored..?-LOG OUT",width=18,font=('Beauty Mountains Personal Use',22),activebackground='orange',bg='yellow',foreground = "black",command=callLoginScreen)# log out
btnLogOut.place(x=840,y=130)
btnAdd.place(x=90,y=150)
btnView.place(x=90,y=230)
btnUpdate.place(x=90,y=310)
btnDelete.place(x=90,y=390)
btnGraph.place(x=90,y=470)
btnInfo.place(x=90,y=550)

# ###########################################################################################################################################################################################
#VIEW STUDENT
vist=Toplevel(root)
vist.title("View Stu.")
vist.geometry("1280x970+0+0")
vist.configure(background='powder blue')
vist.withdraw()
lb_heading=Label(vist,text="____________________Student Details___________________________",width=27,font=('Beauty Mountains Personal Use',46),bg='powder blue',foreground = "black")
lb_heading.place(x=90,y=20)  
msg="---<<-----WISE WORDS----->>---" +"\n" + "- You'll never change your life "+"\n"+"until you change something you do DAILY " +'\n' +"\n" + "-You either succeed or learn , you never fail " +"\n" + "\n" +"- Change is Constant"+"\n" +"\n" +"- TRY ...Don't CRY" +"\n"+"\n"+"*******Have A Great Day Ahead*******"
stdata=scrolledtext.ScrolledText(vist,width=60,height=22,font=('Century Schoolbook',13)) 
btnViewBack=Button(vist,text="Back",font=('Beauty Mountains Personal Use',20),activebackground='pink',bg='white',foreground = "black",command=f4)
lblquote=Label(vist,text=msg,width=28,height=11,font=('Beauty Mountains Personal Use',25),bg='pink',foreground = "black")
lblquote.place(x=760,y=100)  

stdata.place(x=180,y=100)
btnViewBack.place(x=390,y=570)





#GRAPH 

graph=Toplevel(root)
graph.title("Top 5 Students.")
graph.geometry("1280x970+0+0")
graph.configure(background='light blue')
graph.withdraw()


Label(graph, text = '_______________Moments Of Pride_________________', font=('Beauty Mountains Personal Use',49)).pack(side = TOP, pady = 10) 
  

msg1=" Study Hacks to Improve Your Memory" +"\n"+"\n"+"cuz YOU too can CONQUER"+"\n"+"\n"+"- Speak Out Loud Instead of Simply Reading."+"\n"+"\n"+"-Reward Yourself With A Treat."+"\n"+"\n"+"-Teach What You Have Learned."+"\n"+'\n'+"-Create Mental Associations."+"\n"+'\n'+"- Draw Diagrams."+"\n"+'\n'+"- Times New Roman is " +"\n" +"the Fastest Font to Read."+'\n'+"- Use Apps to Block Distracting Sites."+'\n'+"\n"+"\n"

btnGraphShow=HoverButton(graph,text="Our five stars",compound=LEFT,font=('Beauty Mountains Personal Use',20),activebackground='yellow',bg='white',foreground = "black",command=f14)
btnGraphBack=HoverButton(graph,text="Back",font=('Beauty Mountains Personal Use',20),activebackground='pink',bg='white',foreground = "black",command=f13)
msg2="Good Luck..."+"\n"+'\n'+"Never Give Up."+"\n"+'\n'+"Trust Yourself."+"\n"+'\n'+"U CAN and U WILL " +"\n" +"\n"+"Compete with yourself."+'\n'+"\n"+"\n"+'\n'+"\n"+"\n"+'\n'+"\n"+"\n"


Label(graph, text = msg2,width=30,height=20, font=('Beauty Mountains Personal Use',23),bg='pink',foreground = "black").place(x=750,y=120)
Label(graph, text = msg1,width=30,height=20, font=('Beauty Mountains Personal Use',23),bg='yellow',foreground = "black").place(x=50,y=120)
  

btnGraphShow.pack(side=TOP)
btnGraphBack.pack(pady=5)


info=Toplevel(root)
info.title(" Stu.")
info.geometry("500x500+300+100")
info.withdraw()


#last statement
root.mainloop()		

