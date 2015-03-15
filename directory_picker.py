from Tkinter import *
import tkFileDialog as tkfd
from PIL import Image, ImageTk
from ScrolledText import ScrolledText
from random import shuffle

import os
import time
from sys import exit

class DirectoryPicker:
	def __init__(self, app, parent):
		self.directorylist = []
		self.appgrid = app.appgrid
		self.pd_btn = Button(parent, text="Pick directory", command=self.pick_directory)
		self.pd_btn.grid(column=self.appgrid["pd_btn_col"], row=self.appgrid["pd_btn_row"])
		self.pd_choices = ""
		self.pd_display = ScrolledText(parent)
		self.pd_display.insert(END, self.pd_choices)
		self.pd_display.config(state=DISABLED)
		self.start_btn = Button(parent, text="Start sorting", command=app.start_sorting)
		
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
			self.pd_display.grid(column=self.appgrid["pd_display_setup_col"], row=self.appgrid["pd_display_setup_row"])
			self.start_btn.grid(column=self.appgrid["start_btn_col"], row=self.appgrid["start_btn_row"])
			self.pd_choices = picked
			self.pd_display.config(state=NORMAL)
			self.pd_display.insert(END, self.pd_choices)
			self.pd_display.config(state=DISABLED)
			
	def update_grid(self):
		self.pd_btn.grid_remove()
		self.start_btn.grid_remove()
		self.pd_display.grid(column=self.appgrid["pd_display_running_col"], row=self.appgrid["pd_display_running_row"])