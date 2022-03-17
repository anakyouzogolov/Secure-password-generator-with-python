
# import all python modules needed

import random
import string

import subprocess

# *********************** head **********************

# password list to store all
password_list = []

# get number, lower and upper letters, symbols from string python module
lowercase = string.ascii_lowercase
uppercae = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# get password length from user input
length = int(input("Password Length :"))


#
lowercase_option = input("Include Lowercase : (y/n) ")
while(lowercase_option != "y" and lowercase_option != "n"):
    lowercase_option = input(
        "Include Lowercase type 'y' for yes or 'n' for no : (y/n) ")

    if(lowercase_option == "y"):
        password_list.append(lowercase)
    elif(lowercase_option == "n"):
        print("Lowercase Excluded !!")


# *********************** body **********************
# ********************** password generation logic *************************
#
uppercae_option = input("Include Uppercae : (y/n) ")
while(uppercae_option != "y" and uppercae_option != "n"):
    uppercae_option = input(
        "Include Uppercae type 'y' for yes or 'n' for no : (y/n) ")
else:
    if(uppercae_option == "y"):
        password_list.append(uppercae)
    elif(uppercae_option == "n"):
        print("Uppercae Excluded !!")


#
numbers_option = input("Include Numbers : (y/n) ")
while(numbers_option != "y" and numbers_option != "n"):
    numbers_option = input(
        "Include Numbers type 'y' for yes or 'n' for no : (y/n) ")
else:
    if(numbers_option == "y"):
        password_list.append(numbers)
    elif(numbers_option == "n"):
        print("Numbers Excluded !!")


#
symbols_option = input("Include Symbols : (y/n) ")
while(symbols_option != "y" and symbols_option != "n"):
    symbols_option = input(
        "Include Symbols type 'y' for yes or 'n' for no : (y/n) ")
else:
    if(symbols_option == "y"):
        password_list.append(symbols)
    elif(symbols_option == "n"):
        print("Symbols Excluded !!")


# *********************** footer **********************
# convert password_list to string to get random letters from it
password_str = "".join(password_list)


# Method to print our password result if any
def print_password(password):
    print("\n")
    print(f"*"*20 + "Your Password is :" + "*"*20)

    print(random_password)

    print(f"*"*60)


# password length condition
if(len(password_str) >= length):
    random_password = "".join(random.choices(password_str, k=length))
    print_password(random_password)
else:
    print("\n")
    print("Password Length Error, Try one more time !!")
    # execute this "python script.py" to run our script one more time
    # by using subprocess built-in python module
    subprocess.run(["python", "script.py"])
