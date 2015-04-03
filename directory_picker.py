from Tkinter import *

import picker_widget as pw


class DirectoryPicker:
	def __init__(self, app, parent):
		self.sourcelist = []
		self.shortsources = []
		self.targetlist = []
		self.shorttargets = []
		
		self.sel_frame = Frame(parent, height=400, width=400)
		self.sel_frame.pack_propagate(False)
		self.sel_frame.pack()

		self.source_widget = pw.Picker(app, self, "source")
		self.target_widget = pw.Picker(app, self, "target")
		
		self.start_btn = Button(self.sel_frame, text="Start sorting", command=app.start_sorting, state=DISABLED)
		self.start_btn.pack()

	def update_grid(self):
		self.start_btn.pack_forget()
		self.source_widget.update_grid()
		self.target_widget.update_grid()