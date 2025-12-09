
import db_utils

def deposit(acc,amt):
    user=db_utils.get_user(acc)
    if not user: return "User not found"
    name,email,bal,acc=user
    new=bal+amt
    db_utils.update_balance(acc,new)
    db_utils.log_transaction(acc,"DEPOSIT",amt)
    db_utils.singleEmailsender(email,"Deposit Successful",f"{amt} deposited. New balance {new}.")
    return f"Balance: {new}"
