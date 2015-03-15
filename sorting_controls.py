from Tkinter import *
from PIL import Image, ImageTk

import os
import time
from random import shuffle
from sys import exit

class SortingControls:
	def __init__(self, app, parent):
		self.skip_btn = Button(parent, text="Skip", command=app.next)
		self.edited_btn = Button(parent, text="Already edited", command=lambda: self.write_comment(app, app.edited))
		self.edit_btn = Button(parent, text="I like this one!", command=lambda: self.write_comment(app, app.to_edit))
		self.veto_btn = Button(parent, text="I don't like this one :(", command= lambda: self.write_comment(app, app.veto))
		
		self.comment_label = Label(parent, text="Add a comment")
		self.comment_box = Entry(parent)
	
	def write_comment(self, app, fname, event=None):
		with open(fname, "a") as f:
			if self.comment_box.get()!=None:
				if self.comment_box.get() != "":
					f.write("#"+self.comment_box.get()+"\n")
			f.write(app.current_photo+"\n\n")
		app.next()
		
	def grid(self, appgrid):	
		self.skip_btn.grid(column=appgrid["skip_btn_col"], row=appgrid["skip_btn_row"])
		self.edited_btn.grid(column=appgrid["edited_btn_col"], row=appgrid["edited_btn_row"])
		self.edit_btn.grid(column=appgrid["edit_btn_col"], row=appgrid["edit_btn_row"])
		self.veto_btn.grid(column=appgrid["veto_btn_col"], row=appgrid["veto_btn_row"])
		self.comment_label.grid(column=appgrid["comment_label_col"], row=appgrid["comment_label_row"])
		self.comment_box.grid(column=appgrid["comment_box_col"], row=appgrid["comment_box_row"])
		
	def delete_comment(self):
		self.comment_box.delete(0, END)
		
	
	
	
	
		 
	
	