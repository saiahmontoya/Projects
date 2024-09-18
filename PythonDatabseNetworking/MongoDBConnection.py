from pymongo import MongoClient, database
import subprocess
import threading
import pymongo
from datetime import datetime, timedelta,timezone
import time
import certifi

DBName = "test" #Use this to change which Database we're accessing
connectionURL = "mongodb+srv://saiahmontoya01:WB6ldzVvr1ZQutb1@assignment7.rgy1djn.mongodb.net/" #Put your database URL here
sensorTable = "Traffic Data" #Change this to the name of your sensor data table

def QueryToList(query):
	# Iterate through the query and put it in a list.
	queryList = []
	for doc in query:
		queryList.append(doc)
	return queryList

def QueryDatabase() -> list[dict]:
	global DBName
	global connectionURL
	global currentDBName
	global running
	global filterTime
	global sensorTable
	cluster = None
	client = None
	db = None
	try:
		cluster = connectionURL
		client = MongoClient(connectionURL, tlsCAFile=certifi.where())
		db = client[DBName]
		print("Database collections: ", db.list_collection_names())

		#We first ask the user which collection they'd like to draw from.
		sensorTableObject = db[sensorTable]
		print("Table:", sensorTableObject)

		#We convert the cursor that mongo gives us to a list for easier iteration.
		# Convert the time now in the current location to UTC, then subtract 5 minutes to get all the documents generated 
		# in the past 5 minutes.
		timeCutOff = datetime.now(timezone.utc) - timedelta(minutes=5) #TODO: Set how many minutes you allow
		
		# Swapped the names of the variables for less confusion. Old documents are before the time cutoff. Current
		# documents are after the time cutoff.
		oldDocuments = QueryToList(sensorTableObject.find({"time":{"$lte":timeCutOff}}))
		currentDocuments = QueryToList(sensorTableObject.find({"time":{"$gte":timeCutOff}}))
		#TODO: Parse the documents that you get back for the sensor data that you need
		return currentDocuments
		


	except Exception as e:
		print("Please make sure that this machine's IP has access to MongoDB.")
		print("Error:",e)
		exit(0)
