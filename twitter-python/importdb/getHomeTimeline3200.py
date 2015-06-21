#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import csv
import re

api = twitter.Api(consumer_key        ='',
                  consumer_secret     ='',
                  access_token_key    ='',
                  access_token_secret ='')

max_tweet = 3200
count = 200
accessAPI = max_tweet / count
max_id = None

f = open("timeline.csv","ab")
for i in range(accessAPI):
    home = api.GetHomeTimeline(count=count,max_id=max_id,exclude_replies = True)
    if not home:
        break
    for tweet in home:
        post = re.sub(r'\,',' ', tweet.text)
        post = re.sub(r'\n',' ', post)
        f.write(post.encode("utf-8"))
        f.write(",")
        f.write(tweet.user.name.encode("utf-8"))
        f.write("\n")
        max_id = tweet.id -1
