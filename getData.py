# For each twitter handle which is provided, it creates two text files,
# one containing the tweets extracted, and another which simply contains the sentiment
# of the tweet, pos for positive, neg for negative and neutral for neutral

#TODO Include score of each sentiment in calculation
#TODO Find a way to remove tweets which are part of contests done by various brands 

import tweepy
import csv
import requests

def getData(name):
	#Enter your Twitter credentials
	consumer_key = 
	consumer_secret = 
	access_token = 
	access_token_secret = 

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	f = open(name+".txt","a")
	tweetOut = open(name+"Tweets.txt","a")
	count = 0
	for tweet in tweepy.Cursor(api.search,q="@"+name,lang="en").items(): #Using Tweepy API, streams tweet for the given query
		count = count + 1
		text = tweet.text.encode('utf-8')
		text = text.lower()

		if(len(text) > 5):
			tweetOut.write(text)
			tweetOut.write("\n")
			data = {"text":text}
			r = requests.post("http://text-processing.com/api/sentiment/",data) #For each tweet extracted, uses Text-Processing.com's API to get the sentiment
			json = r.json() #Sentiment returned in json value. Currently ignoring score of each sentiment
			print text, json['label']
			f.write(json['label'])
			f.write("\n")

def main():
	#Enter Twitter handle of the company, withouot the '@' sign
	#Example
	tweetHandle = "flipkart" 
	getData(tweetHandle)

main()