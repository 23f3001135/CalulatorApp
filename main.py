# main.py
import math
import sys
import os
import platform
from prettytable import PrettyTable


def clear(): # Helper function to clear the screen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pretty_print(data): # Helper function to pretty print data
    table = PrettyTable()
    table.field_names = ["Index", "Value"]
    for i, v in enumerate(data):
        table.add_row([i, v])
    print(table)


def history(data): # Helper function to print history
    pretty_print(data)
    print("\n")

# a pretty help function! ^^
def help():
    print("┌─────────────────────────────────────────────────────────┐")
    print("│                   Welcome to the calculator!           │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  Please select an option:                              │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│  1. Addition               2. Subtraction              │")
    print("│  3. Multiplication         4. Division                 │")
    print("│  5. Square                 6. Cube                     │")
    print("│  7. Square root            8. Cube root                │")
    print("│  9. Factorial              10. Exponential             │")
    print("│  11. Logarithm             12. Trigonometry            │")
    print("│  13. Inverse Trigonometry  14. Permutation             │")
    print("│  15. Combination           16. GCD                     │")
    print("│  17. LCM                   18. Pretty Print            │")
    print("│  19. History               20. Exit                    │")
    print("│  21. Help                                             │")
    print("└─────────────────────────────────────────────────────────┘")

# main function

def main():
    history_data = []
    while True:
        help()
        choice = input("Enter your choice: ")
        if choice == "1":
            clear()
            print("Addition")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = a + b
            print(f"The result of {a} + {b} is {result}")
            history_data.append(f"{a} + {b} = {result}")
        elif choice == "2":
            clear()
            print("Subtraction")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = a - b
            print(f"The result of {a} - {b} is {result}")
            history_data.append(f"{a} - {b} = {result}")
        elif choice == "3":
            clear()
            print("Multiplication")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = a * b
            print(f"The result of {a} * {b} is {result}")
            history_data.append(f"{a} * {b} = {result}")
        elif choice == "4":
            clear()
            print("Division")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = a / b
            print(f"The result of {a} / {b} is {
                result}")
            history_data.append(f"{a} / {b} = {result}")
        elif choice == "5":
            clear()
            print("Square")
            a = float(input("Enter the number: "))
            result = a ** 2
            print(f"The result of {a} ^ 2 is {result}")
            history_data.append(f"{a} ^ 2 = {result}")
        elif choice == "6":
            clear()
            print("Cube")
            a = float(input("Enter the number: "))
            result = a ** 3
            print(f"The result of {a} ^ 3 is {result}")
            history_data.append(f"{a} ^ 3 = {result}")
        elif choice == "7":
            clear()
            print("Square root")
            a = float(input("Enter the number: "))
            result = math.sqrt(a)
            print(f"The result of sqrt({a}) is {result}")
            history_data.append(f"sqrt({a}) = {result}")
        elif choice == "8":
            clear()
            print("Cube root")
            a = float(input("Enter the number: "))
            result = a ** (1 / 3)
            print(f"The result of {a} ^ (1/3) is {result}")
            history_data.append(f"{a} ^ (1/3) = {result}")
        elif choice == "9":
            clear()
            print("Factorial")
            a = int(input("Enter the number: "))
            result = math.factorial(a)
            print(f"The result of {a}! is {result}")
            history_data.append(f"{a}! = {result}")
        elif choice == "10":
            clear()
            print("Exponential")
            a = float(input("Enter the number: "))
            result = math.exp(a)
            print(f"The result of e^{a} is {result}")
            history_data.append(f"e^{a} = {result}")
        elif choice == "11":
            clear()
            print("Logarithm")
            a = float(input("Enter the number: "))
            b = float(input("Enter the base: "))
            result = math.log(a, b)
            print(f"The result of log_{b}({a}) is {result}")
            history_data.append(f"log_{b}({a}) = {result}")
        elif choice == "12":
            clear()
            print("Trigonometry")
            print("1. sin")
            print("2. cos")
            print("3. tan")
            choice = input("Enter your choice: ")
            if choice == "1":
                a = float(input("Enter the angle in degrees: "))
                result = math.sin(math.radians(a))
                print(f"The result of sin({a}) is {result}")
                history_data.append(f"sin({a}) = {result}")
            elif choice == "2":
                a = float(input("Enter the angle in degrees: "))
                result = math.cos(math.radians(a))
                print(f"The result of cos({a}) is {result}")
                history_data.append(f"cos({a}) = {result}")
            elif choice == "3":
                a = float(input("Enter the angle in degrees: "))
                result = math.tan(math.radians(a))
                print(f"The result of tan({a}) is {result}")
                history_data.append(f"tan({a}) = {result}")
        elif choice == "13":
            clear()
            print("Inverse Trigonometry")
            print("1. asin")
            print("2. acos")
            print("3. atan")
            choice = input("Enter your choice: ")
            if choice == "1":
                a = float(input("Enter the value: "))
                result = math.degrees(math.asin(a))
                print(f"The result of asin({a}) is {result}")
                history_data.append(f"asin({a}) = {result}")
            elif choice == "2":
                a = float(input("Enter the value: "))
                result = math.degrees(math.acos(a))
                print(f"The result of acos({a}) is {result}")
                history_data.append(f"acos({a}) = {result}")
            elif choice == "3":
                a = float(input("Enter the value: "))
                result = math.degrees(math.atan(a))
                print(f"The result of atan({a}) is {result}")
                history_data.append(f"atan({a}) = {result}")
        elif choice == "14":
            clear()
            print("Permutation")
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = math.perm(n, r)
            print(f"The result of P({n}, {r}) is {result}")
            history_data.append(f"P({n}, {r}) = {result}")
        elif choice == "15":
            clear()
            print("Combination")
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = math.comb(n, r)
            print(f"The result of C({n}, {r}) is {result}")
            history_data.append(f"C({n}, {r}) = {result}")
        elif choice == "16":
            clear()
            print("GCD")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = math.gcd(a, b)
            print(f"The result of gcd({a}, {b}) is {result}")
            history_data.append(f"gcd({a}, {b}) = {result}")
        elif choice == "17":
            clear()
            print("LCM")
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = math.lcm(a, b)
            print(f"The result of lcm({a}, {b}) is {result}")
            history_data.append(f"lcm({a}, {b}) = {result}")
        elif choice == "18":
            clear()
            print("Pretty Print")
            pretty_print(history_data)
        elif choice == "19":
            clear()
            print("History")
            history(history_data)
        elif choice == "20":
            clear()
            print("Exit")
            print("Thank you for using the calculator.")
            print("Goodbye!")
            sys.exit()
        elif choice == "21":
            clear()
            print("Help")
            help()
        else:
            clear()
            print("Invalid choice. Please try again.")
            help()
            
if __name__ == "__main__":
    main()