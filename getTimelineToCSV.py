#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import csv
import sys

CK = ''  # Consumer Key
CS = ''  # Consumer Secret
AT = ''  # Access Token
AS = ''  # Accesss Token Secert

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# とくにパラメータは不要
params = {}

# OAuth で GET
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.get(url, params=params)

if req.status_code == 200:
    # レスポンスはJSON形式なので parse する
    timeline = json.loads(req.text)
    # 各ツイートのデータを取得
    for tweet in timeline:
        f = open("timeline.csv","ab")
        tweet_id = tweet[u'id_str']
        text = tweet[u'text'].encode("utf-8")
        created_at = tweet[u'created_at'].encode("utf-8")
        user_id = tweet[u'user'][u'id_str'].encode("utf-8")
        f.write(tweet_id)
        f.write(",")
        f.write(user_id)
        f.write(",")
        f.write(text)
        f.write(",")
        f.write(created_at)
        f.write(",")
        f.write("\n")
        f.flush()
        f.close()
    
    else:
        # エラーの場合
        print("Error: %d" % req.status_code)
        
