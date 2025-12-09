
import login, balance, withdrawal, deposit, transfer, history, db_utils

def main():
    acc=input("Enter account number: ")
    pwd=input("Enter password: ")
    if not login.login(acc,pwd):
        print("Invalid login"); 
    user=db_utils.get_user(acc)
    print(f"Welcome, {user[0]}! (DB)")

    while True:
        print("1 Balance\n2 Withdrawal\n3 Deposit\n4 Transfer\n5 Mini statement\n6 Logout")
        ch=int(input("Choice: "))
        if ch==1: 
            print(balance.balance(acc))
        elif ch==2: 
            print(withdrawal.withdraw(acc,int(input("Amount: "))))
        elif ch==3: 
            print(deposit.deposit(acc,int(input("Amount: "))))
        elif ch==4: 
            print(transfer.transfer(acc,input("To Acc: "),int(input("Amount: "))))
        elif ch==5: 
            print(history.mini_statement(acc))
        elif ch==6: 
            break
        else:
            print("Invalid choice")

if __name__=='__main__': 
    main()
