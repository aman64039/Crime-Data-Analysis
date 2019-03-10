import Tkinter
import tkMessageBox
from Tkinter import *
from PIL import Image
from PIL import ImageTk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
global window

window= Tkinter.Tk()
window.title("Amanpreet Cime Analysis")
window.geometry("1200x1000")

image= Image.open('/home/aman/Desktop/MAJORPROJECT/Crime.jpg')
img = ImageTk.PhotoImage(image)
background_label = Label(window, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def data1():
	#read the data from the csv file and print
	data1 = pd.read_csv('data1.csv')
	data=pd.DataFrame(data1)
	data=data.sort('Year')


	Year=data['Year']
	print data['Year']

	#filter the data mean we have tp print only from arrest to year mean  columns
	FilterData = data.ix[:,'Arrest':'NonArrest']


	"""# export data
	my_data = [Year, FilterData]
	result = pd.concat(my_data,axis=1)
	result.to_csv('result.csv')
	result.to_excel('result.xlsx')
	result.to_html('result.htm')
	result.to_clipboard()
"""

	# generate a figure
	plt.figure(1)
	plt.plot(Year,FilterData[['Arrest','NonArrest']])
	#plt.plot(a)
	plt.savefig('plot.png')
	plt.show()
	
"""
	# generate a figure
	ax = data[['Arrest','NonArrest']].plot(kind='bar', title ="CCLV Crime", figsize=(15, 	10), legend=True, fontsize=12)
	ax.plot(Year,FilterData[['Arrest','NonArrest']])
	ax.set_xticklabels(data['Year'])
	ax.set_xlabel("Year", fontsize=12)
	ax.set_ylabel("Count", fontsize=12)
	#ax.set_xlim([2000,2018])
	plt.show()
"""	
def data2():
	#read the data from the csv file and print
	data1 = pd.read_csv('data2.csv')
	data=pd.DataFrame(data1)
	data=data.sort('Year')


	Year=data['Year']


	#filter the data mean we have tp print only from arrest to year mean  columns
	FilterData = data.ix[:,'Arrest':'NonArrest']


	"""# export data
	my_data = [Year, FilterData]
	result = pd.concat(my_data,axis=1)
	result.to_csv('result.csv')
	result.to_excel('result.xlsx')
	result.to_html('result.htm')
	result.to_clipboard()
"""
	"""
	# generate a figure
	plt.figure(1)
	plt.plot(Year,FilterData[['Arrest','NonArrest']])
	#plt.plot(a)
	plt.savefig('plot.png')
	plt.show()
	
	"""
	# generate a figure
	ax = data[['Arrest','NonArrest']].plot(kind='bar', title ="ARSON Crime", figsize=(15, 	10), legend=True, fontsize=12)
	ax.plot(Year,FilterData[['Arrest','NonArrest']])
	ax.set_xticklabels(data['Year'])
	ax.set_xlabel("Year", fontsize=12)
	ax.set_ylabel("Count", fontsize=12)
	#ax.set_xlim([2000,2018])
	plt.show()


def data3():
	#read the data from the csv file and print
	data1 = pd.read_csv('data3.csv')
	data=pd.DataFrame(data1)
	data=data.sort('Year')


	Year=data['Year']


	#filter the data mean we have tp print only from arrest to year mean  columns
	FilterData = data.ix[:,'Arrest':'NonArrest']


	"""# export data
	my_data = [Year, FilterData]
	result = pd.concat(my_data,axis=1)
	result.to_csv('result.csv')
	result.to_excel('result.xlsx')
	result.to_html('result.htm')
	result.to_clipboard()
"""
	"""
	# generate a figure
	plt.figure(1)
	plt.plot(Year,FilterData[['Arrest','NonArrest']])
	#plt.plot(a)
	plt.savefig('plot.png')
	plt.show()
	
	"""
	# generate a figure
	ax = data[['Arrest','NonArrest']].plot(kind='bar', title ="ASSAULT Crime", figsize=(15, 	10), legend=True, fontsize=12)
	ax.plot(Year,FilterData[['Arrest','NonArrest']])
	ax.set_xticklabels(data['Year'])
	ax.set_xlabel("Year", fontsize=12)
	ax.set_ylabel("Count", fontsize=12)
	#ax.set_xlim([2000,2018])
	plt.show()


def data4():
	#read the data from the csv file and print
	data1 = pd.read_csv('data4.csv')
	data=pd.DataFrame(data1)
	data=data.sort('Year')


	Year=data['Year']


	#filter the data mean we have tp print only from arrest to year mean  columns
	FilterData = data.ix[:,'Arrest':'NonArrest']


	"""# export data
	my_data = [Year, FilterData]
	result = pd.concat(my_data,axis=1)
	result.to_csv('result.csv')
	result.to_excel('result.xlsx')
	result.to_html('result.htm')
	result.to_clipboard()
"""
	"""
	# generate a figure
	plt.figure(1)
	plt.plot(Year,FilterData[['Arrest','NonArrest']])
	#plt.plot(a)
	plt.savefig('plot.png')
	plt.show()
	
	"""
	# generate a figure
	ax = data[['Arrest','NonArrest']].plot(kind='bar', title ="BATTERY Crime", figsize=(15, 	10), legend=True, fontsize=12)
	ax.plot(Year,FilterData[['Arrest','NonArrest']])
	ax.set_xticklabels(data['Year'])
	ax.set_xlabel("Year", fontsize=12)
	ax.set_ylabel("Count", fontsize=12)
	#ax.set_xlim([2000,2018])
	plt.show()


def data5():
	#read the data from the csv file and print
	data1 = pd.read_csv('data5.csv')
	data=pd.DataFrame(data1)
	data=data.sort('Year')
	Year=data['Year']


	#filter the data mean we have tp print only from arrest to year mean  columns
	FilterData = data.ix[:,'Arrest':'NonArrest']


	"""# export data
	my_data = [Year, FilterData]
	result = pd.concat(my_data,axis=1)
	result.to_csv('result.csv')
	result.to_excel('result.xlsx')
	result.to_html('result.htm')
	result.to_clipboard()
"""
	"""
	# generate a figure
	plt.figure(1)
	plt.plot(Year,FilterData[['Arrest','NonArrest']])
	#plt.plot(a)
	plt.savefig('plot.png')
	plt.show()
	
	"""
	# generate a figure
	ax = data[['Arrest','NonArrest']].plot(kind='bar', title ="BURGLARY	 Crime", figsize=(15, 	10), legend=True, fontsize=12)
	ax.plot(Year,FilterData[['Arrest','NonArrest']])
	ax.set_xticklabels(data['Year'])
	ax.set_xlabel("Year", fontsize=12)
	ax.set_ylabel("Count", fontsize=12)
	#ax.set_xlim([2000,2018])
	plt.show()
def exit():
	window.destroy()


lbl = Tkinter.Label(window, text= "Top 5 Crimes in CHICAGO in Between 2002 to 2018 are CCLV,ARSON,ASSAULT,\nBATTERY and BURGLARY. Please click thebutten for more imformation on these \nCrimes. This Data is  Analysis with the help of Hive and Visulization with the help of \nPython Pandas.This Analysis and Visulization is Implimented by\n Er.Amanpreet Singh(1421708).",font=("Arial Bold", 18),bg="#EBADAD")
lbl.pack()
B1 = Tkinter.Button(window, text ="CCLV", command = data1, width=15, height=5, bd=10,bg="SeaGreen2")
B2= Tkinter.Button(window, text ="ARSON", command = data2, width=15, height=5, bd=10,bg="SeaGreen2")

B3 = Tkinter.Button(window, text ="ASSAULT", command = data3, width=15, height=5, bd=10,bg="SeaGreen2")

B4= Tkinter.Button(window, text ="BATTERY", command = data4, width=15, height=5, bd=10,bg="SeaGreen2")

B5 = Tkinter.Button(window, text ="BURGLARY", command = data5, width=15, height=5, bd=10,bg="SeaGreen2")
B6=Tkinter.Button(window,text="Exit",command=exit,width=15,height=5,bd=10,bg="red")
B1.place(relx=.1, rely=.3, anchor="c")
B2.place(relx=.3, rely=.3, anchor="c")
B3.place(relx=.5, rely=.3, anchor="c")
B4.place(relx=.7, rely=.3, anchor="c")
B5.place(relx=.9, rely=.3, anchor="c")
B6.place(relx=.9, rely=.9, anchor="c")
window.mainloop()






















