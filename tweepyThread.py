#!/usr/bin/python
# Jacob Mannix [08-31-2020]

# TweepyThread function to tweet multiple tweets in a thread

# Import Dependencies
import tweepy

# Function
def tweepyThread(user, list, ckey, csecret, atoken, asecret):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Create API object
    api = tweepy.API(auth)
    
    # Loops through list to reply to the previoud tweet to create a thread
    count = 0
    for i in list:
        statuses = api.user_timeline(user, count = 1) 
        count += 1
        if count > 1:
            for status in statuses:
                tweetid = status.id
            api.update_status(status = i, in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)
            # time.sleep(2) # optional sleep between each tweet
        else:
            api.update_status(status = i)
            # time.sleep(2) # optional sleep between each tweet
