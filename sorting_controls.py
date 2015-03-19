from Tkinter import *
from PIL import Image, ImageTk

import os
import time
from random import shuffle
from sys import exit

class SortingControls:
	def __init__(self, app, parent):
	
		self.sc_frame = Frame(parent, height=350, width=400, bd=5, relief=RAISED)
		self.sc_frame.pack_propagate(False) 
		#Don't pack until editing has started
		
		self.skip_btn = Button(self.sc_frame, text="Skip", command=app.next)
		self.edited_btn = Button(self.sc_frame, text="Already edited", command=lambda: self.write_comment(app, app.edited))
		self.edit_btn = Button(self.sc_frame, text="I like this one!", command=lambda: self.write_comment(app, app.to_edit))
		self.veto_btn = Button(self.sc_frame, text="I don't like this one :(", command= lambda: self.write_comment(app, app.veto))
		
		self.skip_btn.pack()
		self.edited_btn.pack()
		self.edit_btn.pack()
		self.veto_btn.pack()
		
		self.comment_label = Label(self.sc_frame, text="Add a comment")
		self.comment_box = Entry(self.sc_frame)
		self.comment_label.pack()
		self.comment_box.pack()
	
	def write_comment(self, app, fname, event=None):
		with open(fname, "a") as f:
			if self.comment_box.get()!=None:
				if self.comment_box.get() != "":
					f.write("#"+self.comment_box.get()+"\n")
			f.write(app.current_photo+"\n\n")
		app.next()
		
	def delete_comment(self):
		self.comment_box.delete(0, END)
		
	def pack(self):
		self.sc_frame.pack()
	
	
	
		 
	
	