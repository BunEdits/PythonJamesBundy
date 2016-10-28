import random #Imports random, allows for random selection in code
import time #Imports time
import datetime #Imports date


print("I am Version 001 Of Idubbbz ChatBot").upper()
print("Created By James Bundy")


#Restart Section
def RESTART():
	print("You Have Restarted") #Prints message
	GREETINGS() #Runs function

	
#Talk about something else section
def SOMETHINGELSE():
	print("You Have Chosen To Talk About Something Else") #Prints message
	TALKABOUT() #Runs function


#Kills the bot jumps to deadend	
def ENDBOT():
	print("Bye Bye, Run Me Again Soon! ") #Prints message
	print("Or I Have Died to Poor Code! ") #Prints message

	
#Greetings section
def GREETINGS():

	greetingPeople = ['hey','hello','hi','yo'] #My list of greetings
	anGreeting = raw_input("Say Hey, Hello, Hi or Yo!: ").lower() #User input, sets it to lower case so can be found in list
	
	if anGreeting in greetingPeople: #Searches list if statement
		#print("DEBUG Found It") #DEBUG
		print(random.choice(greetingPeople)).upper()
		print(":D")

	else:
		#print("DEBUG Not Found") #Not found a greeting, DEBUG
		print("Wrong! Greet Me!")
		GREETINGS()

		
#Age section		
def HOWOLD():
	
	global AGEG #Makes age global for other functions
	print("Enter Only A Number") #Prints message
	AGEG = raw_input("How Old Are You?: ") #User input
	
	print("Good to know you are" + ' ' + AGEG + ' ' + "this will be usful to me later!") #Prints message with age variable

	
#Talk about section, acts like menu	
def TALKABOUT():

#Prints message for user to know what to input.
	print("I Want To Learn About You Complete All Below")
	print("""To Talk About Choose From:
	Favourite age!
	Favourite time of day!
	Favourite colour!
	Favourite food!
	
	Finished!
	
	""")
	
#Global variable	
	global ANSWERTA
	

#Prints message for user to know what to input.	
	print("Once You Have Told Me All Your Favourites Say 'Finished' ")
	print("Say 'Favourite Age', Or Any From The List. ")
	ANSWERTA = raw_input("What would you like to talk about?: ").lower() #User input, sets it to lower case

#Global variables	
	global FAge
	global FTimeOfDay
	global FColour
	global FFood
	global FFinished
	
	FAge = ['favourite age', 'FAVOURITE AGE', 'favourite age!'] #List for age, includes caps version
	FTimeOfDay = ['favourite time of day', 'FAVOURITE TIME OF DAY', 'favourite time of day!'] #List for Time/Date, inlucdes caps version
	FColour = ['favourite colour', 'FAVOURITE COLOUR', 'favourite colour!'] #List for colour, includes caps version
	FFood = ['favourite food', 'FAVOURITE FOOD', 'favourite food!'] #List for food, includes caps version
	FFinished = ['finished', 'FINISHED', 'finished!'] #List for finished, includes caps version
	

#Else if statements to choose direction of script	
	if ANSWERTA in FAge:
		#print("DEBUG AGE")
		FAVOURITEage()
	elif ANSWERTA in FTimeOfDay:
		#print("DEBUG TIME")
		FAVOURITEtimeofday()
	elif ANSWERTA in FColour:
		#print("DEBUG COLOUR")
		FAVOURITEcolour()
	elif ANSWERTA in FFood:
		#print("DEBUG FOOD")
		FAVOURITEfood()
	elif ANSWERTA in FFinished:
		#print("DEBUG FOOD")
		Finished()
	else:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
		print("Im Not That Smart! ")
		TALKABOUT()
	
	
	
	
	
	
	





	

def FAVOURITEage():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator

	global WISHAGE
	
	print("I Know You Are" + ' ' + AGEG)
	WISHAGE = raw_input("What age do you wish you was again?: ")
	
	print("I Wish I Could Be" + ' ' + WISHAGE + ' ' + "Again! This Will Be Usful To Me Later!")


def FAVOURITEtimeofday():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global WISHTIME
	global WISHDATE
	
	print("Input Time As Follows 24 Hour Clock: HH:MM:SS ")
	WISHTIME = raw_input("What is your favourite time of day?: ")
	
	print(" ")

	print("Input Date As Follows: DD/MM/YYYY ")
	WISHDATE = raw_input("What Is Your Favourite Date?: ")
	
	print(" ")
	
	print("Now I Know Your Favourite Time Of Day Is:" + ' ' + WISHTIME + ' ' + "This Will Be Usful To Me Later!")
	print("Now I Know Your Favourite Date Is:" + ' ' + WISHDATE + ' ' + "This Will Be Usful To Me Later!")


def FAVOURITEcolour():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global USERCOLOUR
	
	print("""Say A Colour From The Rainbow:
	Red
	Orange
	Yellow
	Green
	Blue
	Purple
	Pink
	""")
	
	print(" ")
	
	print("Input Example 'Blue' In Caps If You Like! ")
	USERCOLOUR = raw_input("What Is Your Favourite Colour?: ").lower()
	
	print(USERCOLOUR)


def FAVOURITEfood():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global USERFOOD
	
	USERFOOD = raw_input("DEBUG")
	
	print(USERFOOD)


def Finished():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	print("Finished")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


GREETINGS() #Activates function
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
HOWOLD() #Activates function
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
TALKABOUT() #Activates function
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator









#RESTART() #Activates Function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
#ENDBOT() #Activates Function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
