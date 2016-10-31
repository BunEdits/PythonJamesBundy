import random #Imports random, allows for random selection in code
import time #Imports time
import datetime #Imports date


print("I am Version 002 Of Idubbbz ChatBot").upper()
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

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator

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
		
	HOWOLD() #Activates function

		
#Age section		
def HOWOLD():
	
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global AGEG #Makes age global for other functions
	print("Enter Only A Number") #Prints message
	AGEG = raw_input("How Old Are You?: ") #User input
	
	print("Good To Know You Are" + ' ' + AGEG + ' ' + "This Will Be useful To Me Later!") #Prints message with age variable
	
	TALKABOUT()




	
#Talk about section, acts like menu	
def TALKABOUT():

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator

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
	ANSWERTA = raw_input("What Would You Like To Talk About?: ").lower() #User input, sets it to lower case

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
	WISHAGE = raw_input("What Age Do You Wish You Was Again?: ")
	
	print("I Wish I Could Be" + ' ' + WISHAGE + ' ' + "Again! I Will Use This Later!")
	
	TALKABOUT()


def FAVOURITEtimeofday():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global WISHTIME
	global WISHDATE
	
	print("Input Time As Follows 24 Hour Clock: HH:MM:SS ")
	WISHTIME = raw_input("What Is Your Favourite Time Of Day?: ")
	
	print(" ")

	print("Input Date As Follows: DD/MM/YYYY ")
	WISHDATE = raw_input("What Is Your Favourite Date?: ")
	
	print(" ")
	
	print("Now I Know Your Favourite Time Of Day Is:" + ' ' + WISHTIME + ' ' + "This Will Be Useful To Me Later!")
	print("Now I Know Your Favourite Date Is:" + ' ' + WISHDATE + ' ' + "This Will Be Useful To Me Later!")

	print(" ")

	print("Here Is Everything I Know About the Time/Date: ")
	
	print(" ")
	
	print("                                         Day-Month-Year-Hour-Minute")
	print "This Is The Current date and time Right Now: ",datetime.datetime.now().strftime("%d-%m-%y-%H-%M")
	print "This Is The Current Year Right Now: ", datetime.date.today().strftime("%Y")
	print "This Is The Current Month Of Year: ", datetime.date.today().strftime("%B")
	print "This Is The Current Week Number Of The Year Out Of 52: ", datetime.date.today().strftime("%W")
	print "This Is The Current Weekday Of The Week: ", datetime.date.today().strftime("%w")
	print "This Is The Current Day Of The Year Out Of The 365 Days: ", datetime.date.today().strftime("%j")
	print "This Is The Current Day Of The Month : ", datetime.date.today().strftime("%d")
	print "This Is The Current Day Of The Week: ", datetime.date.today().strftime("%A")
	
	TALKABOUT()

	
def FAVOURITEcolour():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global USERCOLOUR #This is the users input colour
	
	print("""Say A Colour From The Rainbow:
	Red
	Orange
	Yellow
	Green
	Blue
	Purple
	Pink
	""")
	
	
	coloursAll = ['red','orange','yellow','green','blue','purple','pink']
	
	
	print(" ")
	
	print("Input Example 'Blue' In Caps If You Like! ")
	print("Or You May Put It In A Sentence Like 'I Like the Colour Blue' ")
	USERCOLOUR = raw_input("What Is Your Favourite Colour?: ").lower()
	
	print(" ")
	
	if any(x in USERCOLOUR for x in coloursAll):
		print(USERCOLOUR + ' ' + "This Will Be Useful To Me Later!")
	else:
		print("Did You Say A Colour?")
		FAVOURITEcolour()
		
	TALKABOUT()


def FAVOURITEfood():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	
	global USERFOOD
	
	print("""Say Your Favourite Food From The List:
	Unhealthy
	Healthy
	Chocolatte
	McDonald's
	Chips
	Scones
	Crisps
	Fruit
	Pancake
	""")
	
	USERFOOD = raw_input("What Is Your Favou")
	
	print(USERFOOD)
	
	TALKABOUT()


def Finished():
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
	print("Finished")
	


	
	
GREETINGS() #Activates function





#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
#HOWOLD() #Activates function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
#TALKABOUT() #Activates function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator

#RESTART() #Activates Function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
#ENDBOT() #Activates Function
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Prints the separator
