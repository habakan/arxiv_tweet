import json 
from env import *
import datetime as dt
from requests_oauthlib import OAuth1Session 


with open('params.json', 'r') as f:
    params = json.load(f)

def search_tweet(params):
    twitter = OAuth1Session(CK, CS, AT, ATS) 
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    res = twitter.get(url, params = params)
    if res.status_code == 200:
        timelines = json.loads(res.text)
        latest_id = timelines['statuses'][0]['id']
        text = '本日のarxiv関連Tweets\n'
        for line in timelines['statuses']: 
            text += line['created_at'] + '\n'
            text += line['text'] + '\n'

            if len(line['entities']['urls']) > 0:
                text += line['entities']['urls'][0]['expanded_url'] + '\n'

            tweet_url = "https://twitter.com/" + line['user']['screen_name'] + '/status/' + str(line['id'])
            text += tweet_url + '\n'
            text += '-------------------------------------------\n'

    params['since_id'] = latest_id

    with open('params.json', 'w') as f:
        json.dump(params, f)

    return text
