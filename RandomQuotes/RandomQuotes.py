import schedule, time, random, tweepy
from datetime import datetime

#Opens the quotes files and turns the lines
#into a list, then closes the file.
f = open("quotes.txt", encoding = "utf8")
lines = list(f)
f.close()

#Opens the credentials file and turns the
#lines into a list, then closes the file.
f = open("creds.txt", encoding = "utf8")
creds = list(f)
f.close()

#Sets the credentials from the creds list.
API_KEY = creds[0]
API_SECRET_KEY = creds[1]
ACCESS_TOKEN = creds[2]
ACCESS_TOKEN_SECRET = creds[3]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#Makes sure status is not None before tweeting.
#Successful tweet shows time and status of tweet.
#If failed to tweet, a different tweet is sent
#instead of throwing an error.
def tweet():
    status = getQuote()
    if not status == None:
        api.update_status(status)
        print("Tweeted at " + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print(status)
    else:
        api.update("Quote machine tired. Check back tomorrow.")
        print("Tweeted at " + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print("No quote today")

#Pulls a psuedorandom line from the list of
#lines and makes sure it is less than 240
#characters before returning it. Then removes
#the line from the list and returns the line.
def getQuote():
    quote = random.choice(lines)
    if len(quote) < 240:
        lines.remove(quote)
        return quote

#Uses schedule to call the tweet function every
#Monday at 10:30 PM. Makes sure that there are
#more than 0 lines in the list of lines before
#continuing.
schedule.every.monday.at("10:30").do(tweet)
while len(lines) > 0:
    schedule.run_pending()
    time.sleep(1)



