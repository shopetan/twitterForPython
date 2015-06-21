#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

api = twitter.Api(consumer_key        ='',
                  consumer_secret     ='',
                  access_token_key    ='',
                  access_token_secret ='')

users = api.GetHomeTimeline(count=200)
for tweet in users:
    print tweet.text
