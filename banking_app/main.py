import Single_email_send
import bulk_email_send






if __name__ == "__main__":
    
    subject = input("Enter subject: ")
    body = input("Enter body:: " )
    choice = int(input("Select your operation \n 1.Single email send\n 2.Bulk email send"))
    if choice ==1:
        email = input("Please enter recevier email address: ")
        Single_email_send.singleEmailsender(
            to_email=email,
            subject= subject,
            body=body
)
    elif choice==2:
        emails = input("Enter enails seperated by comma ").split(",")
        bulk_email_send.bulkEmailSend(
            emails=emails,
            subject=subject,
            body=body
        )

