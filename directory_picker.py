from Tkinter import *
import tkFileDialog as tkfd
from PIL import Image, ImageTk
from random import shuffle

import os
import time
from sys import exit

class DirectoryPicker:
	def __init__(self, app, parent):
		self.directorylist = []
		self.pd_button = Button(parent, text="Pick directory", command=self.pick_directory)
		self.pd_button.grid(column=1, row=5)
		self.pd_choices = ""
		self.pd_display = Text(parent)
		self.pd_display.insert(END, self.pd_choices)
		self.pd_display.config(state=DISABLED)
		self.start_button = Button(parent, text="Start sorting", command=app.start_sorting)
		
	def pick_directory(self):
		picked = tkfd.askdirectory()
		self.directorylist.append(picked)
		spacer="\n"
		if self.pd_display.winfo_ismapped():
			self.pd_choices = self.pd_choices+spacer+picked
			self.pd_display.config(state=NORMAL)
			self.pd_display.delete(1.0, END)
			self.pd_display.insert(END, self.pd_choices)
			self.pd_display.config(state=DISABLED)
		else:
			print "Adding dir"
			self.pd_display.grid(column=1, row=6)
			self.start_button.grid(column=1, row=7)
			self.pd_choices = picked
			self.pd_display.config(state=NORMAL)
			self.pd_display.insert(END, self.pd_choices)
			self.pd_display.config(state=DISABLED)
			
	def grid_remove(self):
		self.pd_button.grid_remove()
		self.start_button.grid_remove()