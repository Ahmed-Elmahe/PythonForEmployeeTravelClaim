# Description: This is the program for generating 12 characters random password 
# Author: Adewale Gbadamosi
# Date: February 18, 2024

# import the secrets module, which provides functions for generating random numbers
# import the string module, which provides a collection of constants representing ASCII character sets.
import secrets
import string
import calendar

def calSome():
    while True:
        print()
        while True:
            month = int(input("Enter the month: "))
            year = int(input("Enter the year: "))

            print(calendar.month(year, month))
            break

        while True:
            # Define the characters to use for generating the password
            characters = string.ascii_letters + string.digits + string.punctuation

            # Initialize an empty string to store the password
            password = ""

            # Generate a random password of length 12
            for _ in range(12): # '_' used as placeholder variable name as the value is not used
                password += secrets.choice(characters)

            # Example - Display the generated password
            print()
            print("|---------------------------------|")
            print("|Generated Password:", password, "|")
            print("|---------------------------------|")
            print()

            break
        
        while True:
            continuePrompt = input("Do you want to generate another passwaord (Y / N): ").upper()

            if continuePrompt == "":
                print("Data Entry Error - Continue option cannot be blank.")
            elif continuePrompt != "Y" and continuePrompt != "N":
                print("Data Entry Error - Continue option must be a Y or N.")
            else:
                break
        
        if continuePrompt == "N":
            break
    print("\nProgram ended.")
