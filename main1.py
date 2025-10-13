# main.py

import addition
import substraction
import multiplication
import division
import modulusDivision
import squareroot
import power

def calculator():
    print("Calculator started...")  
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Power")
        print("7. Modulus")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "7"]:
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
            elif choice == "7":
                print("Result:", modulusDivision.modulus(int(a), int(b)))

        elif choice == "5":
            n = float(input("Enter number: "))
            try:
                print("Result:", squareroot.calculate_sqrt(n))
            except ValueError as e:
                print("Error:", e)

        elif choice == "6":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", power.calculate_power(base, exponent))

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    calculator()
