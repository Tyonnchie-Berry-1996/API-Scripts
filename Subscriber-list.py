from googleapiclient.discovery import build
import json
from google.oauth2.credentials import Credentials


with open('credentials.json') as f:
    credentials_data = json.load(f)
    a = credentials_data['installed']

credentials = Credentials.from_authorized_user_info(info=a)

youtube = build('youtube', 'v3', credentials=credentials)

channel = ''

response = youtube.subscriptions().list(
    part='subscriberSnippet',
    mySubscribers=True,
    maxResults=250,
).execute()


if 'items' in response:
    for item in response['items']:
        snippet = item['subscriberSnippet']
        subscriber_title = snippet['title']
        subscriber_id = snippet['channelId']
        print(f"Subscriber Title: {subscriber_title}, Subscriber ID: {subscriber_id}")
else:
    print("No subscribers found.")


