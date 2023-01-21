#Use the tweepy library to connect to the Twitter API and collect tweets on a specific topic
#Use the textblob library to perform sentiment analysis on the tweets
#Use the matplotlib library to plot the sentiment analysis results

# import os
# from dotenv import load_dotenv
# load_dotenv()

import tweepy
from tweepy import Cursor
from textblob import TextBlob
import matplotlib.pyplot as plt

#Step 1 - Authenticate
# consumer_key = os.getenv("API_Key")
consumer_key = "dNfO4F2zl7GfCQQRSyey29rBz"
# consumer_secret = os.getenv("API_Key_Secret")
consumer_secret = "vb5yRnBCM3JVw5lj5KMz4Ogy5ddUKHgAf96KVokcLzI8GAP04P"

# access_token
# access_token_secret

auth = tweepy.OAuth2AppHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)


#Step 2 - Retrieve Tweets
api = tweepy.API(auth)
# public_tweets = api.search('Tate')
public_tweets = []
for tweet in Cursor(api.search_tweets, q='Tate').items(40):
    print(tweet)
    public_tweets.append(tweet)

#Step 3 - Perform Sentiment Analysis on Tweets
polarity = 0
positive = 0
negative = 0
neutral = 0
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

#Step 4 - Visualize the results
labels = ['Positive ['+str(positive)+']','Neutral ['+str(neutral)+']','Negative ['+str(negative)+']']
sizes = [positive,neutral,negative]
colors = ['yellowgreen','gold','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on Tate by analyzing '+str(positive+neutral+negative)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()

#Step 5 - Print the results
print("How people are reacting on Tate by analyzing "+str(positive+neutral+negative)+" Tweets. ")
if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print("Positive")

#Step 6 - Save the results
f = open("results.txt", "w")
f.write("How people are reacting on Tate by analyzing "+str(positive+neutral+negative)+" Tweets. ")
if (polarity == 0):
    f.write("Neutral")
elif (polarity < 0):
    f.write("Negative")
elif (polarity > 0):
    f.write("Positive")
f.close()

#Step 7 - Save the plot
plt.savefig('plot.png')
