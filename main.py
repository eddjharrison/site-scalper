import requests
import base64
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime
import os

SERVICE_ACCOUNT_FILE = url = os.environ.get("SERVICE_ACCOUNT_FILE")
WORKER_EMAIL_ADDRESS = os.environ.get("WORKER_EMAIL")

def scalpText(site, subject, sender, hit_str1, hit_str2, mail_text, neg_str, recipients):
    """ Takes a site for scalping, first string hit, second string hit, email text to send,
        negative string hit and list of recipient email addresses"""
    re = requests.get(site)
    site_text = re.text
    if hit_str1 in site_text:
        service_gmail = login()
        message(text=mail_text,subject=subject, sender=sender,
                recipients=recipients, service_gmail=service_gmail)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Hit 1 found: ", current_time)

    elif hit_str2 in site_text:
        service_gmail = login()
        message(text=mail_text,subject=subject, sender=sender,
                recipients=recipients, service_gmail=service_gmail)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Hit 2 found: ", current_time)

    elif neg_str in site_text:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("No hits yet: ", current_time)

def login():
    credentials = service_account.Credentials.from_service_account_file(
        filename=SERVICE_ACCOUNT_FILE,
        scopes=['https://mail.google.com/'],
        subject=WORKER_EMAIL_ADDRESS
        )

    service_gmail = build('gmail', 'v1', credentials=credentials)
    return service_gmail

def message(text, subject, sender, recipients, service_gmail):
    length = len(recipients)
    for i in range(length):
        receiver_mail = recipients[i]
        print('Sent notification to:', receiver_mail)
        message = MIMEText(text)
        message['To'] = str(receiver_mail)
        message['From'] = str(sender)
        message['Subject'] = str(subject)
        sendMessage(message, service_gmail)


def sendMessage(message, service_gmail):
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }

    send_message = (service_gmail.users().messages().send
                    (userId="me", body=create_message).execute())
    print(F'Message Id: {send_message["id"]}')

def run(check_interval, site, subject, sender, hit_str1, hit_str2, mail_text, neg_str, recipients):
    starttime = time.time()
    while True:
        try:
            print('Looking for appointments...')
            time.sleep(float(check_interval) - ((time.time() - starttime) % float(check_interval)))
            scalpText(site=site, subject=subject, sender=sender,
                      hit_str1=hit_str1, hit_str2=hit_str2,
                      mail_text=mail_text, neg_str=neg_str,
                      recipients=recipients)
        except Exception as e:
            print('Failed because', e)
            print('Restarting connection..')
            run()


