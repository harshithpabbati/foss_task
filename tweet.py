import tweepy
import tokens
consumer_key=tokens.consumer_key()
consumer_secret=tokens.consumer_secret()
access_key=tokens.access_key()
access_secret=tokens.access_secret()
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
search=input("what do you want tweet:")
api=tweepy.API(auth)
api.update_status(search)
