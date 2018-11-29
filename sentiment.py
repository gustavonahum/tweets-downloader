import re
import tweepy
import textblob


def clean_tweet(tweet): 
	''' 
	Utility function to clean tweet text by removing links, special characters 
	using simple regex statements. 
	'''
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])  \
				(\w+:\/\/\S+)", " ", tweet).split()) 

def tweet_polarity(tweet):
	analysis = textblob.TextBlob(clean_tweet(tweet))

	polarity = analysis.sentiment.polarity

	return polarity

def tweet_sentiment(polarity):
	if polarity > 0: return 'positive'
	if polarity == 0: return 'neutral'
	if polarity < 0: return 'negative'

if __name__ == "__main__":

	with open("input_sentiment.txt") as file:
		for tweet in file:
			polarity = tweet_polarity(tweet)
			sentiment = tweet_sentiment(polarity)
			print(str(sentiment) + '   \t' + str(round(polarity, 2)) + '\t' + str(tweet))