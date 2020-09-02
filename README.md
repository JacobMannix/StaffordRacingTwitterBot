# Stafford Motor Speedway Racing Results Twitter Bot
This script posts tweets to twitter in order to share the most recent racing results from Stafford Motor Spedway's SK Modified Feature Events. The tweet includes the date of the race, the race title, the top 5 finishers and the link to the full article on the tracks website.

##### [Stafford Motor Speedway Website](https://staffordmotorspeedway.com/)                        [Twitter @TheKingTC13](https://twitter.com/TheKingTC13)
![StaffordandTwitter](staffordandtwitter.jpeg)


---

### Variables for functions to change
- archiveURL = "ARTICLEURL" - The URL that contains a list of posts.
- webhook_url = "WEBHOOKURL" - The webhook URL if you want to send messages using webhooks.
- twitterUser = 'TWITTERUSERNAME' - The twitter username of the account that is tweeting, used for creating twreads of tweets.

### [TWEEPY](https://www.tweepy.org/) Twitter API Variables to change
To create and use the twitter API apply for a [Twitter Developer Account](https://developer.twitter.com/).
- ckey = "APIKEY" - Consumer Key
- csecret = "APISECRETKEY" - Consumer Secret
- atoken = "APIACCESSTOKEN" - Access Token
- asecret = "APIACCESSTOKENSECRET" - Access Token Secret

### Functions in Script
- tweepyThread - Function using [tweepy](https://www.tweepy.org/) in order to send multiple tweets in a thread fashion.
- discordMessage - Function using [requests](https://requests.readthedocs.io/en/master/) to send messages over webhooks, this one is used mainly for discord.
- staffordResults - The main part of this script



Retrieves Race results posted on Stafford (staffordmotorspeedway.com) website and tweets them out on Twitter (@TheKingTC13)
