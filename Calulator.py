# This program is made by Abhinav Raj.
# You can contact the developer at E-Mail - abhinavraj081006@gmail.com
# To make program whose main function is to perform basic arithematic operations like addition, subtraction, multiplication and division.


# Importing the required module.
import os
import sys
import argparse
import random
import datetime
import time
import math

# Printing the time of usage.
current_time = datetime.datetime.now()
print("Time of using the program:", current_time)
print(" ")

# Print the purpose of writing the program.
print("Hi there! How are you doing....?😊")
print("This program is written to perform basic arithematic operations like addition, subtraction, multiplication and division.")
print("Please enter the numbers when asked.")

# Jokes part.
print("Ohh..! your PC is so slow.💀💀")
print("Let me handle it.😎")
print(" ")
time.sleep(5)

# Taking input from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Please wait for a moment...")
time.sleep(3)

# Asking for the operation to be performed.
print(" ")
print("Please select the operation you want to perform.")
print("You can select from the following operations:")
sys.stdout.write("For addition, type \033[1m'add'\033[0m. ")
sys.stdout.write("For subtraction, type \033[1m'sub'\033[0m. ")
sys.stdout.write("For multiplication, type \033[1m'mul'\033[0m. ")
print("For division, type \033[1m'div'\033[0m.")
op = input("Enter the operation you want to perform: ")
print(" ")

# Performing the operation.
# Printing the result
if op == 'add':
    print("Performing addition...")
    result = num1 + num2
    print(f"The result is: {result}")
elif op == 'sub':
    print("Performing subtraction...")
    result = num1 - num2
    print(f"The result is: {result}")
elif op == 'mul':
    print("Performing multiplication...")
    result = num1 * num2
    print(f"The result is: {result}")
elif op == 'div':
    print("Performing division...")
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")


# To thanks the user.
print(" ")
print("Thanks for using the program.😊")