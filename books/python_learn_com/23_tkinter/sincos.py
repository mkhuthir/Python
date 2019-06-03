#! /usr/bin/python

from Tkinter import *
import math

class App:
	def __init__(self, master):
		canvas = Canvas(master, width=400, height=400)
		canvas.pack()
		S=10
		for x in range(1,400):
			canvas.create_line((x-1)*S,math.sin(x-1)*S+200,x*S,math.sin(x)*S+200,fill='green',width=1)
			canvas.create_line((x-1)*S,math.cos(x-1)*S+200,x*S,math.cos(x)*S+200,fill='red',width=1)


root = Tk()
root.wm_title('Canvas Test')
app = App(root)
root.mainloop()


