#import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

import nltk

import string

#import numpy as np

import random

import os

os.chdir('C:\\Users\\avikmukherjee\\Desktop')

f=open('chatbot.txt','r',errors = 'ignore')

raw=f.read()

raw=raw.lower()# converts to lowercase

nltk.download('punkt') # first-time use only

nltk.download('wordnet') # first-time use only

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 

word_tokens = nltk.word_tokenize(raw)# converts to list of words

#print(sent_tokens)

#print(word_tokens)

lemmer = nltk.stem.WordNetLemmatizer()

#WordNet is a semantically-oriented dictionary of English included in NLTK.

def LemTokens(tokens):

    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):

    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hello!", "hi", "hi!", "greetings", "greetings!", "sup", "what's up?","hey","how are you?")

GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "hello! please shoot me MDM related questions!"]

def greeting(sentence):

 

    for word in sentence.split():

        if word.lower() in GREETING_INPUTS:

            return random.choice(GREETING_RESPONSES)



#user_response="What is a chatbot"

def response(user_response):

    robo_response=''

    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

    tfidf = TfidfVec.fit_transform(sent_tokens)

    #sdf = pd.SparseDataFrame(tfidf)

    vals = cosine_similarity(tfidf[-1], tfidf)

    idx=vals.argsort()[0][-2]

    flat = vals.flatten()

    flat.sort()

    req_tfidf = flat[-2]

    if(req_tfidf==0):

        robo_response=robo_response+"I am sorry! I don't understand you"

        return robo_response

    else:

        robo_response = robo_response+sent_tokens[idx]

        return robo_response

flag=True

print("ROBO: My name is Robo. I will answer your queries about MDM. If you want to exit, type Bye!")

while(flag==True):

    user_response = input()

    user_response=user_response.lower()

    if(user_response!='bye'):

        if(user_response=='thanks' or user_response=='thank you' ):

            flag=False

            print("ROBO: You are welcome..")

        else:

            if(greeting(user_response)!=None):

                print("ROBO: "+greeting(user_response))

            else:

                print("ROBO: ",end="")

                print(response(user_response))

                sent_tokens.remove(user_response)

    else:

        flag=False

        print("ROBO: Bye! take care..")