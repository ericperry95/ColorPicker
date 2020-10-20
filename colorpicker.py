# colorpicker.py
# author: Eric Perry 
# 10/20/20

# GUI program to choose a color and see hex/RGB

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
	# displays the results of picking a color
	def __init__(self):
		# sets up the window and the widgets
		EasyFrame.__init__(self, title = "Color Picker")

		# labels and output fields
		self.addLabel(text = "R", row = 0, column = 0)
		self.addLabel(text = "G", row = 1, column = 0)
		self.addLabel(text = "B", row = 2, column = 0)
		self.addLabel(text = "Color", row = 3, column = 0)

		self.r = self.addIntegerField(value = 0, row = 0, column = 1)
		self.g = self.addIntegerField(value = 0, row = 1, column = 1)
		self.b = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hex = self.addTextField(text = "#000000", row = 3, column = 1)

		# canvas widget with an initial black color background
		self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")

		# command button
		self.addButton(text = "Choose Color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)
	
	# event handling method	
	def chooseColor(self):
		# pops up a color choose from the OS and outputs the results
		colorTuple = tkinter.colorchooser.askcolor() 
		if not colorTuple[0]:
			return 
		((r, g, b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString

def main():
	# instantiaties and pops up the window 
	ColorPicker().mainloop()

# global call to the main() function
main()

