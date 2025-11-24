from google_auth_oauthlib.flow import InstalledAppFlow

import json

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

with open('credentials.json', 'r') as f:
    client_credentials = json.load(f)

flow = InstalledAppFlow.from_client_config(client_credentials, SCOPES)

credentials = flow.run_local_server(access_type='offline', open_browser=False)

print("Access token:", credentials.token)
print("Refresh token:", credentials.refresh_token)
print("Token expiry:", credentials.expiry)




