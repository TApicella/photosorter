from Tkinter import *
import tkFileDialog as tkfd


class Picker:
	def __init__(self, app, parent, dir_type):
		self.directorylist = []
		self.parent= parent
		self.dir_type = dir_type
		
		self.dp_frame = Frame(parent.sel_frame, height=175, width=400, bd=5, relief=RAISED)
		self.dp_frame.pack_propagate(False)
		self.dp_frame.pack()
		
		self.pd_btn = Button(self.dp_frame, text="Pick destination directory", command=self.pick_directory)
		self.pd_btn.pack()
		
		self.pd_choices = {}
		
		self.pd_display = Frame(self.dp_frame, height=100, width=400)
		self.pd_display.pack_propagate(False)
		self.pd_display.pack()
		
		self.pd_choices_label = Label(self.pd_display, text="Selected destinations:")
		self.pd_choices_label.pack()

		self.pd_choices_bar =Scrollbar(self.pd_display)
		self.pd_choices_list = Listbox(self.pd_display, selectmode=EXTENDED, height=100, width=384, yscrollcommand=self.pd_choices_bar.set)
		self.pd_choices_list.pack()
		self.pd_choices_bar.config(command=self.pd_choices_list.yview)
		
		self.remove_btn = Button(self.dp_frame, text="Remove selected", command=self.remove_dirs, state=DISABLED)
		self.remove_btn.pack()

	def pick_directory(self):
		picked = tkfd.askdirectory()
		self.directorylist.append(picked)
		if self.dir_type=="target":
			self.parent.targetlist.append(picked)
		else:
			self.parent.sourcelist.append(picked)
		
		dir_length = len(picked)
		if dir_length>50:
			picked_split = picked.split('/')
			picked_split = picked_split[1:]
			picked_split[0] = '/'+picked_split[0]
			if len(".../"+picked_split[-1])>50:
				fpicked=".../"+picked_split[-1]
				fpicked = fpicked[0:50]
			elif (len(picked_split[0]+"/"+picked_split[-1]))>50:
				fpicked=".../"+picked_split[-1]
			else:
				prefix = picked_split[0]
				suffix = "/.../"+picked_split[-1]
				for dir in picked_split[1:]:
					if len(prefix+"/"+dir+suffix)<50:
						prefix=prefix+"/"+dir
					else:
						fpicked=prefix+suffix
		else:
			fpicked = picked
		self.pd_choices_list.insert(END, fpicked)
		self.remove_btn.config(state=NORMAL)
		self.parent.start_btn.config(state=NORMAL)
		if len(self.directorylist)>4:
			self.pd_choices_list.pack_forget()
			self.remove_btn.pack_forget()
			self.pd_choices_bar.pack(side=RIGHT, fill=Y)
			self.pd_choices_list.pack()
			self.remove_btn.pack()
		
	def remove_dirs(self):
		to_delete = list(self.pd_choices_list.curselection())
		while len(to_delete)>0:
			index=to_delete.pop()
			self.directorylist.pop(int(index))
			if self.dir_type=="target":
				self.parent.targetlist.pop(int(index))
			else:
				self.parent.sourcelist.pop(int(index))
			self.pd_choices_list.delete(index)
			to_delete = list(self.pd_choices_list.curselection())
		if len(self.directorylist)<=4:
			self.pd_choices_list.pack_forget()
			self.remove_btn.pack_forget()
			self.pd_choices_bar.pack_forget()
			self.pd_choices_list.config(width=400)
			self.pd_choices_list.pack()
			self.remove_btn.pack()
		if len(self.directorylist)==0:
			self.remove_btn.config(state=DISABLED)
			self.parent.start_btn.config(state=DISABLED)

	def update_grid(self):
		self.pd_btn.pack_forget()
		self.remove_btn.pack_forget()