
import tweepy
from datamuse import datamuse
from random import randint
CONSUMER_KEY = "CVFmG4DSOvGc1gVHtBP5qbYzJ"
CONSUMER_SECRET = "t4ouGgBMNGbabfrSRe7k0rZUVdTIDGNYa7tqL4bEeoEYKitE2u"
ACCESS_TOKEN = "1091439390541271040-otarsi1XOiPZU5vw5L8yqkkNo0NX12"
ACCESS_TOKEN_SECRET = "nq41iqJPyrAHhqywycDn4HpYqLnSta2i412LsHBNjFSVk"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API (auth)
api2 = datamuse.Datamuse()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print (tweet.text)

def word(str) : 
    b = api2.words(rel_rhy=str, max =10)
    return(b)


print("Enter a word fam")
userWord = input("") 
anyword = word(userWord)


#dict1 = word[2]
#print(dict1)
#del dict1['score']
#del dict1['numSyllables']
#print(dict1)
#print(dict1.get('word'))

a = randint(0,9)

def randomIndexGen(a):
    muse = anyword[a]
    response = muse.get('word')
    return response
    

rTweet = randomIndexGen(a)
print(rTweet)
k = input()

