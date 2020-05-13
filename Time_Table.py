import random
from Time_Schedule import DAY,TIME,TOPICS,printDAY         # This is the module created by me where all the function and the variables are defined
import datetime
from tkinter import *
import tkinter as tk

print(random.randint(1,12))
print(random.randint(2015,2019))
def show():

	timeTable = {}
	flag=0

	for i in range(len(TIME)):
		topic = TOPICS[random.randint(0,len(TOPICS)-1)]

		if(topic=='PYTHON 7 HOURS'):
			timeTable[TIME[i]] = topic
			flag=1

		elif(flag==0):
			timeTable[TIME[i]] = topic


	i=1
	for key,value in timeTable.items():
		sub = key + ": "+ value
		if(i==1):
			First.config(text=sub)
		elif(i==2):
			Second.config(text=sub)
		elif(i==3):
			Third.config(text=sub)
		elif(i==4):
			Fourth.config(text=sub)
		elif(i==5):
			Fifth.config(text=sub)
		elif(i==6):
			Sixth.config(text=sub)

		i+=1



if __name__ == '__main__':

	root = tk.Tk()
	root.geometry("650x400")

	root.title("Time Table Generator")

	Date = Label(root,text = datetime.date.today(),font = 'times 15 bold')
	Date.grid(row=1,column=1,padx=50,pady=1)

	DAY = Label(root,text = printDAY(),font = 'times 15 bold')
	DAY.grid(row=2,column=1,padx=50,pady=1)

	Enter = Label(root,text = "<----------------------------------------------------------------------->",font = 'times 15 bold')
	Enter.grid(row=3,column=1,padx=50,pady=1)


	First = Label(root, font='times 15 bold')
	First.grid(row=4, column=1,padx=50,pady=10)

	Second = Label(root, font='times 15 bold')
	Second.grid(row=8, column=1,padx=50,pady=10)

	Third = Label(root, font='times 15 bold')
	Third.grid(row=12, column=1,padx=50,pady=10)

	Fourth = Label(root, font='times 15 bold')
	Fourth.grid(row=16, column=1,padx=50,pady=10)

	Fifth = Label(root, font='times 15 bold')
	Fifth.grid(row=20, column=1,padx=50,pady=10)

	Sixth = Label(root, font='times 15 bold')
	Sixth.grid(row=24, column=1,padx=50,pady=10)


	show()

	root.mainloop()






	
