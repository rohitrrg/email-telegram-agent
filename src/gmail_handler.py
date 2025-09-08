import os, base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            raise Exception("⚠️ Run Gmail API quickstart to generate token.json")
    return build('gmail', 'v1', credentials=creds)

def check_new_email(service, last_id=None):
    results = service.users().messages().list(
    userId='me',
    labelIds=['INBOX'],
    q="is:unread category:primary"
).execute()
    messages = results.get('messages', [])
    if not messages:
        return None

    msg_id = messages[0]['id']
    if msg_id == last_id:
        return None

    msg = service.users().messages().get(userId='me', id=msg_id, format="full").execute()
    headers = msg["payload"]["headers"]

    subject = next((h["value"] for h in headers if h["name"] == "Subject"), "")
    sender = next((h["value"] for h in headers if h["name"] == "From"), "")
    message_id = next((h["value"] for h in headers if h["name"] == "Message-ID"), "")

    body = ""
    if "parts" in msg["payload"]:
        body = base64.urlsafe_b64decode(msg["payload"]["parts"][0]["body"]["data"]).decode("utf-8")
    elif "body" in msg["payload"] and "data" in msg["payload"]["body"]:
        body = base64.urlsafe_b64decode(msg["payload"]["body"]["data"]).decode("utf-8")

    return {
        "id": msg_id,
        "threadId": msg["threadId"],
        "from": sender,
        "subject": subject,
        "message_id": message_id,
        "body": body
    }

def send_email_reply(service, to, subject, text, thread_id=None, message_id=None):
    from email.mime.text import MIMEText

    message = MIMEText(text)
    message['to'] = to
    message['subject'] = "Re: " + subject

    if message_id:
        message['In-Reply-To'] = message_id
        message['References'] = message_id

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw}
    if thread_id:
        body['threadId'] = thread_id

    service.users().messages().send(userId="me", body=body).execute()
