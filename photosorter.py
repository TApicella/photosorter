from Tkinter import *
from PIL import Image, ImageTk

import directory_picker as dp
import sorting_controls as sc

import os
from random import shuffle
from sys import exit

class App():
	def __init__(self):
		self.root = Tk()
		
		#Assuming home directory is current directory
		self.home = ""
		self.to_edit = self.home+"to_edit.txt"
		self.veto = self.home+"veto.txt"
		self.edited = self.home+"edited.txt"
		self.skip = {}
		
		self.root.geometry('+10+10')
		
		self.control_frame = Frame(self.root)
		self.control_frame.grid(column=1, row=0)
		
		self.directory_widget = dp.DirectoryPicker(self, self.control_frame)
		self.sourcelist = self.directory_widget.sourcelist
		self.targetlist = self.directory_widget.targetlist
		
		self.sorting_widget = sc.SortingControls(self, self.control_frame)
		
		self.current_photo = ""
		self.root.mainloop()
	
	def start_sorting(self):
		self.init_list()
		self.sorting_widget.pack()
		self.directory_widget.update_grid()
		self.update_picture(initial=True)
		self.picture.bind("<Button-1>", self.next)
		
	
	def update_picture(self, initial=False):
		self.sorting_widget.delete_comment()
		self.current_photo = self.photolist[self.index][0]
		original = Image.open(self.photolist[self.index][0])
		ratio = 750.0/float(original.size[1])
		newwidth = int(float(original.size[0]) * ratio)
		resized = original.resize((newwidth, 750),Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(resized)
		if initial:
			self.picture = Label(image=photo)
			self.picture.photo = photo
			self.picture.grid(column=0, row=0)
		else:
			self.picture.configure(image=photo)
			self.picture.image = photo
		self.root.wm_title(self.photolist[self.index][1]+": "+str(self.index)+" viewed")
	
	def next(self, event=None):
		self.index = self.index+1
		print self.index
		print self.count
		print
		if self.index >= self.count:
			self.init_list()
		self.update_picture()
	
	def init_list(self):
		if os.path.isfile(self.veto):
			with open(self.veto) as v:
				for line in v:
					if line[0]!="#" and len(line.strip())!=0:
						self.skip[line.strip()]="y"
						
		if os.path.isfile(self.to_edit):			
			with open(self.to_edit) as t:
				for line in t:
					if line[0]!="#" and len(line.strip())!=0:
						self.skip[line.strip()]="y"
					
		if os.path.isfile(self.edited):
			with open(self.edited) as e:
				for line in e:
					if line[0]!="#" and len(line.strip())!=0:
						self.skip[line.strip()]="y"
					
		self.photolist = set()
		self.index = 0
		print self.sourcelist
		for ps in self.sourcelist:
			for dirName, subdirList, fileList in os.walk(self.home+ps):
				for fname in fileList:
					fullname = dirName+"/"+fname
					ext = fullname[-4:]
					if ext.lower()==".jpg" or ext.lower()==".png": 
						if fullname not in self.skip:
							self.photolist.add((fullname, fname))
						else:
							print "Skipping "+fullname

		self.photolist = list(self.photolist)
		shuffle(self.photolist)
		
		self.count = len(self.photolist)
		print self.count
		if self.count==0:
			print "No pictures found!"
			exit()
			
	

app=App()