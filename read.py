import imaplib

from config import IMAP_URL, IMAP_USERNAME, IMAP_PASSWORD
from process_email import process_email, extract_email, print_extracted_email

username = IMAP_USERNAME
password = IMAP_PASSWORD
imap_server = IMAP_URL

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL(imap_server)
# authenticate
imap.login(username, password)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 13
# total number of emails
messages = int(messages[0])

# Note: Still buggy if we have no message :o
for i in range(messages, max(messages-N, 0), -1):
	# fetch the email message by ID
	res, msg = imap.fetch(str(i), "(RFC822)")
	# process_email(msg)
	list = extract_email(msg)
	print_extracted_email(list)

# close the connection and logout
imap.close()
imap.logout()