from accounts_data import user_details
import Single_email_send

def history(user_name: int):
    if user_name in user_details:
        try:
            to_email = user_details[user_name][2]
            subject = "History Check Notification"
            body = f"Hello {user_details[user_name][0]},\n\nYou checked your transaction history (feature under development).\n\nThank you."
            Single_email_send.singleEmailsender(to_email, subject, body)
        except Exception as e:
            return f"History check requested. Email failed: {e}"
        return "Mini statement feature under development... Email notification sent."
    return "User not found"
