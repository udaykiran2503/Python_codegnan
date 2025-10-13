from accounts_data import user_details
import Single_email_send

def withdraw(user_name: int, withdraw_amount: int):
    if user_name not in user_details:
        return "User not found"

    amount = user_details[user_name][1]
    if withdraw_amount > amount:
        return "Insufficient funds"

    user_details[user_name][1] -= withdraw_amount
    current_balance = user_details[user_name][1]

    try:
        to_email = user_details[user_name][2]
        subject = "Transaction Alert: Amount Withdrawn"
        body = (f"Hello {user_details[user_name][0]},\n\n"
                f"An amount of {withdraw_amount} has been withdrawn.\n"
                f"New balance: {current_balance}.\n\nThank you.")
        Single_email_send.singleEmailsender(to_email, subject, body)
    except Exception as e:
        return f"Withdraw successful: {withdraw_amount}. Current Balance: {current_balance}. Email failed: {e}"

    return f"Withdraw successful: {withdraw_amount}. Current Balance: {current_balance}"
