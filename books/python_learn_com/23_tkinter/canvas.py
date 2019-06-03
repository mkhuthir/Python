#! /usr/bin/python

from Tkinter import *

class App:
	def __init__(self, master):
		canvas = Canvas(master, width=400, height=400)
		canvas.pack()

		canvas.create_line(100, 120, 110, 120, fill='black', width=2) 	# Line 1
		canvas.create_line(110, 120, 120, 110, fill='black', width=2)	# 2
		canvas.create_line(120, 110, 130, 120, fill='black', width=2)	# 3
		canvas.create_line(130, 120, 130, 130, fill='black', width=2)	# 4
		canvas.create_line(130, 130, 120, 130, fill='black', width=2)	# 5
		canvas.create_line(120, 130, 120, 140, fill='black', width=2)	# 6
		canvas.create_line(120, 140, 110, 140, fill='black', width=2)	# 7
		canvas.create_line(110, 140, 110, 130, fill='black', width=2)	# 8
		canvas.create_line(110, 130, 100, 130, fill='black', width=2)	# 9
		canvas.create_line(100, 130, 100, 120, fill='black', width=2)	# 10


		canvas.create_oval(150, 150, 200, 200, fill='red')

		canvas.create_rectangle(210, 210, 240, 240, fill='green')





root = Tk()
root.wm_title('Canvas Test')
app = App(root)
root.mainloop()


