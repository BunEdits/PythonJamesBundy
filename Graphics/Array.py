from GraphicsEngine import * #Imports graphics engine
import random #Imports random allows for random.choice
import time #Imports sleep


#Click Mouse To Cycle Through The Stages.



Window = GraphWin("Viewing Window", 800,800) #Creates window
Window.setBackground(color_rgb(40,40,40)) #Sets colour of the window



#This is my array, numbers dont have ' ' only strings do
myArray = [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 
43, 72, 74, 59, 44, 57, 55, 49, 54, 54]

while True:

	Red = random.randint(1,255)
	Green = random.randint(1,255)
	Blue = random.randint(1,255)
	
	#print(Red,Green,Blue) #DEBUG rgb random

	randomNumberfirst = random.choice(myArray) #Sets var to number in array
	time.sleep(0.1)
	#print(random.choice(myArray)) #Prints random number from my array of numbers

	
	# Create and draw a rectangle, Acts as my BG
	BG = Rectangle(Point(0,0),Point(800,800)) #Top Left, Bottom Right
	BG.setFill(color_rgb(randomNumberfirst,randomNumberfirst,randomNumberfirst))
	BG.setOutline(color_rgb(40,40,40))
	BG.draw(Window)
	
	# Create and draw a rectangle, Acts as my BG
	BG = Rectangle(Point(10,10),Point(790,70)) #Top Left, Bottom Right
	BG.setFill(color_rgb(Blue,Red,Green))
	BG.setOutline(color_rgb(randomNumberfirst,randomNumberfirst,randomNumberfirst))
	BG.draw(Window)
	
	# Create and draw some text
	Randomtext = Text(Point(400,50),randomNumberfirst)
	Randomtext.draw(Window)
	
	
	#Creates circle
	Ball = Circle(Point(400,400), randomNumberfirst)
	Ball.setFill(color_rgb(Red,Green,Blue))
	Ball.setOutline(color_rgb(Red,Green,Blue))
	Ball.draw(Window)
	
	Window.getMouse()	#Waits until mouse click to finish script, Click to run while loop agains