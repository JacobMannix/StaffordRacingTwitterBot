#!/usr/bin/python

# Jacob Mannix [08-31-2020]

# Check to see if working directory is the same as 'postedResults.txt'
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Import dependencies
import requests
import bs4
# from bs4 import BeautifulSoup
import pandas as pd
import math
from datetime import datetime
import re
import tweepy

#Variables
archiveURL = "https://staffordmotorspeedway.com/category/results/sk-modified-results/"
webhook_url = "https://discordapp.com/api/webhooks/750039834910785727/1xEBzZPWb90v6Rff4IZ8DN0U_4WdIE3eOVJlKFUZg0-X8I407lkqoNt1dbhHHBZYjIgq"
twitterUser = 'thekingtc13'

# TweepyThread function to tweet multiple tweets in a thread
ckey = "GBStFVszP6roFQZ1v5qVPeFzI"
csecret = "exeVOmNZvItxHpkpH61hW8wqCJ2VvW7accQo9xZNtNEHKiBr9b"
atoken = "1300816049386946562-4CgIiZgfomBgBQ8SMCbK1OKqv56YqH"
asecret = "6C4kM545189HYZ4L2OO16S1wltf1CNdlAYhOP5p2QnABU"
def tweepyThread(user, list):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Create API object
    api = tweepy.API(auth)
    
    count = 0
    for i in list:
        statuses = api.user_timeline(user, count = 1) 
        count += 1
        if count > 1:
            for status in statuses:
                tweetid = status.id
            api.update_status(status = i, in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)
        else:
            api.update_status(status = i)

# Discord Function to send 'message_content' from above
def discordMessage(webhook_url, message_content):
    Message = {"content": message_content}
    requests.post(webhook_url, data=Message)

# Race Results function
def staffordResults(archiveURL):
    # Getting Page of all Race Results
    archivePage = requests.get(archiveURL)
    archiveSoup = bs4.BeautifulSoup(archivePage.text, "html.parser")
    resultsHTML = archiveSoup.find(itemprop="url")

    resultsURL = resultsHTML['href'] # Getting URL of most recent race result
    title = resultsHTML.string # Get title of article of most recent race

    # Use most recent race URL to see results of race
    resultsPage = requests.get(resultsURL)
    resultsSoup = bs4.BeautifulSoup(resultsPage.text, "html.parser")
    resultsData = resultsSoup.find(class_= "row-hover") #TODO change this variable name

    # Appending Race Results to Lists
    A=[]
    B=[]
    C=[]
    for row in resultsData.findAll("tr"):
        cells = row.findAll('td')
        drivers = row.findAll('th')
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
    dfDiscord = dfDiscord.replace('Driver', '');
    
    # Creates list for sectioning off drivers to limit 6 drivers per message
    sections = [[0,5], [5,10], [10, 15], [15,20], [20,25], [25, 30], [30, 35]]
    num_sections = math.ceil((len(df)/5))
    list_dfString = []
    for i,j in sections[:int(num_sections)]:
        dfString = repr(df[i:j])

        # Formatting string to contain less characters
        dfString = dfString.replace('  ', '');
        dfString = dfString.replace(') ', ')');
        dfString = dfString.replace(')', ') ');
        dfString = dfString.replace('Driver', '');
        if len(dfString) > 0:
            if i == 0:
                list_dfString.append(title + "\n" + dfString)
            else:
                list_dfString.append(dfString)
    
    # Add URL for race results to end of list
    list_dfString.append(resultsHTML['href'])

    # Open date of most recently posted race
    postedResults = []
    with open('postedResults.txt', 'r') as fh:
        for line in fh:
            postedResults.append(str(line))
            
    # Convert date in list to datetime and format it
    postedResults = datetime.strptime(postedResults[0], "%B %d, %Y").strftime("%B %d, %Y")
    
    # Using Regex to extract the race date from the 'resultsHTML' webpage
    date = re.search(r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})", resultsHTML.string)
    raceDate = date.group(0)#[0]
    
    # Checks if raceDate
    if raceDate != postedResults:
        postedResults = raceDate
        print(list_dfString)

        # Send race results in tweet thread
        tweepyThread(twitterUser, list_dfString)

        # Send race results to discord
        message_content = title + "\n" + dfDiscord
        discordMessage(webhook_url, message_content)

    else:
        # print('no race')
        # discordMessage(webhook_url, 'no race')
    # Save date of most recent race results
    with open("postedResults.txt", "w") as output:
        output.write(str(postedResults))
    
# Calling Function
staffordResults(archiveURL)
