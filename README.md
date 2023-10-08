This is a python routine reading emails from an IMAP account.

1. Rename the file config.example.py to config.py and update the values to your connection parameters.

2. Then run the script:

		`python3 read-google.py`
		
	or for a generic email (WIP, only connecting)
		
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