from Tkinter import *
import os.path
from shutil import move as smove
from shutil import copy2 as scopy

class SortingControls:
	def __init__(self, app, parent):

		self.shorttargets = app.shorttargets
		self.targetlist = app.targetlist
		self.sc_frame = Frame(parent, height=600, width=400, bd=5, relief=RAISED)
		self.sc_frame.pack_propagate(False) 
		#Don't pack until editing has started
		
		self.move_or_copy = IntVar()
		self.move_or_copy.set(1)
		self.copy_btn = Radiobutton(self.sc_frame, text="Copy photos", variable = self.move_or_copy, value=1)
		self.move_btn = Radiobutton(self.sc_frame, text="Move photos", variable = self.move_or_copy, value=2)
		self.move_btn.pack()
		self.copy_btn.pack()

		self.comment_label = Label(self.sc_frame, text="Add a comment")
		self.comment_box = Entry(self.sc_frame)
		self.comment_label.pack()
		self.comment_box.pack()
		
		self.sc_choices_bar =Scrollbar(self.sc_frame)
		
		self.sc_choices_list = Listbox(self.sc_frame, selectmode=SINGLE, height=600, width=384, yscrollcommand=self.sc_choices_bar.set)
		self.sc_choices_list.bind("<Double-Button-1>", lambda event: self.process_photo(app))
		
		self.sc_choices_bar.config(command=self.sc_choices_list.yview)

	def process_photo(self, app, event=None):
		selection = self.sc_choices_list.curselection()
		value = self.sc_choices_list.get(selection[0])
		fsplit = app.current_photo.split('/')
		fname = fsplit[-1]
		full_target_path = app.targetlist[self.shorttargets.index(value)]
		full_file_path = full_target_path+'/'+fname
		new_file_path = full_file_path
		copynum = 1
		while os.path.isfile(new_file_path):
			new_file_path = self.last_replace(full_file_path, copynum)
			copynum = copynum+1
		if self.move_or_copy.get()==1:
			scopy(app.current_photo, new_file_path)
		else:
			smove(app.current_photo, new_file_path)
		comment_name = new_file_path.split('/')[-1]
		comment_path = full_target_path+"/"+"comments.txt"
		self.write_comment(app, comment_path, comment_name)
		self.sc_choices_list.selection_clear(0, END)
		app.next()

	def write_comment(self, app, cpath, pname, event=None):
		with open(cpath, "a") as f:
			if self.comment_box.get()!=None:
				if self.comment_box.get().strip() != "":
					f.write("Photo: "+pname+"\n")
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
		for targ in self.shorttargets:
			self.sc_choices_list.insert(END, targ)
		self.sc_choices_list.pack()
		self.sc_choices_bar.pack()
		self.sc_frame.pack()