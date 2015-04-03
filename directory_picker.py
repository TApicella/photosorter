from Tkinter import *

import source_picker as sp
import target_picker as tp


class DirectoryPicker:
	def __init__(self, app, parent):
		self.sourcelist = []
		self.targetlist = []
		self.sel_frame = Frame(parent, height=400, width=400)
		self.sel_frame.pack_propagate(False)
		self.sel_frame.pack()

		self.source_widget = sp.SourcePicker(app, self)
		self.target_widget = tp.TargetPicker(app, self)
		
		self.start_btn = Button(self.sel_frame, text="Start sorting", command=app.start_sorting, state=DISABLED)
		self.start_btn.pack()

	def update_grid(self):
		self.start_btn.pack_forget()
		self.source_widget.update_grid()
		self.target_widget.update_grid()