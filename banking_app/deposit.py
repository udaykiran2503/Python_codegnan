from accounts_data import user_details
import Single_email_send

def deposit(user_name: int, deposit_amount: int):
    if user_name not in user_details:
        return "User not found"

    user_details[user_name][1] += deposit_amount
    current_balance = user_details[user_name][1]

    try:
        to_email = user_details[user_name][2]
        subject = "Transaction Alert: Amount Deposited"
        body = (f"Hello {user_details[user_name][0]},\n\n"
                f"An amount of {deposit_amount} has been deposited.\n"
                f"New balance: {current_balance}.\n\nThank you.")
        Single_email_send.singleEmailsender(to_email, subject, body)
    except Exception as e:
        return f"Deposit successful: {deposit_amount}. Current Balance: {current_balance}. Email failed: {e}"

    return f"Deposit successful: {deposit_amount}. Current Balance: {current_balance}"
