from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail scopes — read, send, modify
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    creds = None

    # If token.json exists, load it
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid creds, go through auth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # 👇 Here we pass redirect_uri in InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(
                'config/gmail_credentials.json', SCOPES,
                redirect_uri='urn:ietf:wg:oauth:2.0:oob'
            )

            # Generate the auth URL
            auth_url, _ = flow.authorization_url(
                access_type='offline',
                include_granted_scopes='true',
                prompt='consent'
            )

            print("🔗 Please open this URL in your Windows browser:\n")
            print(auth_url)
            print("\nAfter logging in and allowing access, you’ll get a code.")

            code = input("📋 Paste the authorization code here: ")
            flow.fetch_token(code=code)
            creds = flow.credentials

        # Save credentials for later
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Confirm Gmail works
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    print("\n✅ Gmail API connected! Labels:")
    for label in labels:
        print(" -", label['name'])


if __name__ == '__main__':
    main()
