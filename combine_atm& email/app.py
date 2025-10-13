# app.py

# Import the email sending module
import Single_email_send

# operations
operations=(
    "1. Balance\n",
    "2. Withdraw\n"
    "3. Deposite\n"
    "4. Transfer\n"
    "5. History\n"
    "6. Logout"
)

# accounts_table
accounts ={
    12345:"6789",
    12346:'6788'
    }

#user_details table
user_details = {
    12345: ["codegnan",1000,"22jr5a4411@gmail.com"],
    12346: ['Destination',2000,'22jr5a4411@gmail.com'] # Corrected email for testing
}

#login function
def login(user_name:int, password:str):
    print("I am in login page")
    # checking user_name presenrt in account table or not
    if user_name in accounts:
        if accounts[user_name]== password:
            print("Successfully logedin to Codegnan Online Netbanking")
            return True
        else:
            print("check your user credencialts")
    else:
        print("User not found")
        return False
    


#operatuions functions creation
#balance function creation
def balance(user_name:int):
    
    #check user present in user table
    if user_name in user_details:
        amount = user_details[user_name][1]
        print(f"Current balance is {amount}")
    #user is not in users table
    else:
        print("user not found")
    

# withdraw function creation
def withdraw(user_name:int,Withdraw_amount:int):
   
    #check user present in user table
    if user_name in user_details:
        amount=user_details[user_name][1]
        if Withdraw_amount<= amount:
            user_details[user_name][1]-=Withdraw_amount
            print(f"Successfully withdraw your amount {Withdraw_amount}")
            current_balance = user_details[user_name][1]
            print(f"Current Balance is {current_balance}")
            
            # --- Send Email Notification ---
            try:
                to_email = user_details[user_name][2]
                subject = "Transaction Alert: Amount Withdrawn"
                body = f"Hello {user_details[user_name][0]},\n\nAn amount of {Withdraw_amount} has been withdrawn from your account.\nYour new balance is {current_balance}.\n\nThank you."
                Single_email_send.singleEmailsender(to_email=to_email, subject=subject, body=body)
            except Exception as e:
                print(f"Failed to send email notification. Error: {e}")
        else:
            print("Insufficent amount in your acount")
    #user is not in users table
    else:
        print("user not found")

    

#deposite function defination
def deposite(user_name:int,deposite_amount:int):
   
    #check user present in user table
    if user_name in user_details:
       user_details[user_name][1]+= deposite_amount
       current_balance = user_details[user_name][1]
       print(f"Current balance is {current_balance}")

       # --- Send Email Notification ---
       try:
           to_email = user_details[user_name][2]
           subject = "Transaction Alert: Amount Deposited"
           body = f"Hello {user_details[user_name][0]},\n\nAn amount of {deposite_amount} has been deposited into your account.\nYour new balance is {current_balance}.\n\nThank you."
           Single_email_send.singleEmailsender(to_email=to_email, subject=subject, body=body)
       except Exception as e:
           print(f"Failed to send email notification. Error: {e}")
    #user is not in users table
    else:
        print("user not found")

#Transfer function defination
def transfer(user_name:int,to_account:int,transfer_amount:int):
     if user_name in user_details:
        if to_account in user_details:
            amount=user_details[user_name][1]
            if transfer_amount<= amount:
                # Perform the transfer
                user_details[user_name][1]-=transfer_amount
                user_details[to_account][1]+=transfer_amount
                
                sender_balance = user_details[user_name][1]
                receiver_balance = user_details[to_account][1]

                print(f"Transfer successful. Your new balance is {sender_balance}")
                
                # --- Send Email to Sender ---
                try:
                    sender_email = user_details[user_name][2]
                    subject_sender = "Transaction Alert: Amount Transferred"
                    body_sender = f"Hello {user_details[user_name][0]},\n\nYou have successfully transferred {transfer_amount} to account {to_account}.\nYour new balance is {sender_balance}.\n\nThank you."
                    Single_email_send.singleEmailsender(to_email=sender_email, subject=subject_sender, body=body_sender)
                except Exception as e:
                    print(f"Failed to send sender email notification. Error: {e}")

                # --- Send Email to Receiver ---
                try:
                    receiver_email = user_details[to_account][2]
                    subject_receiver = "Transaction Alert: Amount Received"
                    body_receiver = f"Hello {user_details[to_account][0]},\n\nYou have received {transfer_amount} from account {user_name}.\nYour new balance is {receiver_balance}.\n\nThank you."
                    Single_email_send.singleEmailsender(to_email=receiver_email, subject=subject_receiver, body=body_receiver)
                except Exception as e:
                    print(f"Failed to send receiver email notification. Error: {e}")
            else:
                print(f"Insufficent Amount in {user_name}")
        else:
            print(f"{to_account} User not found")
     else:
        print(f"{user_name} user not found")
    

# mini statement function
def history(user_name:int):
    print("Development under processing.....")
    pass

#logout function defination
def logout():
    print("User Successfully logedout")
    exit()
    

#main function
if __name__ == "__main__":
    print("Welcome to codegnan online netbanking app")
    account =int(input("Please enter your account number: "))
    password = input("please enter your password: ")
    if login(user_name=account,password=password):
        while True:
             print(*operations)
             choice=int(input("please select your operation: "))

             if choice ==1:
                balance(user_name=account)

             elif choice==2:
                amount=int(input("Please enter your withdraw amount: "))
                withdraw(user_name=account,Withdraw_amount=amount)

             elif choice==3:
                amount=int(input("Please enter your deposite amount: "))
                deposite(user_name=account,deposite_amount=amount)

             elif choice==4:
                reciver_account=int(input("Please enter your recivier account number: "))
                amount=int(input("Please enter your transfer amount: "))
                transfer(user_name=account,to_account=reciver_account,transfer_amount=amount)

             elif choice==5:
                history(user_name=account)

             elif choice==6:
                logout()
                
             else:
                print("Please enter between 1-6")