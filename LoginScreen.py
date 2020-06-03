from tkinter import *
from tkinter import messagebox 
from cx_Oracle import *
import re
import os

window=Tk()

# Function verifying user credentials 
def validateUser(user_fName,user_Pwd):
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,pwd from  users "
		cursor.execute(sql)
		data=cursor.fetchall()
		count=0
		for d in data:
			if user_fName==str(d[0]) and user_Pwd==str(d[1]) :
				count=count+1
		if count==1:
			return True
		else:
			return False
							
	except DatabaseError as e:
		messagebox.showerror(" Galat Kiya ",e)
	
	finally:
		if con is not None:
			con.close()




#Callback function for validating User Name

def validate_name(user_name):
	if user_name.isalpha():
		return True
	elif user_name is "":
		return True 
	else:
		msg="Dear User, Please enter valid user name " +"\n"+ "Hint: Use Alphabets to fill this field  " 
		messagebox.showerror('Oops..',msg)
		return False


# #################
def validateAllFields():
	if v_fName.get() == "":
		messagebox.showerror('Oops..','Dear User,Kindly enter Fullname to proceed ...Please enter all the details and then click REGISTER')
	elif len(v_fName.get()) <2 :
		messagebox.showerror('Oops..','Dear User, Please enter valid name to proceed ...Please enter all the details and then click REGISTER ')
	elif v_pwd.get()=="":
		messagebox.showerror('Oops..','Dear User, Please enter your password to proceed...Please enter all the details and then click REGISTER ')
	elif (not validateUser(v_fName.get(),v_pwd.get())):
		messagebox.showerror('Invalid',"Wrong UserName or password ")
	else:
		messagebox.showinfo('Info',"Congratsssssss!!!!")
		entry_fullname.focus()
		window.destroy()
		# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
		os.system('python prj.py')
			

#Function to clear all User Inputs in fields

def clearAllFields():
	v_fName.set("")
	v_pwd.set("")
	

# Call new user

def callNewUser():
	window.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python RegistrationScreen.py')

# Call new user



window.title("Welcome to User Login Screen ")

# set size and background color of the window 

window.geometry('1280x970+0+0')
window.configure(background="light blue")
window.iconbitmap(r'icon.ico')

#IMAGE  

C = Canvas(window, height=740, width=1280)
filename = PhotoImage(file = "ls.gif")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()


v_fName = StringVar()
v_pwd=StringVar()

# Label widget to display box where u can place text and imgs 

lb_heading=Label(window,text="Login Screen",width=15,font=('Beauty Mountains Personal Use',56),bg="powder blue")

lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="User Name",width=25,font=('Beauty Mountains Personal Use',25),bg="powder blue")
lb_fullname.place(x=90,y=160)

# Entry will allow User to enter any kind of values like numbers,string, special characters
 
entry_fullname=Entry(window,textvariable=v_fName,width='22')
entry_fullname.place(x=382,y=175)

#Register Callback function validate_name

valid_name = window.register(validate_name)

#Pass option value to call back function - validate %P is specifier used to pass to call back function

entry_fullname.config(validate="key",validatecommand=(valid_name,'%P'))

lb_pwd=Label(window,text="Password",width=25,font=('Beauty Mountains Personal Use',25),bg="powder blue")
lb_pwd.place(x=90,y=215)
entry_pwd=Entry(window,show="*",textvariable=v_pwd,width='22')
entry_pwd.place(x=382,y=230)

btn_login = Button(window,text="Login",command = validateAllFields,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',25)).place(x=90,y=274)
btn_clear=Button(window,text="Clear",command = clearAllFields,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',25)).place(x=239,y=274)
btn_new_user=Button(window,text="New User?",command = callNewUser,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',25)).place(x=380,y=274)

# window.mainloop() , this function calls the endless loop of the window , so will remain open till user closes it 

window.mainloop()




