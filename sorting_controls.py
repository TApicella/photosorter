from Tkinter import *
import os.path
from shutil import move as smove
from shutil import copy2 as scopy

class SortingControls:
	def __init__(self, app, parent):

		self.shorttargets = app.shorttargets
		self.targetlist = app.targetlist
		self.sc_frame = Frame(parent, height=350, width=400, bd=5, relief=RAISED)
		self.sc_frame.pack_propagate(False) 
		#Don't pack until editing has started
		
		self.move_or_copy = IntVar()
		self.move_or_copy.set(1)
		self.move_btn = Radiobutton(self.sc_frame, text="Move photos", variable = self.move_or_copy, value=1)
		self.copy_btn = Radiobutton(self.sc_frame, text="Copy photos", variable = self.move_or_copy, value=2)
		self.move_btn.pack()
		self.copy_btn.pack()

		self.action_btn = Button(self.sc_frame, text="Process photo", command=lambda: self.process_photo(app))
		self.action_btn.pack()

		self.comment_label = Label(self.sc_frame, text="Add a comment")
		self.comment_box = Entry(self.sc_frame)
		self.comment_label.pack()
		self.comment_box.pack()

	def process_photo(self, app, even=None):
		fsplit = app.current_photo.split('/')
		fname = fsplit[-1]
		full_target_path = app.targetlist[self.shorttargets.index(self.target_dir.get())]
		full_file_path = full_target_path+'/'+fname
		new_file_path = full_file_path
		copynum = 1
		while os.path.isfile(new_file_path):
			new_file_path = self.last_replace(full_file_path, copynum)
			copynum = copynum+1
		if self.move_or_copy.get()==1:
			smove(app.current_photo, new_file_path)
		else:
			scopy(app.current_photo, new_file_path)

		comment_path = full_target_path+"/"+"comments.txt"
		self.write_comment(app, comment_path, fname)
		app.next()

	def write_comment(self, app, cpath, pname, event=None):
		with open(cpath, "a") as f:
			if self.comment_box.get()!=None:
				f.write("Photo: "+pname+"\n")
				if self.comment_box.get() != "":
					f.write("#"+self.comment_box.get()+"\n\n")
			
		app.next()
		
	def delete_comment(self):
		self.comment_box.delete(0, END)
	
	#Use this for inserting a number before the extension
	def last_replace(self, filename, number):
		numstring = "("+str(number)+")."
		temp = filename.rsplit(".", 1)
		return numstring.join(temp)


	def pack(self):
		#Needs to be added after shorttargets has been populated
		self.target_dir = StringVar()
		self.target_dir.set(self.shorttargets[0])
		self.target_options = apply(OptionMenu, (self.sc_frame, self.target_dir) + tuple(self.shorttargets))
		self.target_options.pack()
		
		self.sc_frame.pack()