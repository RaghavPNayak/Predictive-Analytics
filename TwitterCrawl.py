from twython import Twython
import json
import time
import sys
import codecs
import unicodedata
import senti_definer as s

APP_KEY = "AgVX36jZGpmo1CA2bAjzYNcNN"
APP_SECRET = "ieOLnHT9pCGVO3CF7XhrwnZjKkm2MDbfC79DZrITmmIVs29zxZ"

twitter = Twython(APP_KEY, APP_SECRET)

data1 = twitter.search(q='Batman v Superman'or'Dawn of Justice'or'Batman Superman',lang='en', count='100',max_id='711752885625884672')

i=0
j=0
tweet_En=data1['statuses']
data1En=[]

for i in tweet_En:
    tweetE=i
    if "http" not in tweetE['text']:
        TweetEn={}
        TweetEn['time_zone'] = tweetE['user']['time_zone']
        TweetEn['screen_name'] = tweetE['user']['screen_name']
        TweetEn['created_at'] = tweetE['created_at']
        TweetEn['lang'] = tweetE['lang']
        TweetEn['text'] = tweetE['text']
        TweetEn['id'] = tweetE['id']
        sentiment_value, confidence = s.sentiment(tweetE['text'])
        TweetEn['sentiment'] = sentiment_value
        TweetEn['confidence'] = confidence

#For checking performance metrics
        if "pos" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSPosTweets.txt","a")
            output.write(str(tweetE['text']))
            output.write('\n')
            output.close()
        if "neg" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSNegTweets.csv","a")
            output.write(str(tweetE['text']))
            output.write('\n')
            output.close()


#Data for generating charts
        if "pos" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSGraphPos.csv","a")
            output.write(str(tweetE['created_at']))
            output.write(',')
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        if "neg" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSGraphNeg.csv","a")
            output.write(str(tweetE['created_at']))
            output.write(',')
            output.write(sentiment_value)
            output.write('\n')
            output.close()

#Data for generating maps
        if "pos" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSMapsPos.csv","a")
            output.write(str(TweetEn['time_zone']))
            output.write(',')
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        if "neg" in TweetEn['sentiment']:
            output = open("Crawled_Dataset/BatmanVSuperman/BVSMapsNegative.csv","a")
            output.write(str(TweetEn['time_zone']))
            output.write(',')
            output.write(sentiment_value)
            output.write('\n')
            output.close()

#Data for entering into textBoxes
        if "RT" not in tweetE['text']:
            if "pos" in TweetEn['sentiment']:
                output = open("Crawled_Dataset/BatmanVSuperman/BVSTxtBoxPos.txt","a")
                output.write("Screen Name: ")
                output.write(TweetEn['screen_name'])
                output.write('\n')
                output.write("Created At: ")
                output.write(str(tweetE['created_at']))
                output.write('\n')
                output.write("Tweet: ")
                output.write(str(tweetE['text']))
                output.write('\n')
                output.write('\n')
                output.close()
            if "neg" in TweetEn['sentiment']:
                output = open("Crawled_Dataset/BatmanVSuperman/BVSTxtBoxNeg.txt","a")
                output.write("Screen Name: ")
                output.write(TweetEn['screen_name'])
                output.write('\n')
                output.write("Created At: ")
                output.write(str(tweetE['created_at']))
                output.write('\n')
                output.write("Tweet: ")
                output.write(str(tweetE['text']))
                output.write('\n')
                output.write('\n')
                output.close()
                
        if "Batman v Superman: Dawn of Justice" or "Batman Superman" or "Dawn of Justice" in tweetE['text']:
            TweetEn['movies'] = "Batman v Superman : Dawn of Justice";
        
   
        URL_EnList= []
        hashtag_EnList = []
        for j in tweetE['entities']['urls']:
            URL_EnList.append(j['expanded_url'])
        for j in tweetE['entities']['hashtags']:
            hashtag_EnList.append(j['text'])
        TweetEn['tweet_urls'] = URL_EnList
        TweetEn['tweet_hashtags'] = hashtag_EnList
        if "Batman v Superman: Dawn of Justice" or "Batman Superman" or "Dawn of Justice" in TweetEn['tweet_hashtags']:
            TweetEn['movies'] = "Batman v Superman : Dawn of Justice";
        
        TweetEn['created_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.strptime(TweetEn['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        data1En.append(TweetEn)


fen= codecs.open('Crawled_Dataset/BatmanVSuperman/BVSProcessed','a', encoding="ISO-8859-1")
json.dump(data1En,fen)
fen.close()


zen= codecs.open('Crawled_Dataset/BatmanVSuperman/BVSRaw','a', encoding="ISO-8859-1")
json.dump(data1,zen)
zen.close()

'''End of Tweet Collection'''
