#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

api = twitter.Api(consumer_key        ='',
                  consumer_secret     ='',
                  access_token_key    ='',
                  access_token_secret ='')

#Get user timeline
statuses = api.GetUserTimeline(screen_name='[user_name]',count=200)
tweetlist = []
for tweet in statuses:
    print tweet.text
