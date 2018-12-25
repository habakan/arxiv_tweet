import os
from dotenv import load_dotenv


# load env file
load_dotenv('.env')
CK = os.environ.get("CONSUMER_KEY")
CS = os.environ.get("CONSUMER_SECRET")
AT = os.environ.get("ACCESS_TOKEN")
ATS = os.environ.get("ACCESS_TOKEN_SECRET")
slack_webhook = os.environ.get("SLACK_WEBHOOK_URL")
