# Stafford Motor Speedway Racing Results Twitter Bot
This script posts tweets to twitter in order to share the most recent racing results from Stafford Motor Spedway's SK Modified Feature Events. The tweet includes the date of the race, the race title, the top 5 finishers and the link to the full article on the tracks website.

---

##### [Stafford Motor Speedway Website](https://staffordmotorspeedway.com/) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [Twitter @TheKingTC13](https://twitter.com/TheKingTC13)
![StaffordandTwitter](images/staffordandtwitter.jpeg)

---

## Environment Variables
See the docs: [python-dotenv](https://github.com/theskumar/python-dotenv).

Change the below variables in '.env'. Using environment variables to secure api keys.

#### Twitter API Variables 
API calls using [Tweepy](https://www.tweepy.org/).

To create and use the twitter API apply for a [Twitter Developer Account](https://developer.twitter.com/).

- API_KEY = "YOUR_KEY_HERE"
- API_SECRET = "YOUR_KEY_HERE"
- API_ACCESS_TOKEN = "YOUR_KEY_HERE"
- API_ACCESS_SECRET = "YOUR_KEY_HERE"

#### Twitter Account Variable
- TWITTER_ACCOUNT = "YOUR_@TWITTER_HERE"

#### Webhook Variable
- WEBHOOK_URL = "WEBHOOK_URL" - The webhook URL if you want to send messages using webhooks.

#### Other Variable
- ARCHIVE_URL = "ARTICLE_URL" - The URL that contains a list of posts.

## Functions in Script
- [tweepyThread](https://github.com/JacobMannix/TweepyThread) - Function using [tweepy](https://www.tweepy.org/) in order to send multiple tweets in a thread fashion.
- discordMessage - Function using [requests](https://requests.readthedocs.io/en/master/) to send messages over webhooks, this one is used mainly for discord.
- [staffordResults](https://github.com/JacobMannix/StaffordResults) - The main part of this script

---

### License
Licensed under the [MIT License](LICENSE).