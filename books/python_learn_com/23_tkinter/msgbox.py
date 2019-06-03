#! /usr/bin/python

import Tkinter as tk
import tkMessageBox as tkmb


class App:
	def __init__(self, master):
		b1=tk.Button(master, width=12, text='information', command=self.info).pack()
		b2=tk.Button(master, width=12, text='Error', command=self.error).pack()
		b3=tk.Button(master, width=12, text='Warning', command=self.warn).pack()
		b4=tk.Button(master, width=12, text='Question 1', command=self.askq1).pack()
		b5=tk.Button(master, width=12, text='Question 2', command=self.askq2).pack()
		b6=tk.Button(master, width=12, text='Question 3', command=self.askq3).pack()
		b7=tk.Button(master, width=12, text='Question 4', command=self.askq4).pack()

	def info(self):
		tkmb.showinfo("Info", "The weather is as usual")

	def error(self):
		tkmb.showerror("Error", "There was error !!!")

	def warn(self):
		tkmb.showwarning("Warning", "Be careful...")

	def askq1(self):
		tkmb.askquestion("Question", "Are you OK ?")

	def askq2(self):
		tkmb.askokcancel("Question", "Still you want to do it ?")

	def askq3(self):
		tkmb.askyesno("Question", "Are you OK ?")

	def askq4(self):
		tkmb.askretrycancel("Question", "Could not find it.\nDo you want to try again?")


root = tk.Tk()
root.wm_title('Dialog')
app = App(root)
root.mainloop()


