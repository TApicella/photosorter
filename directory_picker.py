from Tkinter import *

import source_picker as sp


class DirectoryPicker:
	def __init__(self, app, parent):
		self.directorylist = []
		self.sel_frame = Frame(parent, height=400, width=400)
		self.sel_frame.pack_propagate(False)
		self.sel_frame.pack()

		self.source_widget = sp.SourcePicker(app, self)
		
	def update_grid(self):
		self.source_widget.update_grid()