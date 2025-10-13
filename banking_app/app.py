from login import login
from balance import balance
from withdraw import withdraw
from deposit import deposit
from transfer import transfer
from history import history
from logout import logout

operations = (
    "1. Balance\n",
    "2. Withdraw\n",
    "3. Deposit\n",
    "4. Transfer\n",
    "5. History\n",
    "6. Logout"
)

if __name__ == "__main__":
    print("Welcome to Codegnan Online Netbanking App")
    account = int(input("Enter account number: "))
    password = input("Enter password: ")

    login_status = login(account, password)
    print(login_status)

    if "successful" in login_status:
        while True:
            print(*operations)
            choice = int(input("Select operation: "))

            if choice == 1:
                print(balance(account))
            elif choice == 2:
                amt = int(input("Enter withdraw amount: "))
                print(withdraw(account, amt))
            elif choice == 3:
                amt = int(input("Enter deposit amount: "))
                print(deposit(account, amt))
            elif choice == 4:
                receiver = int(input("Enter receiver account: "))
                amt = int(input("Enter transfer amount: "))
                print(transfer(account, receiver, amt))
            elif choice == 5:
                print(history(account))
            elif choice == 6:
                print(logout(account))
                break
            else:
                print("Invalid choice, select between 1-6")
    else:
        print("Exiting program.")
