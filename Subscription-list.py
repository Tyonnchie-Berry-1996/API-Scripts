from __future__ import annotations
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path
import readline

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
credentials_file = Path("credentials.json")
def auth_helper():
    with open(credentials_file, 'r') as f:
        readline.parse_and_bind("set editing-mode emacs")
        readline.parse_and_bind('"\\e[D": backward-char')
        readline.parse_and_bind('"\\e[C": forward-char')

        client_credentials = json.load(f)

        client_id = input("\nPaste your client id: ").strip()
        client_credentials['installed']['client_id'] = client_id

        client_secret = input("\nPaste your client secret: ").strip()
        client_credentials['installed']['client_secret'] = client_secret

        project_id = input("\nPaste your project id: ").strip()
        client_credentials['installed']['project_id'] = project_id

        refresh_token = input("\nPaste your refresh token: ").strip()
        client_credentials['installed']['refresh_token'] = refresh_token

    with open(credentials_file, 'w') as e:
        json.dump(client_credentials, e, indent=4)

    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
    creds = flow.run_local_server(access_type='offline')

    return build("youtube", "v3", credentials=creds)

youtube = auth_helper()


response = youtube.subscriptions().list(
    part="snippet",
    mySubscribers=True,
    maxResults=50
).execute()


if "items" in response:
    for item in response["items"]:
        print(item)
else:
    print("No subscribers found.")

with open(credentials_file, 'r') as f:
    client_credentials = json.load(f)

    client_id = "EMPTY_PLACE_HOLDER"
    client_credentials['installed']['client_id'] = client_id

    client_secret = "EMPTY_PLACE_HOLDER"
    client_credentials['installed']['client_secret'] = client_secret

    project_id = "EMPTY_PLACE_HOLDER"
    client_credentials['installed']['project_id'] = project_id

    refresh_token = "EMPTY_PLACE_HOLDER"
    client_credentials['installed']['refresh_token'] = refresh_token

with open(credentials_file, 'w') as e:
    json.dump(client_credentials, e, indent=4)
