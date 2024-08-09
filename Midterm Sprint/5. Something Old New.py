# Description: This program calculates the program with a new feature
# Author: Joshua Youden
# Date edited: Febuary 22nd, 2024


# Enter required liberaries
import calendar  # Be sure to import this or else it will not work

while True:
    # Enter a year that the code can display (and make sure it's a number NOT a letter)
    print()
    Year = int(input("Enter a year: "))

    # Enter a month that the code can display (and make sure it's a number NOT a letter)
    Month = int(input("Enter a month: "))

    # Here is where you will see the calender.

    print()
    print()
    print()
    # Print the calender using the following code to make it display
    print(calendar.month(Year, Month))
    # End program

    while True:
        continuePrompt = input("Do you want to generate another calendar (Y / N): ").upper()
        
        if continuePrompt == "":
            print("Data Entry Error - Continue option cannot be blank.")
        elif continuePrompt != "Y" and continuePrompt != "N":
            print("Data Entry Error - Continue option must be a Y or N.")
        else:
            break
    
    if continuePrompt == "N":
        break
print("\nProgram ended.")
