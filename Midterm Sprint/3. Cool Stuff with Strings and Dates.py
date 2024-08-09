# Description: This program generate employee ID, Username and Password
# Author: Adewale Gbadamosi
# Date: February 17, 2024

from datetime import datetime, timedelta

while True:
    # Employee information
    currentDate = datetime.now()
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'.,-")
    
    while True:
        firstName = input("Enter the employee first name:        ").strip().title()
        if firstName == "":
            print("Date Entry Error - employee first name can not be blank.")
        elif set(firstName).issubset(allowed_char) != True:
            print("Data Entry Error - employee first name contains invalid characters.")
        else:
            break
    
    while True:
        lastName = input("Enter the employee last name:         ").strip().title()
        if lastName == "":
            print("Date Entry Error - employee last name can not be blank.")
        elif set(lastName).issubset(allowed_char) != True:
            print("Data Entry Error - employee last name contains invalid characters.")
        else:
            break

    while True:
        try:
            startDateStr = input("Enter the start date (YYYY-MM-DD):    ").strip()
            startDate = datetime.strptime(startDateStr, "%Y-%m-%d")
        except:
            print("Data Entry Error - start date is not in a valid format.")
        else:
            break

    while True:
        try:
            birthDateStr = input("Enter the birthdate (YYYY-MM-DD):     ").strip()
            birthDate = datetime.strptime(birthDateStr, "%Y-%m-%d")
        except:
            print("Data Entry Error - birthdate is not in a valid format.")
        else:
            break
    
    while True:
        phoneNum = input("Enter phone number (9999999999):      ").strip()
        if phoneNum == "":
            print("Data Entry Error - Phone number cannot be blank")
        elif phoneNum.isdigit() == False:
            print("Data Entry Error - phone number must be digit number")
        if len(phoneNum) != 10:
            print("Data Entry Error - phone number must 10 digit number")
        else:
            break
    

    # Employee ID based on initials and current date
    employeeID = f"{firstName[0]}{lastName[0]}{startDate.strftime('%Y%m%d')}"

    # Username based on first name, last name, and birthdate
    username = f"{firstName.lower()}.{lastName.lower()}{birthDate.strftime('%y')}"

    # Password based on reversed last name and birth year
    password = f"{lastName[::-1]}{birthDate.strftime('%Y')}"

    # Years and days worked with the company
    yearsWorked = (currentDate - startDate).days // 365
    daysWorked = (currentDate - startDate).days % 365

    # Years until retirement (assuming retirement age is 65)
    retirementAge = 65
    yearsToRetirement = retirementAge - (currentDate.year - birthDate.year)

    # Days until next birthday
    nextBirthDay = datetime(currentDate.year, birthDate.month, birthDate.day)
    if nextBirthDay < currentDate:
        nextBirthDay = nextBirthDay.replace(year=currentDate.year + 1)
    daysUntilBirthday = (nextBirthDay - currentDate).days

    # Display results
    print(f"\n------------------------------------------------")
    print(f"            AJ Service Limited")
    print(f"   121 Elizabeth Avenue, St. John's NL A1B3G4")
    print(f"------------------------------------------------")
    print("\nEmployee Profile:")
    print(f"-----------------")
    print(f" First Name:   {firstName}")
    print(f" Last Name:    {lastName}")
    print(f" Phone Number: {phoneNum}")
    print(f" Start Date:   {startDate.strftime('%B %d, %Y')}")
    print(f" Birthdate:    {birthDate.strftime('%B %d, %Y')}")
    print("\nEmployee Details:")
    print(f"-----------------")
    print(f" Employee ID:  {employeeID}")
    print(f" Username:     {username}")
    print(f" Password:     {password}")
    print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"+  Years and Days Worked:    {yearsWorked} years, {daysWorked} days  +")
    print(f"+  Years Until Retirement:   {yearsToRetirement} years           +")
    print(f"+  Days Until Next Birthday: {daysUntilBirthday} days           +")
    print(f"+++++++++++++++++++++++++++++++++++++++++++++++++")
    print()

    while True:
        continuePrompt = input("Do you want to process another employee (Y / N): ").upper()
        
        if continuePrompt == "":
            print("Data Entry Error - Continue option cannot be blank.")
        elif continuePrompt != "Y" and continuePrompt != "N":
            print("Data Entry Error - Continue option must be a Y or N.")
        else:
            break
    
    if continuePrompt == "N":
        break
print("\nProgram ended.")