# How to Use
To have these programs run as intended, they would ideally be run from a cloud computer 
such as AWS EC2/Google Cloud Console or a Raspberry Pi. This is so that the programs aren't ended early or have to restart.

# Twitter_Bot
This is a basic Twitter bot that tweets daily at a specified time and keeps a daily 
counter that increments every time the tweet is sent.<br/>

This utilizes Tweepy, schedule, time, and  datetime to handle everything.<br/>
The credentials used to allow Tweepy to interact with Twitter need to be accessed from your
developer.twitter.com account.

You can find them by logging into the site then going to:  
Team dropdown> Apps> Details> Keys and Tokens<br/>

Tweepy documentation can be found [here](http://docs.tweepy.org/en/latest/).  
Schedule documentation can be found [here](schedule.readthedocs.io).  

# RandomQuotes
This is another basic Twitter bot, but this one involves pulling random lines from a text file and 
using those as tweets. API credentials are also grabbed from a text file.<br/>

The credentials file, creds.txt, only needs the API credentials to be entered in place of the
placeholder variables to work with the python file.
