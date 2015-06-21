#!/user/bin/env python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import csv
import json
import sys, codecs



search_words = raw_input(u"Keyword?:")

C_KEY = '[c_key]'
C_SECRET ='[c_secret]'
A_KEY = '[a_key]'
A_SECRET = '[a_secret]'



def Search_words():
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": unicode(search_words, "utf-8"),
        "lang": "ja",
        "result_type": "recent",
        "count": "100"
    }
    tw = OAuth1Session(C_KEY,C_SECRET,A_KEY,A_SECRET)
    req = tw.get(url, params = params)
    tweets = json.loads(req.text)
    
    f = open("tweetsearch.csv" , "ab")
    writer = csv.writer(f)
    writer.writerow(["datetime", "id", "name", "text"])
    for tweet in tweets["statuses"]:
        time = (tweet["created_at"])
        id = (tweet["user"]["screen_name"].encode("utf-8"))
        name = (tweet["user"]["name"].encode("utf-8"))
        text = (tweet["text"].encode("utf-8"))
        
        writer.writerow([time, id, name, text])
        
        f.close()
        
        return Search_words
    
Search_words()
    
