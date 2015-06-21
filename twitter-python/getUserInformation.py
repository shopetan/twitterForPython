#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
api = twitter.Api(consumer_key        ='',
                  consumer_secret     ='',
                  access_token_key    ='',
                  access_token_secret ='')

# user infomation
user = api.GetUser('[user_id]')
print user.screen_name
print user.name
print user.location
print user.description
print user.protected
print user.utc_offset
print user.time_zone

