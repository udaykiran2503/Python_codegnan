
import db_utils

def transfer(sender,receiver,amt):
    su=db_utils.get_user(sender)
    ru=db_utils.get_user(receiver)
    if not su: 
        return "Sender not found"
    if not ru: 
        return "Receiver not found"
    sname,semail,sbal,sacc=su
    rname,remail,rbal,racc=ru
    if amt>sbal:
        return "Insufficient funds"

    db_utils.update_balance(sender,sbal-amt)
    db_utils.update_balance(receiver,rbal+amt)

    db_utils.log_transaction(sender,"TRANSFER_SENT",amt)
    db_utils.log_transaction(receiver,"TRANSFER_RECEIVED",amt)

    db_utils.singleEmailsender(semail,"Transfer Sent",f"You sent {amt} to {receiver}. New balance {sbal-amt}.")
    db_utils.singleEmailsender(remail,"Transfer Received",f"You received {amt} from {sender}. New balance {rbal+amt}.")
    return "Transfer successful"
