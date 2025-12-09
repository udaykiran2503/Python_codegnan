# Single_email_send.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

#configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
# IMPORTANT: Replace with your email and a 16-digit 'App Password' from your Google Account
SENDER_EMAIL ="Your email" 
SENDER_PASSKEY="Your passkey" # open gmail settings then turn on 2 step verification and then go to app passwords and create a password it will generate a passkey paste it here.

# create single sender emaail function
def singleEmailsender(to_email:str,subject:str,body:str):
    msg=MIMEMultipart() # Corrected class name from multipart to MIMEMultipart
    msg['To'] = to_email
    msg['Subject']= subject
    msg['From']=SENDER_EMAIL
    msg.attach(MIMEText(body,'plain'))


    #start server
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls() # Corrected method call from starttls to starttls()
    server.login(SENDER_EMAIL,SENDER_PASSKEY)
    server.sendmail(SENDER_EMAIL,to_email,msg.as_string())
    server.quit()
    print(f"Successfully sent email notification to {to_email}")
