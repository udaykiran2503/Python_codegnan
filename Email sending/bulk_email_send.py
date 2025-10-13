import Single_email_send


#bulk email sender function
def bulkEmailSend(emails:list,subject:str,body:str):
    for email in emails:
        try:
            Single_email_send.singleEmailsender(
                to_email=email,
                subject=subject,
                body=body
            )
        except:
            print("Email send field")