from Tkinter import *
import tkFileDialog as tkfd
from PIL import Image, ImageTk
from random import shuffle

import os
import time
from sys import exit

class App():
	def __init__(self):
		self.root = Tk()
		self.directorylist = []

		#Testing
		#self.directorylist = ["testfolder"]
		#self.home = os.path.expanduser("~")+"/Pictures/"
		
		#Assuming home directory is current directory
		self.home = ""
		self.toedit = self.home+"toedit.txt"
		self.veto = self.home+"veto.txt"
		self.edited = self.home+"edited.txt"
		self.skip = {}
		#self.init_list()
			
		self.root.geometry('+10+10')
		
		self.skipbtn = Button(self.root, text="Skip", command=self.next)
		#self.skipbtn.grid(column=1, row=0)
		self.editedbtn = Button(self.root, text="Already edited", command=self.editedpic)
		#self.editedbtn.grid(column=1, row=1)
		self.toeditbtn = Button(self.root, text="I like this one!", command=self.editpic)
		#self.toeditbtn.grid(column=1, row=2)
		self.vetobtn = Button(self.root, text="I don't like this one :(", command=self.vetopic)
		#self.vetobtn.grid(column=1, row=3)
		
		self.commentlabel = Label(self.root, text="Add a comment")
		#self.commentlabel.grid(column=1, row=4)
		self.comment = Entry(self.root)
		#self.comment.grid(column=1, row=5)
		
		self.pickdir = Button(self.root, text="Pick directory", command=self.pickdir)
		self.pickdir.grid(column=1, row=5)
		self.picked_dirs_string = ""
		self.picked_dirs = Label(self.root, text=self.picked_dirs_string)
		self.start_sorting = Button(self.root, text="Start sorting", command=self.start_sorting)
		self.current_photo = ""
		#self.update_picture(initial=True)
		#self.picture.bind("<Button-1>", self.next)
		self.root.mainloop()
	
	def start_sorting(self):
		self.init_list()
		self.skipbtn.grid(column=1, row=0)
		self.editedbtn.grid(column=1, row=1)
		self.toeditbtn.grid(column=1, row=2)
		self.vetobtn.grid(column=1, row=3)
		self.commentlabel.grid(column=1, row=4)
		self.comment.grid(column=1, row=5)
		self.pickdir.grid_remove()
		self.start_sorting.grid_remove()
		self.update_picture(initial=True)
		self.picture.bind("<Button-1>", self.next)
		
	
	def pickdir(self):
		pickeddir = tkfd.askdirectory()
		self.directorylist.append(pickeddir)
		print pickeddir
		print self.picked_dirs.winfo_ismapped()
		if self.picked_dirs.winfo_ismapped():
			self.picked_dirs_string = self.picked_dirs_string+"\n"+pickeddir
			self.picked_dirs.configure(text=self.picked_dirs_string)
		else:
			print "Adding dir"
			self.picked_dirs.grid(column=1, row=6)
			self.start_sorting.grid(column=1, row=7)
			self.picked_dirs.configure(text=pickeddir)
		
	def update_picture(self, initial=False):
		self.comment.delete(0, END)
		self.current_photo = self.photolist[self.index][0]
		original = Image.open(self.photolist[self.index][0])
		#print self.photolist[self.index][1]
		ratio = 750.0/float(original.size[1])
		newwidth = int(float(original.size[0]) * ratio)
		resized = original.resize((newwidth, 750),Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(resized)
		if initial:
			self.picture = Label(image=photo)
			self.picture.photo = photo
			self.picture.grid(column=0, row=0, rowspan=5)
		else:
			self.picture.configure(image=photo)
			self.picture.image = photo
		self.root.wm_title(self.photolist[self.index][1]+": "+str(self.index)+" viewed")
	
	def vetopic(self, event=None):
		with open(self.veto, "a") as v:
			if self.comment.get()!=None:
				if self.comment.get() != "":
					v.write("#"+self.comment.get()+"\n")
			v.write(self.current_photo+"\n\n")
			
		self.next()
	
	def editpic(self, event=None):
		with open(self.toedit, "a") as t:
			if self.comment.get()!=None:
				if self.comment.get() != "":
					t.write("#"+self.comment.get()+"\n")
			t.write(self.current_photo+"\n\n")

		self.next()
	
	def editedpic(self, event=None):
		with open(self.edited, "a") as e:
			if self.comment.get()!=None:
				if self.comment.get() != "":
					e.write("#"+self.comment.get()+"\n")
			e.write(self.current_photo+"\n\n")
			
		self.next()
		 
	
	def next(self, event=None):
		self.index = self.index+1
		if self.index >= self.count:
			self.init_list()
		self.update_picture()
	
	def init_list(self):
		if os.path.isfile(self.veto):
				with open(self.veto) as v:
					for line in v:
						if line[0]!="#" and len(line.strip())!=0:
							self.skip[line.strip()]="y"
						
		if os.path.isfile(self.toedit):			
			with open(self.toedit) as t:
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
		print self.directorylist
		for ps in self.directorylist:
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
			#exit()

app=App()