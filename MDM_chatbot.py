#This is a basic chatbot which can be used to interact with a file and answer simple queries
#Author: Avik Mukherjee
#------------------------------------------------------------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import string
import random
--import os
from tqdm import tqdm
import requests

url = "https://github.com/getavik/My-SourceFiles/Metric Definition List Text.txt"
response = requests.get(url, stream=True)

with open("10MB", "wb") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)
--os.chdir('C:\\Users\\avikmukherjee\\Desktop\\My FIs\\Finance Master')
f=open('Metric Definition List Text.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find(os.path.join('corpora', 'wordnet'))
except LookupError:
    nltk.download('punkt')
    nltk.download('wordnet')
    
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
GREETING_INPUTS = ("hello", "hello!", "hi", "hi!", "greetings", "greetings!", "sup","hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "how can I help you today?"]

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
print("SENSEI: My name is SENSEI. I will answer your queries about Finance Master MDM. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("SENSEI: You are welcome...")
        else:
            if(greeting(user_response)!=None):
                print("SENSEI: "+greeting(user_response))
            else:
                print("SENSEI: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("SENSEI: Bye! take care..")
