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
		
		self.dp_frame = Frame(parent, height=400, width=400)
		self.dp_frame.pack_propagate(False)
		self.dp_frame.pack()
		
		self.pd_btn = Button(self.dp_frame, text="Pick directory", command=self.pick_directory)
		self.pd_btn.pack()
		
		self.pd_choices = {}
		
		self.pd_display = Frame(self.dp_frame, height=200, width=400, bd=5, relief=RAISED)
		self.pd_display.pack_propagate(False)
		self.pd_display.pack()
		
		self.pd_choices_label = Label(self.pd_display, text="Selected directories:")
		self.pd_choices_label.pack()
		
		self.start_btn = Button(self.dp_frame, text="Start sorting", command=app.start_sorting, state=DISABLED)
		self.start_btn.pack()
		
	def pick_directory(self):
		picked = tkfd.askdirectory()
		self.directorylist.append(picked)
		spacer="\n"
		self.start_btn.config(state=NORMAL)
		self.pd_choices[picked]=Label(self.pd_display, text=picked, anchor=W, justify=LEFT, wrap=390)
		self.pd_choices[picked].pack(anchor=NW)
			
		
	def update_grid(self):
		self.pd_btn.pack_forget()
		self.start_btn.pack_forget()