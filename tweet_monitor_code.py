from twarc import Twarc
import json
import fileinput
import sys

print (" # Loading keys")
consumer_key = 'INSERT YOUR CONSUMER KEY HERE'
consumer_secret = 'INSERT YOUR CONSUMER SECRET HERE'
access_token = 	'INSERT YOUR TOKEN HERE' 
access_token_secret = 'INSERT YOUR TOKEN SECRET HERE'
twarc_auth = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

print (" # Reading search terms")
with open('tweet_terms.txt','r') as tweet_terms_file_content:
	my_tweet_terms = [line.strip() for line in tweet_terms_file_content]
	print (" # Search terms loaded")
	
	if len(my_tweet_terms) > 0:
		twitter_query = ",".join(my_tweet_terms)
		print " # Search terms: " + twitter_query
	
		for tweet in twarc_auth.filter(track = twitter_query):
			with open('data_dump.json', 'a') as json_output_file:
				json.dump(tweet, json_output_file, indent=4, sort_keys=True)
	else:
		print "No search terms provided, printing generic stream"
		for tweet in twarc.sample():
			print(tweet)
print (" # Authentication successful, dumping results")
tweet_terms_file_content.close()
json_output_file.close()