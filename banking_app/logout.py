from accounts_data import user_details
import Single_email_send

def logout(user_name: int):
    if user_name in user_details:
        try:
            to_email = user_details[user_name][2]
            subject = "Logout Notification"
            body = f"Hello {user_details[user_name][0]},\n\nYou have successfully logged out.\n\nThank you."
            Single_email_send.singleEmailsender(to_email, subject, body)
        except Exception as e:
            return f"Logout successful, but email failed: {e}"
        return "User successfully logged out"
    return "User not found"
