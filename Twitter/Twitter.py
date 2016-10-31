import twitter #Imports Twitter API
import time #Enables for time.sleep
import datetime


while True:
	#Below reads my last tweet
	user = 2422855266 #My user ID
	file = open("C:\Users\james\Desktop\~Desktop~\James Plymouth Uni\~Tasks~\~Second Year~\DAT 505\PythonJamesBundy\Twitter\TwitterCredentials.txt")
	creds = file.read().split('\n')
	api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
	statuses = api.GetUserTimeline(user)

	print(statuses[0].text)
	time.sleep(3600) #Makes script sleep for 1 hour.
	#time.sleep(2) #DEBUG Check if time.sleep works. 2 seconds

	

file = open("C:\Users\james\Desktop\~Desktop~\James Plymouth Uni\~Tasks~\~Second Year~\DAT 505\PythonJamesBundy\Twitter\TwitterCredentials.txt")
creds = file.read().split('\n')
api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Tweeted at " + str(timestamp))
print("Status updated to: " + response.text)
