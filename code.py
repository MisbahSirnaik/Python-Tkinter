import socket 
import requests
import os
import sys

try:
	socket.create_connection(("www.google.com",80))
	res=requests.get("https://ipinfo.io/")
	data=res.json()
	city=data['city']
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q=" + city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res1=requests.get(api_address)
	#print(res1)
	data=res1.json()
	temp=data['main']['temp']
	
	#print("shehar= ",city)
	#print("mausam= ",temp,"\u00B0","C",sep='')
except OSError:
	pass

import bs4
import requests

res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
#print(res)

soup=bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})
#print(quote)

text=quote['alt']
#print("text of the day ",text)



from PIL import ImageDraw,Image,ImageFont

#image=Image.open("C:\\Users\\FATIMA\\OneDrive\\Pictures\\wal.jpg")
image=Image.open("prj.jpg")

msg=str(temp)+"\u00B0"+"C"
font_type=ImageFont.truetype('beautymountainspersonaluse-od7z.ttf',96)
#font_type1=ImageFont.truetype('jerseym54-alx9.ttf',36)
font_type1=ImageFont.truetype('arial.ttf',56)
draw=ImageDraw.Draw(image)
draw.text(xy=(50,50),text=city,fill='yellow',font=font_type)
draw.text(xy=(300,50),text=msg,fill='yellow',font=font_type1)
draw.text(xy=(50,300),text=text,fill='yellow',font=font_type)
image.show()

