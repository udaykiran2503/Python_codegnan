from accounts_data import accounts, user_details
import Single_email_send

def login(user_name: int, password: str) -> str:
    if user_name in accounts and accounts[user_name] == password:
        try:
            to_email = user_details[user_name][2]
            subject = "Login Notification"
            body = f"Hello {user_details[user_name][0]},\n\nYou have successfully logged in.\n\nThank you."
            Single_email_send.singleEmailsender(to_email, subject, body)
        except Exception as e:
            return f"Login successful, but email failed: {e}"
        return "Login successful"
    return "Login failed! Invalid credentials."
