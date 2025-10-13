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
    12345: ["codegnan",1000,"codegnan@codegnan.com"],
    12346: ['Destination',2000,'Destination@codegnan']

}

#login function
def login(user_name:int, password:str):
    print("I am in login page")
    # checking user_name presenrt in account table or not
    if user_name in accounts:
        if accounts[user_name]== password:
            print("Successfu;lly logedin to Codegnan Online Netbanking")
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
            print(f"Current Balance is {user_details[user_name][1]}")
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
       print(f"Current balance is {user_details[user_name][1]}")
    #user is not in users table
    else:
        print("user not found")
#Transfer function defination
def transfer(user_name:int,to_account:int,transfer_amount:int):
     if user_name in user_details:
        if to_account in user_details:
            amount=user_details[user_name][1]
            if transfer_amount<= amount:
                user_details[user_name][1]-=transfer_amount
                user_details[to_account][1]+=transfer_amount
                
                print(f"Current Balance is {user_details[user_name][1]}")
            else:
                print(f"Insufficent Amount in {user_name}")
        else:
            print(f"{to_account}User not found")
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
            
        