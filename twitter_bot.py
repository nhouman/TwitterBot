#Complete Tweepy documentation can be found at docs.tweepy.org
import tweepy, time, schedule
from datetime import datetime

#Authorization credentials
#API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
#are meant to be replaced by your keys and tokens found
#at developer.twitter.com. These are what allow your program
#to interact with Twitter and write tweets
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#count is to keep track of the days
count = 1

#Replace STATUS with whatever you want your tweet to be.
#A success message will print showing the time the tweet
#was sent and what the tweet said.
def tweet():
    global count
    status = "STATUS " + str(count)
    api.update_status(status)
    print("Tweeted at " + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    print ("Tweet: " +  status)
    count += 1

#Replace TIME with whatever time you  want the tweet to send at/
#TIME uses 24 hour clock (ex. 1:30PM = 13:30)
#Other scheduler methods can be found at schedule.readthedocs.io
#To prevent errors, similar tweets should not be sent to quickly
def main():
    user = api.me()
    print (user.name)

    schedule.every().day.at("TIME").do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()

