#!/usr/bin/python
# Jacob Mannix [08-31-2020]

#Import dependencies
import requests
import bs4
import pandas as pd
import math
from datetime import datetime
import re
import tweepy
import time
import os

# Local Modules
from webhooks import webhookMessage
from tweepyThread import tweepyThread

# Load Environment Variables - uses .env file
from dotenv import load_dotenv
load_dotenv()

# Check to see if working directory is the same as 'postedResults.txt'
# To change the working directory on linux use the below code to the current path
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

# Environment Variables - change in '.env' file
ckey = os.getenv("API_KEY")
csecret = os.getenv("API_SECRET")
atoken = os.getenv("API_ACCESS_TOKEN")
asecret = os.getenv("API_ACCESS_SECRET")
twitterUser = os.getenv("TWITTER_ACCOUNT")
webhook_url = os.getenv("WEBHOOK_URL")
archiveURL = os.getenv("ARCHIVE_URL")

# Race Results function
def staffordResults(archiveURL):
    # Getting Page of all Race Results
    
    print(archiveURL)
    # print(archivePage)
    # archiveURL = archiveURL[0].get('src').strip("https://")
    # archiveURL="https://"+archiveURL
    if 'staffordmotorspeedway' not in archiveURL:
        archiveURL=archiveURL[:7]+'staffordmotorspeedway.com/'+archiveURL[7:]
    print(archiveURL)

    print("comic url",archiveURL)


    archivePage = requests.get(archiveURL)
    archiveSoup = bs4.BeautifulSoup(archivePage.text, "html.parser")
    resultsHTML = archiveSoup.find(itemprop="url")

    resultsURL = resultsHTML['href'] # Getting URL of most recent race result
    title = resultsHTML.string # Get title of article of most recent race

    # Use most recent race URL to see results of race
    resultsPage = requests.get(resultsURL)
    resultsSoup = bs4.BeautifulSoup(resultsPage.text, "html.parser")
    resultsData = resultsSoup.find(class_= "row-hover")

    # Appending Race Results to Lists
    A=[]
    B=[]
    C=[]
    for row in resultsData.findAll("tr"):
        cells = row.findAll('td')
        # drivers = row.findAll('th')
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
    
    # Append A,B,C Lists to new list with some formatting
    list_index = []
    list_results = []
    for i in range(0,len(A)):
        list_index.append(A[i] + " (" + B[i] + ") ") # Finish and Start positions formatted in index column
        list_results.append(C[i]) # Driver Name

    # Convert Lists into DataFrame
    df = pd.DataFrame(index = list_index)
    df['Driver']=list_results
    
    # Specific Formatting for Discord
    dfDiscord = repr(df)
    dfDiscord = dfDiscord.replace('Driver', '')
    
    # Creates list for sectioning off drivers to limit 6 drivers per message
    # sections = [[0,5], [5,10], [10, 15], [15,20], [20,25], [25, 30], [30, 35]] # showing 5 drivers per tweet
    sections = [[0,5]] # only showing top 5 drivers
    num_sections = int(len(df) / 5) + (len(df)  % 5 > 0) # Divides the number of drivers by 5 (5 per tweet) and rounds up
    list_dfString = []
    for i,j in sections[:int(num_sections)]:
        dfString = repr(df[i:j])

        # Formatting string to contain less characters
        dfString = dfString.replace('  ', '')
        dfString = dfString.replace(') ', ')')
        dfString = dfString.replace(')', ') ')
        dfString = dfString.replace('Driver', '')
        
        # Originally made this to tweet all results in a thread of tweets but after testing works best for me...
        # to tweet once with top 5 results along with link to rest of results
        # Uncomment remaining of if statement and pass in a list to tweet in a thread
        if len(dfString) > 0:
            if i == 0:
                list_dfString.append(title + "\n" + dfString + "\n" + " "  + "\n" + resultsHTML['href'])
            # elif i <= 5:
                # list_dfString.append(dfString)
            # else:
                # list_dfString.append(dfString + "\n" + resultsHTML['href'])
    
    # Open date of most recently posted race
    postedResults = []
    with open('postedResults.txt', 'r') as fh:
        for line in fh:
            postedResults.append(str(line))
            
    # Convert date in list to datetime and format it
    postedResults = datetime.strptime(postedResults[0], "%B %d, %Y").strftime("%B %d, %Y")
    
    # Using Regex to extract the race date from the 'resultsHTML' webpage
    date = re.search(r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})", resultsHTML.string)
    # raceDate = date.group(0)
    raceDate = datetime.strptime(date.group(0), "%B %d, %Y").strftime("%B %d, %Y") #[0]

    # Checks if raceDate
    if raceDate != postedResults:
        postedResults = raceDate
        print(list_dfString)

        # Send race results in tweet thread
        # tweepyThread(twitterUser, list_dfString, ckey, csecret, atoken, asecret) # Calling function from above to tweet, takes a list

        # Send race results to discord -- Optional if you want to send results through webhook
        message_content = title + "\n" + dfDiscord
        webhookMessage(webhook_url, message_content)

    else:
        print('no new race results')
        # webhookMessage(webhook_url, 'no new race results') 
    # Save date of most recent race results
    with open("postedResults.txt", "w") as output:
        output.write(str(postedResults))
    
# Calling Function
staffordResults(archiveURL)