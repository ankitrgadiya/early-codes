#File: Basic_calculator.py
#This is a Basic_calculator based on python.
#Currently this supports addition, substraction, multiplication, division and raise to the power operations.
print("Currently this calculator can use +,-,x,/,^\n","1. +\n\t", "2. -\n\t" "3. x\n\t", "4. /\n\t", "5. ^\n\t")
#This simplify the program and make is user-friendly as the user have to just type a no. not the actual function.
operation=input("Enter the numer before operation you wanna use...\n")
#Using if contidion to process the information entered by the user.
if operation=="1":
    num1=float(input("Enter first number\n"))
    num2=float(input("Enter second number\n"))
    answer=num1 + num2
    print("Your answer is:", answer)
#First condition is for addition.
#Using elif because we have more than 2 conditions.
elif operation=="2":
    num1=float(input("Enter first number\n"))
    num2=float(input("Enter second number\n"))
    answer=num1 - num2
    print("Your answer is:", answer)
#Second condition is for substraction.
elif operation=="3":
    num1=float(input("Enter first number\n"))
    num2=float(input("Enter second number\n"))
    answer=num1 * num2
    print("Your answer is:", answer)
#Third condition is for multiplication.
elif operation=="4":
    num1=float(input("Enter first number\n"))
    num2=float(input("Enter second number\n"))
    answer=num1 / num2
    print("Your answer is:", answer)
#Forth condition is for division.
elif operation=="5":
    num1=float(input("Enter the number\n"))
    num2=float(input("Enter the power\n"))
    answer=num1**num2
    print("Your answer is:", answer)
#Fifth condition is for raise to the power operation.
else:
    print("Oops! seems like its not a valid option available")
#Finally the else condition used if the user type invalid option.
