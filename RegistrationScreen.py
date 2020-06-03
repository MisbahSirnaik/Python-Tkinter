#import statements

from tkinter import *
from validate_email import validate_email
from tkinter import messagebox 
from cx_Oracle import *
import re
import os

# Creating the main window

window=Tk()

#Callback function for validating User Phone No

def validate_phoneno(user_phoneno):
	if user_phoneno.isdigit():
		return True
	elif user_phoneno is "":
		return True 
	else:
		messagebox.showerror('Oops..','Dear User, Please enter valid phone no ')
		return False

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

#Function for validating User Email ID

def isValidEmail(user_email):
	if len(user_email)>7:
		if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1-3})(]?)$",user_email) != None:
			return True
		return False
	else:
		messagebox.showerror('Oops..','Dear User, Kindly enter valid email address ')
		return False

#Function checks for Strong password

def isStrongPwd(user_pwd):
	if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',user_pwd))==True):
		return True
	else:
	
		return False
	

#Function for validating all other User Input Fields
# pwd,confirmpwd,Phone No,Email Id,Country

def validateAllFields():
	con=None
	try:
		con=connect("system/abc123")
		name=entry_fullname.get()
		pwd=entry_pwd.get()
		phone=entry_phoneno.get()
		email=entry_email.get()
		cursor=con.cursor()
		if name == "":
			messagebox.showerror('Oops..','Dear User,Kindly enter Fullname to proceed ...Please enter all the details and then click REGISTER')
		elif len(name) <2 :
			messagebox.showerror('Oops..','Dear User, Please enter valid name to proceed ...Please enter all the details and then click REGISTER ')
		elif pwd=="":
			messagebox.showerror('Oops..','Dear User, Please enter your password to proceed...Please enter all the details and then click REGISTER ')
		elif (not isStrongPwd(pwd)):
			msg="Dear User, Please enter strong password " +"\n"+ "Hint: Always use a combination of alphanumeric letters for strong password"
			messagebox.showerror('Oops..',msg)		
		elif v_confirmPwd.get()=="":
			messagebox.showerror('Oops..','Dear User, Please confirm your password to proceed...Please enter all the details and then click REGISTER ')
		elif pwd!=v_confirmPwd.get():
			messagebox.showerror('Oops..','Dear User, Password Mismatch...Password does not match with confirmed password  ')
		elif phone=="":
			messagebox.showerror('Oops..','Dear User, Kindly enter Phone No to proceed...Please enter all the details and then click REGISTER ')
		elif len(phone) !=10 :
			messagebox.showerror('Oops..','Dear User, Please enter 10 digit Phone Number to ...Please enter all the details and then click REGISTER')
		elif email=="":
			messagebox.showerror('Oops..','Dear User, Kindly enter email id to proceed ...Please enter all the details and then click REGISTER')
		elif v_gender.get()<1:
			messagebox.showerror('Oops..','Dear User, Please select Gender to proceed...Please enter all the details and then click REGISTER ')
		elif v_country.get()=="" or v_country.get()=="Select Your Country":
			messagebox.showerror('Oops..','Dear User, Kindly enter Country to proceed ...Please enter all the details and then click REGISTER')
		elif v_pwd.get()!=v_confirmPwd.get():
			messagebox.showerror('Oops..','Dear User, Password Mismatch...Password does not match with confirmed password  ')
		elif (not validate_email(email)):
			messagebox.showerror('Oops','Invalid email id ')
		else:
			sql="insert into users values('%s','%s','%s','%s')"
			args=(name,pwd,phone,email)
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+ " record inserted "
			messagebox.showinfo("Sahi Kiya ",msg)
			entry_fullname.delete(0,END)
			entry_pwd.delete(0,END)
			entry_confirm_pwd.delete(0,END)
			entry_phoneno.delete(0,END)
			entry_email.delete(0,END)
			v_gender.set(" ")
			v_country.set("Select Your Country")
			entry_fullname.focus()
	
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

	

#Function to clear all User Inputs in fields

def clearAllFields():
	v_fName.set("")
	v_pwd.set("")
	v_confirmPwd.set("")
	v_phoneNo.set("")
	v_emailId.set("")
	v_gender.set(" ")
	v_country.set("Select Your Country")

