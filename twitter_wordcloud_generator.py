import tweepy
from os import path
from collections import Counter
from PIL import Image, ImageOps
from wordcloud import WordCloud

#Twitter initializer
	#(You need to of course replace the 'Twitter provided key' with your account's keys)
	#(In order to get them you first need to aply as a developer in https://developer.twitter.com)
CONSUMER_KEY = 'Twitter provided key'
CONSUMER_SECRET = 'Twitter provided'
ACCESS_KEY = 'Twitter provided'
ACCESS_SECRET = 'Twitter provided'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

#the rest of the script handles the wordcloud creation, saving the result as a .png file and tweeting it.

#placeholder for appending the user's mentions in his/hers timeline: 
mentions = []

#promt to get the Twitter account we want to get the wordcloud from:
user = print(input("Please enter the user's name (without the @): "))

#The whole process is as follows:
	#1. Looping over the user's Tweeter feed (timeline)
	#2. Getting every mention from the user's timeline
	#3. Skipping the mention's from the user's to himself/herself.
	#4. Appending every other mention into the mentions variable.

#1. fetching 50 pages of 200 tweets each from the user:
for i in range(50):
	for tweet in (api.user_timeline(id=user, count=200, page=i)):
		#2. separating each word from each tweet and checking if the word is a mention:
		splitted_tweets = tweet.text.split()
		for word in splitted_tweets:
			if word.startswith('@'):
				#3. for each mention we need to skip the user's mention to himself (like in Twitter threads).
				if word == (f'@{user}'):
					pass
				#4. appending every other mention to the mentions variable.
				else:
					mentions.append(word)
		
#we counter each ocurrence for each mention on the mentions variable.
#This helps getting a more accurate word cloud
mentions_count = Counter(mentions)

#setting a WordCloud initializer with the parameters we want for the specific cloud:
wc = WordCloud(width=800,
							height=600,
							colormap='summer', #any matplotlib colormap is availible for use directly in Wordcloud
							max_words=300,
							background_color='black',
							max_font_size=92,
							random_state=56)

# generate the word cloud
wc.generate_from_frequencies(mentions_count)

#converting the wordcloud into an Image object
#This is only needed for postproduction of the image (like the autocontrast filter aplied bellow)
image = wc.to_image()
autocontrast = ImageOps.autocontrast(image)

#saving the image
image.save(f'{user}.png')

#Tweeting the wordcloud:
media = api.media_upload(autocontrast)
api.update_status(text=((f"Hey, @{user}! Look what i've just did for you!"), media_ids=[media.media_id])

#That's all. I hope you liked it.
