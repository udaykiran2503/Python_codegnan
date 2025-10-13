import smtplib
from email.mime import multipart
from email.mime.text import MIMEText
import os

#configuration

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL ="your email"
SENDER_PASSKEY="gqkl aswb xgfl txso"

# create single sender emaail function
def singleEmailsender(to_email:str,subject:str,body:str):
    msg=multipart()
    msg['To'] = to_email
    msg['Subject']= subject
    msg['From']=SENDER_EMAIL
    msg.attach(MIMEText(body,'plain'))


    #start server
    server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls
    server.login(SENDER_EMAIL,SENDER_PASSKEY)
    server.sendmail(SENDER_EMAIL,to_email,msg.as_string())
    server.quit()

    print(f"Successfully email sent to {to_email}")
