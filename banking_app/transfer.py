from accounts_data import user_details
import Single_email_send

def transfer(user_name: int, to_account: int, transfer_amount: int):
    if user_name not in user_details:
        return "Sender not found"
    if to_account not in user_details:
        return "Receiver not found"

    if transfer_amount > user_details[user_name][1]:
        return "Insufficient funds"

    user_details[user_name][1] -= transfer_amount
    user_details[to_account][1] += transfer_amount
    sender_balance = user_details[user_name][1]
    receiver_balance = user_details[to_account][1]

    try:
        sender_email = user_details[user_name][2]
        subject = "Transaction Alert: Amount Transferred"
        body = (f"Hello {user_details[user_name][0]},\n\n"
                f"You transferred {transfer_amount} to account {to_account}.\n"
                f"New balance: {sender_balance}.\n\nThank you.")
        Single_email_send.singleEmailsender(sender_email, subject, body)
    except Exception as e:
        return f"Transfer done but sender email failed: {e}"

    try:
        receiver_email = user_details[to_account][2]
        subject = "Transaction Alert: Amount Received"
        body = (f"Hello {user_details[to_account][0]},\n\n"
                f"You received {transfer_amount} from account {user_name}.\n"
                f"New balance: {receiver_balance}.\n\nThank you.")
        Single_email_send.singleEmailsender(receiver_email, subject, body)
    except Exception as e:
        return f"Transfer done but receiver email failed: {e}"

    return f"Transfer successful. Sender Balance: {sender_balance}, Receiver Balance: {receiver_balance}"
