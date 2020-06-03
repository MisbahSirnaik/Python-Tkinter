from cx_Oracle import *
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def f12():
	root.withdraw()
	graph.deiconify()
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