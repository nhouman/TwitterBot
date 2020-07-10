import schedule, time, random, tweepy
from datetime import datetime

f = open("quotes.txt", encoding = "utf8")
lines = list(f)
f.close()

f = open("creds.txt", encoding = "utf8")
creds = list(f)
f.close()

API_KEY = creds[0]
API_SECRET_KEY = creds[1]
ACCESS_TOKEN = creds[2]
ACCESS_TOKEN_SECRET = creds[3]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

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

def getQuote():
    quote = random.choice(lines)
    if len(quote) < 240:
        lines.remove(quote)
        return quote
        
schedule.every.monday.at("10:30").do(tweet)
while len(lines) > 0:
    schedule.run_pending()
    time.sleep(1)