# Call new screen 

def callNewScreen():
	window.destroy()
	# same loc mein file ho toh ('nayi_screen_ka_naam.py') else ( python 'nayi_screen_ka_naam'.py)
	os.system('python LoginScreen.py')

window.title("Welcome to User Registration Screen ")

# set size and background color of the window 

window.geometry('1280x970+0+0')
window.iconbitmap(r'icon.ico')
window.configure(background="black")
#window.configure()

# window.wm_attributes('-alpha', 0.9) for making window transparent

C = Canvas(window, height=740, width=1280)
filename = PhotoImage(file = "p2.gif")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()



v_fName = StringVar()
v_pwd=StringVar()
v_confirmPwd=StringVar()
v_phoneNo=StringVar()
v_emailId = StringVar()
v_gender=IntVar()      # here ...integer reason:-  
v_country=StringVar()


# Label widget to display box where u can place text and imgs 

lb_heading=Label(window,text="   Registration Screen",width=27,font=('Beauty Mountains Personal Use',56),bg='navy blue',foreground = "white")
lb_heading.place(x=90,y=30)   
   
lb_fullname=Label(window,text="User Name",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_fullname.place(x=90,y=140)


# Entry will allow User to enter any kind of values like numbers,string, special characters
 
entry_fullname=Entry(window,textvariable=v_fName,width='35')
entry_fullname.place(x=689,y=155)

#Register Callback function validate_name

valid_name = window.register(validate_name)

#Pass option value to call back function - validate %P is specifier used to pass to call back function

entry_fullname.config(validate="key",validatecommand=(valid_name,'%P'))


lb_pwd=Label(window,text="Password",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_pwd.place(x=90,y=194)

entry_pwd=Entry(window,show="*",textvariable=v_pwd,width='35')
entry_pwd.place(x=689,y=212)



lb_confirm_pwd=Label(window,text="Confirm Password",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_confirm_pwd.place(x=90,y=249)
entry_confirm_pwd=Entry(window,show="*",textvariable=v_confirmPwd,width='35')
entry_confirm_pwd.place(x=745,y=268)

lb_phoneno=Label(window,text="Phone No.",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_phoneno.place(x=90,y=295)
entry_phoneno=Entry(window,textvariable=v_phoneNo,width='35')
entry_phoneno.place(x=689,y=306)


#Register Callback function validate_phoneno

valid_phoneno = window.register(validate_phoneno)

#Pass option value to call back function - validate %P is specifier used to pass to call back function

entry_phoneno.config(validate="key",validatecommand=(valid_phoneno,'%P'))

# Label widget to display box where u can place text and imgs 

lb_email=Label(window,text="Email",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_email.place(x=90,y=335)
entry_email=Entry(window,textvariable=v_emailId,width='35')
entry_email.place(x=689,y=356)

lb_gender=Label(window,text="Gender",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_gender.place(x=90,y=375)

Radiobutton(window,text="Male",bg="light blue",font=('Beauty Mountains Personal Use',16),padx=5,variable=v_gender,value=1).place(x=689,y=377)
Radiobutton(window,text="Female",bg="light blue",font=('Beauty Mountains Personal Use',16),padx=20,variable=v_gender,value=2).place(x=759,y=377)


lb_country=Label(window,text="Country",width=63,font=('Beauty Mountains Personal Use',25),bg="light blue")
lb_country.place(x=90,y=430)
list_country={'India','Canada','UK','Nepal','Germany'};

# *list_country shows all items in the list vertically in drop down ..* ko nikala to horizontal milega

droplist=OptionMenu(window,v_country,*list_country)
droplist.config(width=16,bg="light blue")
v_country.set('Select Your Country')
droplist.place(x=689,y=435)

btn_register = Button(window,text="Register",command = validateAllFields,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',20)).place(x=460,y=500)
btn_clear=Button(window,text="Clear",command = clearAllFields,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',20)).place(x=570,y=500)
btn_existing_user=Button(window,text="Existing User?",command = callNewScreen,bg="dark blue",fg="white",font=('Beauty Mountains Personal Use',20)).place(x=658,y=500)

# window.mainloop() , this function calls the endless loop of the window , so will remain open till user closes it 

window.mainloop()












