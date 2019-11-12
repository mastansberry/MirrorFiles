import tweepy
import json

with open('twitter_auth.json') as file:
    secrets = json.load(file)


auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)


#twitter.update_status(status='My first automated tweet!')


#trythis = twitter.home_timeline()
#print (trythis)
yep=twitter.user_timeline(screen_name='@cnn',count =10)
#print (yep.text)
for yeep in yep:
    tweet=yeep.text
    print (tweet,'\n')
