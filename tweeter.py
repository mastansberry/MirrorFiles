import tweepy
import json

with open('twitter_auth.json') as file:
    secrets = json.load(file)


auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)
