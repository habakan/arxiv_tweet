import json
import requests
from search import search_tweet
from env import *


def post_slack(url, text):
    payload_dic = {
        "text":text,
    }
    return requests.post(url, data=json.dumps(payload_dic))

if __name__=='__main__':

    with open('params.json', 'r') as f:
        params = json.load(f)

    data = search_tweet(params)

    r = post_slack(slack_webhook, data)
