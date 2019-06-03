#! /usr/bin/python3

from tkinter import *
import random

class App:
	def __init__(self, master):
		canvas = Canvas(master, width=400, height=400)
		canvas.pack()

		y, py, px = 0, 0, 0
		for x in range(1,400,2):
			y=random.randint(1,400)
			canvas.create_line(px,py,x,y,fill='green',width=1)
			px=x
			py=y


root = Tk()
root.wm_title('Canvas Test')
app = App(root)
root.mainloop()


