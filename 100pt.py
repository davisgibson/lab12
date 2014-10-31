#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the buttons, the oval moves to the left or right
moveLeft = -10
moveRight = 10
moveDown = 10
moveUp = -10
from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")
oval2 = drawpad.create_oval(170,170,310,310, fill='blue')
oval3 = drawpad.create_oval(180,180,300,300, fill='red')
oval4 = drawpad.create_oval(190,190,290,290, fill='blue')
oval5 = drawpad.create_oval(200,200,280,280, fill='red')
oval6 = drawpad.create_oval(210,210,270,270, fill='blue')
oval7 = drawpad.create_oval(220,220,260,260, fill='red')
oval8 = drawpad.create_oval(230,230,250,250, fill='blue')

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=1,column=0)
		self.button1.bind("<Button-1>", self.button1Click)
	        # Add a second button!
	        
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "yellow")
		self.button2.grid(row=1,column=2)
		self.button2.bind("<Button-1>", self.button2Click)	
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="up", background= "blue")
		self.button3.grid(row=0,column=1)
		self.button3.bind("<Button-1>", self.button3Click)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text='down', background= 'red')
		self.button4.grid(row=2,column=1)
		self.button4.bind("<Button-1>", self.button4Click)	
		
						
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		# Create the code to bind an action to the second button
		# Do not change "<Button-1>"
		 
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		drawpad.move(oval,moveLeft,0)
		drawpad.move(oval2,moveLeft,0)
		drawpad.move(oval3,moveLeft,0)
		drawpad.move(oval4,moveLeft,0)
		drawpad.move(oval5,moveLeft,0)
		drawpad.move(oval6,moveLeft,0)
		drawpad.move(oval7,moveLeft,0)
		drawpad.move(oval8,moveLeft,0)
		
	def button2Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(oval,moveRight,0)
            drawpad.move(oval2,moveRight,0)
	    drawpad.move(oval3,moveRight,0)
	    drawpad.move(oval4,moveRight,0)
	    drawpad.move(oval5,moveRight,0)
	    drawpad.move(oval6,moveRight,0)
	    drawpad.move(oval7,moveRight,0)
	    drawpad.move(oval8,moveRight,0)
	def button3Click(self,event):
	    global oval
	    global drawpad
	    drawpad.move(oval,0,moveUp)
	    drawpad.move(oval2,0,moveUp)
	    drawpad.move(oval3,0,moveUp)
	    drawpad.move(oval4,0,moveUp)
	    drawpad.move(oval5,0,moveUp)
	    drawpad.move(oval6,0,moveUp)
	    drawpad.move(oval7,0,moveUp)
	    drawpad.move(oval8,0,moveUp)
	def button4Click(self,event):
	    global oval
	    global drawpad
	    drawpad.move(oval,0,moveDown)
	    drawpad.move(oval2,0,moveDown)
	    drawpad.move(oval3,0,moveDown)
	    drawpad.move(oval4,0,moveDown)
	    drawpad.move(oval5,0,moveDown)
	    drawpad.move(oval6,0,moveDown)
	    drawpad.move(oval7,0,moveDown)
	    drawpad.move(oval8,0,moveDown)
		
	# Add the event handler for the second button to make it move right!
	
		
myapp = MyApp(root)
root.mainloop()