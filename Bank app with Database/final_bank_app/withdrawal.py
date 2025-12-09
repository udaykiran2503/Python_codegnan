
import db_utils

def withdraw(acc,amt):
    user=db_utils.get_user(acc)
    if not user: 
        return "User not found"
    name,email,bal,acc=user
    if amt>bal: 
        return "Insufficient funds"
    new=bal-amt
    db_utils.update_balance(acc,new)
    db_utils.log_transaction(acc,"WITHDRAW",amt)
    db_utils.singleEmailsender(email,"Withdrawal Successful",f"{amt} withdrawn. New balance {new}.")
    return f"Balance: {new}"
