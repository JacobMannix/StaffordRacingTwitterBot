# Stafford Motor Speedway Racing Results Twitter Bot
[![GitHub](https://img.shields.io/github/license/jacobmannix/kubernetes-stafford?color=blue)](LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/jacobmannix/stafford-racing-twitter-bot)](https://github.com/JacobMannix/kubernetes-stafford)
[![GitHub last commit](https://img.shields.io/github/last-commit/jacobmannix/stafford-racing-twitter-bot)](https://github.com/JacobMannix/kubernetes-stafford/commits/master)

> <b> This script posts tweets to twitter in order to share the most recent racing results from Stafford Motor Speedway's SK Modified Feature Events. The tweet includes the date of the race, the race title, the top 5 finishers and the link to the full article on the tracks website. </b>

#
##### [Stafford Motor Speedway Website](https://staffordmotorspeedway.com/) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [Twitter @TheKingTC13](https://twitter.com/TheKingTC13)
![StaffordandTwitter](images/staffordandtwitter.jpeg)

## Environment Variables
- See the docs: [python-dotenv](https://github.com/theskumar/python-dotenv).
- Change the below variables in '.env'. Using environment variables to secure api keys.

#### Twitter API Variables 
- API calls using [Tweepy](https://www.tweepy.org/).
- To create and use the twitter API apply for a [Twitter Developer Account](https://developer.twitter.com/).
```yaml
API_ACCESS_SECRET: <API_ACCESS_SECRET_base64_encoded>
API_ACCESS_TOKEN: <API_ACCESS_TOKEN_base64_encoded>
API_KEY: <API_KEY_base64_encoded>
API_SECRET: <API_SECRET_base64_encoded>
```

#### Twitter Account Variable
The twitter account username used in the API.
```yaml
TWITTER_ACCOUNT: <TWITTER_ACCOUNT_base64_encoded>
```
#### Webhook Variable
The webhook URL if you want to send messages using webhooks.
```yaml
WEBHOOK_DISCORD: <WEBHOOK_DISCORD_base64_encoded>
```
#### Other Variable
The URL that contains a list of posts.
```yaml
ARCHIVE_WEBSITE: <ARCHIVE_WEBSITE_base64_encoded>
```
## Functions in Script
- [tweepyThread](https://github.com/JacobMannix/TweepyThread) - Function using [tweepy](https://www.tweepy.org/) in order to send multiple tweets in a thread fashion.
- discordMessage - Function using [requests](https://requests.readthedocs.io/en/master/) to send messages over webhooks, this one is used mainly for discord.
- [staffordResults](https://github.com/JacobMannix/StaffordResults) - The main part of this script
