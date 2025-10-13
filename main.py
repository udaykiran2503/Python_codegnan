# main.py

import addition
import substraction
import multiplication
import division
import modulusDivision
import math



def calculator():
    print("Calculator started...")  
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. square_root")
        print("6. Modulus")
        print("7. Exit")


        choice = input("Enter your choice (1-6): ")

        if choice == "7":
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", addition.add(a, b))
            elif choice == "2":
                print("Result:", substraction.subtract(a, b))
            elif choice == "3":
                print("Result:", multiplication.multiply(a, b))
            elif choice == "4":
                print("Result:", division.divide(a, b))
            elif choice=="5":
                n=int(input("Enter your number:"))
                print("Result:",math.sqrt(n**0.5))
            elif choice == "6":
                # modulus only works properly with integers
                print("Result:", modulusDivision.modulus(int(a), int(b)))
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    calculator()
