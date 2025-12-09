
import db_utils

def balance(acc):
    user=db_utils.get_user(acc)
    if not user: return "User not found"
    name,email,amt,acc=user
    db_utils.singleEmailsender(email,"Balance Check",f"Hello {name}, your balance is {amt}.")
    return f"Balance: {amt}"
