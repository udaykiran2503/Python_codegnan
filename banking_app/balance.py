from accounts_data import user_details
import Single_email_send

def balance(user_name: int):
    if user_name in user_details:
        amount = user_details[user_name][1]
        try:
            to_email = user_details[user_name][2]
            subject = "Balance Check Notification"
            body = f"Hello {user_details[user_name][0]},\n\nYour current balance is {amount}.\n\nThank you."
            Single_email_send.singleEmailsender(to_email, subject, body)
        except Exception as e:
            return f"Balance check successful: {amount}. Email failed: {e}"
        return f"Current balance is {amount}"
    return "User not found"
