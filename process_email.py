import email
from email.header import decode_header
import webbrowser
import os

# clean text for creating a folder
def clean(text):    
    return "".join(c if c.isalnum() else "_" for c in text)
    # return os.path.join(folder_root, folder_name)
# Make a folder for this email (named after the subject)
# File path in based on mail subject, within the data folder
def create_file_path_for(subject, filename):
    folder_name = os.path.join("data", clean(subject))
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    return os.path.join(folder_name, filename)

def get_subject(msg):
    # decode the email subject
    subject, encoding = decode_header(msg["Subject"])[0]
    if encoding == None:
        encoding = 'utf-8'
    if isinstance(subject, bytes):
        # if it's a bytes, decode to str
        subject = subject.decode(encoding)
    return subject

def get_from(msg):
    # decode email sender
    From, encoding = decode_header(msg.get("From"))[0]
    if isinstance(From, bytes):
        From = From.decode(encoding)
    return From

def is_plain_text_body(part):
    content_type = part.get_content_type()
    content_disposition = str(part.get("Content-Disposition"))
    return content_type == "text/plain" and "attachment" not in content_disposition

def has_attachment(part):
    content_disposition = str(part.get("Content-Disposition"))
    "attachment" in content_disposition

# Download attachment in folder with subject name
def download_attachment(part, subject):
    filename = part.get_filename()
    if filename:
        filepath = create_file_path_for(subject, filename)        
        # download attachment and save it
        open(filepath, "wb").write(part.get_payload(decode=True))

# Download index.html in folder with subject name
# returns the name of the created file
def download_html(body, subject):
    # if it's HTML, create a new HTML file and open it in browser
    filepath = create_file_path_for(subject, "index.html")    
    # write the file
    open(filepath, "w").write(body)
    return filepath

# Get the body of a message or the body of part of a message
def get_email_body(msg_or_part):
    return msg_or_part.get_payload(decode=True).decode()

# returns an email dictionary
def extract_email(msg):
    msg_list = []
    for response in msg:
        if isinstance(response, tuple):
            single_message = {}
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            single_message['subject'] = get_subject(msg);
            single_message['from'] = get_from(msg);            
            
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    content_type = part.get_content_type()
                    try:                         
                        body = get_email_body(part)
                    except:
                        pass

                    single_message['has_attachment'] = has_attachment(part);     
                    if is_plain_text_body(part):
                        single_message['text_body'] = body;
                    elif has_attachment(part):                        
                        download_attachment(part, get_subject(msg))
            else:
                content_type = msg.get_content_type()
                body = get_email_body(msg)
                if content_type == "text/plain":
                    single_message['text_body'] = body;

            # This is a bit shaggy... It will read content type of last multipart message.
            if content_type == "text/html":
                single_message['html_body'] = body;
            
            msg_list.append(single_message);
    return msg_list

# Display an email dictionary
def print_extracted_email(msg_list):
    for msg in msg_list:

            print("Subject:", msg['subject'])
            print("From:", msg['from'])
            print("Has attachment:", msg['has_attachment'])
            print("Has body:", 'text_body' in msg.keys())
            if 'text_body' in msg.keys():
                print("Start:", msg['text_body'][0:55])
            print("Has HTML body:", 'html_body' in msg.keys())
            if 'text_body' in msg.keys():
                print("HTML Start:", msg['html_body'][0:25])

            print("="*100)
    return

def process_email(msg):
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            print("Subject:", get_subject(msg))
            print("From:", get_from(msg))

            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    content_type = part.get_content_type()
                    try:                         
                        body = get_email_body(part)                        
                    except:
                        pass
                    if is_plain_text_body(part):
                        print(body)
                    elif has_attachment(part):
                        download_attachment(part, get_subject(msg))
            else:
                content_type = msg.get_content_type()
                body = get_email_body(msg)
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)

            # This is a bit shaggy... It will read content type of last multipart message.
            if content_type == "text/html":
                filepath = download_html(body, get_subject(msg))
                # open in the default browser
                webbrowser.open(filepath)

            print("="*100)
    return