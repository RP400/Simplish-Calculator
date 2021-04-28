# Tmport
from time import sleep

# The Calculator() is if i need to import this code into another
def Calculator():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    print("Loading SimplishCalculator.py....")
    sleep(1)
    name = input("Whats your name?: ")
    sleep(0.5)
    print("Hi "+ name +", and welcome to Simplish Calculator. (This is a modified version of programiz.com calculator)")
    sleep(3)
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            sleep(0.2)
            num2 = float(input("Enter second number: "))
            if choice == '1':
                sleep(0.2)
                print(num1, "+", num2, "=", add(num1, num2))
                ag = input("Want to go again? (y/n): ")
                if ag in ("y" , "n"):
                    if ag == "y":
                        print("Going Again...")
                        sleep(0.2)
                    elif ag == "n":
                        print("Goodbye!")
                        sleep(0.2)
                        exit()
                else:
                    print("Oops, that wasnt an answer. If you did do y or n try put it in lower case letters")
                    sleep(0.2)
            elif choice == '2':
                sleep(0.2)
                print(num1, "-", num2, "=", subtract(num1, num2))
                ag = input("Want to go again? (y/n): ")
                if ag in ("y" , "n"):
                    if ag == "y":
                        print("Going Again...")
                        sleep(0.2)
                    elif ag == "n":
                        print("Goodbye!")
                        sleep(0.2)
                        exit()
                else:
                    print("Oops, that wasnt an answer. If you did do y or n try put it in lower case letters")
                    sleep(0.2)
            elif choice == '3':
                sleep(0.2)
                print(num1, "*", num2, "=", multiply(num1, num2))
                ag = input("Want to go again? (y/n): ")
                if ag in ("y" , "n"):
                    if ag == "y":
                        print("Going Again...")
                        sleep(0.2)
                    elif ag == "n":
                        print("Goodbye!")
                        exit()
                else:
                    print("Oops, that wasnt an answer. If you did do y or n try put it in lower case letters")
                    sleep(0.2)
            elif choice == '4':
                sleep(0.2)
                print(num1, "/", num2, "=", divide(num1, num2))
                ag = input("Want to go again? (y/n): ")
                if ag in ("y" , "n"):
                    if ag == "y":
                        print("Going Again...")
                        sleep(0.2)
                    elif ag == "n":
                        print("Goodbye")
                        sleep(0.2)
                        exit()
                else:
                    print("Oops, that wasnt an answer. If you did do y or n try put it in lower case letters")
                    sleep(0.2)
        else:
            sleep(0.2)
            print("Invalid Input!")
# I will remove this if i need to use it as an import
Calculator()