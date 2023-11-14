This is a python routine reading emails from an IMAP account.

1. Rename the file config.example.py to config.py and update the values to your connection parameters.

2. Then run the script:

		`python3 read-google.py`
		
	or for a generic email
		
		`python3 read.py`



Code for reading in Google is courtesy of Geeks for Geeks:

	`https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/`
	
Code for reading generic email is courtesy of The Python Code:

`https://thepythoncode.com/article/reading-emails-in-python#:~:text=fetch()%20method%2C%20which%20fetches,()%20function%20from%20the%20email.`



**Note** The  generic email extractor needs test. Here are a few cases that should be covered:
- Simple part email and Multi-part email
- plain text email and HTML email
- email with attachments (image, pdf, etc.)
- Multipart with plain text messages and HTML version as a part (NOT and attachment)

### Some references for further developments...

#### How to get only new emails (since last connection)

- [How to Use Python’s imaplib to check for new emails(continuously)](https://medium.com/@juanrosario38/how-to-use-pythons-imaplib-to-check-for-new-emails-continuously-b0c6780d796d) by juanrosario on Medium (with a paywall :o )
- [Fetching all messages since last check with Python + Imap](https://blog.yadutaf.fr/2013/04/12/fetching-all-messages-since-last-check-with-python-imap/) by Jean-Tiare Le Bigot
- [IMAPlib how to select only emails since a given date](https://stackoverflow.com/questions/69507867/imaplib-how-to-select-only-emails-since-a-given-date) on StackOverflow

#### Getting across IMAP structure

- !!! [IMAP Tools library](https://github.com/ikvk/imap_tools) on GitHub.
- [Parsing email structure with IMAP functions](https://wpriders.com/snippets/parsing-email-structure-imap-functions/) by Ionut G on WPriders
- [How to download the complete html of emails with python using imap
](https://stackoverflow.com/questions/71535578/how-to-download-the-complete-html-of-emails-with-python-using-imap) on StackOverflow, with link to above IMAP Tools.

#### Download all emails in .eml format

- [Dump IMAP repository](https://gist.github.com/polo2ro/e142e164a327ee576321) on Github