import imaplib
import email
from email.header import decode_header
import webbrowser
import os

from config import IMAP_URL, IMAP_USERNAME, IMAP_PASSWORD

username = IMAP_USERNAME
password = IMAP_PASSWORD
imap_server = IMAP_URL

# clean text for creating a folder
def clean(text):
	return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL(imap_server)
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 3
# total number of emails
messages = int(messages[0])

print(messages)