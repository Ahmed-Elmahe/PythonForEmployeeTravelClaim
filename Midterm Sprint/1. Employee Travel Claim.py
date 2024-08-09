# Description: This program calculate the employee travel claim
# Author: Adewale Gbadamosi
# Date: February 16, 2024

# importing library
import datetime, random


# Assigning constants
PER_DIEM_DAILY_RATE = 85.00
PER_KILOMETER_RATE = 0.17
RENTAL_DAILY_RATE = 65.00
MORE_THAT_3DAYS_BONUS = 100
EXTRA_KILOMETER_RATE = 0.04
EXECUTIVE_BONUS_RATE = 45.00
DEC15_22_BONUS = 50.00
HST_RATE = 0.15

# Gathering the input
while True:
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'.,-")
    while True:
        employeeNum = input("Enter the employee number:         ").strip()
        if employeeNum == "":
            print("Date Entry Error - employee number can not be blank.")
        elif len(employeeNum) != 5:
            print("Date Entry Error - employee number must be 5 digits.")
        elif employeeNum.isdigit() != True:
            print("Data Entry Error - employee number must be digit.")
        else:
            break

    while True:
        firstName = input("Enter the employee first name:     ").strip().title()
        if firstName == "":
            print("Date Entry Error - employee first name can not be blank.")
        elif set(firstName).issubset(allowed_char) != True:
            print("Data Entry Error - employee first name contains invalid characters.")
        else:
            break
    
    while True:
        lastName = input("Enter the employee last name:      ").strip().title()
        if lastName == "":
            print("Date Entry Error - employee last name can not be blank.")
        elif set(lastName).issubset(allowed_char) != True:
            print("Data Entry Error - employee last name contains invalid characters.")
        else:
            break

    while True:
            tripLocation = input("Enter the trip location:           ").strip().title()
            if tripLocation == "":
                print("Date Entry Error - trip location can not be blank.")
            elif set(tripLocation).issubset(allowed_char) != True:
                print("Data Entry Error - trip location contains invalid characters.")
            else:
                break
        
    while True:
        try:
            startDateStr = input("Enter the start date of the trip (YYYY-MM-DD): ").strip()
            startDate = datetime.datetime.strptime(startDateStr, "%Y-%m-%d")
        except:
            print("Data Entry Error - start date is not in a valid format.")
        else:
            break

    while True:
        try:
            endDateStr = input("Enter the end date of the trip (YYYY-MM-DD) - must be within 7 days of start day: ").strip()
            endDate = datetime.datetime.strptime(endDateStr, "%Y-%m-%d")
        except:
            print("Data Entry Error - end date is not in a valid format.")
        else:
            if (endDate - startDate).days > 7:
                print("Data Entry Error - end date must be within 7 days of start date.")
            else:
                break

    while True:
        vehicleUsed = input("Enter the vehicle used ('O' for owned and 'R' for rented):    ").strip().upper()
        if vehicleUsed == "":
            print("Data Entry Error - vehicle used entry can not be blank.")
        elif len(vehicleUsed) != 1:
            print("Data Entry Error - must be one letter ('O' for owned and 'R' for rented.)")
        elif vehicleUsed != "O" and vehicleUsed != "R":
            print("Data Entry Error - O or R must be entered for owned or rented respectively.")
        else:
            break
    
    while True:
        kiloTravelled = 0
        if vehicleUsed == "O":
            try:
                kiloTravelled = int(input("Enter the kilometer travelled:     "))
            except:
                print("Data Entry Error - not a valid number.")
            else:
                if kiloTravelled > 2000:
                    print("Data Entry Error - Kilometer travelled cannot exceed 2,000km")
                else:
                    break
        else:
            break
    
    while True:
        claimType = input("Enter the claim type ('E' for Executive and 'S' for Standard: ").strip().upper()
        if claimType == "":
            print("Data Entry Error - claim type can not be blank.")
        elif len(claimType) != 1:
            print("Data Entry Error - must be one letter ('E' for Executive or 'S' for Standard.)")
        elif claimType != "E" and claimType != "S":
            print("Data Entry Error - E or S must be entered for Executive or Standard respectively.")
        else:
            break
   
    # Calculating output
    numberOfDay = (endDate - startDate).days
    perDiemAmt = numberOfDay * PER_DIEM_DAILY_RATE

    vehicleUsage = ""
    vehicleUsedMessage = ""
    if vehicleUsed == "O":
        mileageAmt = kiloTravelled * PER_KILOMETER_RATE
        vehicleUsedMessage = "Mileage Amount"
        vehicleUsage = "Owned"
    else:
        mileageAmt = numberOfDay * RENTAL_DAILY_RATE
        vehicleUsedMessage = "Rental Amount"
        vehicleUsage = "Rented"
    
    bonus = 0
    if numberOfDay > 3:
        bonus += 100

    if  kiloTravelled > 1000 and vehicleUsed == "O":
        bonus = bonus + (kiloTravelled * EXTRA_KILOMETER_RATE)

    if claimType == "E":
        bonus = bonus + (numberOfDay * EXECUTIVE_BONUS_RATE)
        claimType = "Executive"
    else:
        claimType = "Standard"

    if startDate.month == 12 and 15 <= startDate.day <= 22:
        bonus = bonus + (numberOfDay * DEC15_22_BONUS)

    claimAmt = perDiemAmt + mileageAmt + bonus
    tax = claimAmt * HST_RATE

    totalClaim = claimAmt + tax

    
    # Displaying and formatting the outputs
    print(f"")
    print(f" ------------------------------------------")
    print(f"          NL Chocolate Company")
    print(f"         Employee Travel Claims")
    print(f" ------------------------------------------")
    print(f"")
    print(f" Employee: {employeeNum:>5s}")
    print(f"           {firstName[0]}. {lastName:<24s}")
    print(f"")
    print(f" Trip Location:      {tripLocation}")
    print(f" Start Date:         {startDateStr}")
    print(f" End Date:           {endDateStr}")
    print(f" Number of Days:    {numberOfDay:>2d} days")
    print(f"")
    print(f" Claim Type:         {claimType:<10s}")
    print(f" Vehicle Used:       {vehicleUsage}")
    # Print mileage only if the vehicle used is owned
    if vehicleUsed == "O":
        print(f" Kilometer Travel:   {kiloTravelled:>4d} km")
    print(f"")
    perDiemAmtDsp = "${:,.2f}".format(perDiemAmt)
    print(f" Per Diem Amount:                 {perDiemAmtDsp:>9s}")
    mileageAmtDsp = "${:,.2f}".format(mileageAmt)
    # Displaying either mileage amount or rental amount based on vechicle used type
    print(f" {vehicleUsedMessage:<14s}:                  {mileageAmtDsp:>9s}")
    bonusDsp = "${:,.2f}".format(bonus)
    print(f" Bonus:                           {bonusDsp:>9s}")
    print(f"                                  ---------")
    claimAmtDsp = "${:,.2f}".format(claimAmt)
    print(f" Claim Amount:                    {claimAmtDsp:>9s}")
    taxDsp = "${:,.2f}".format(tax)
    print(f" Tax (HST):                       {taxDsp:>9s}")
    print(f"                                  ---------")
    totalClaimDsp = "${:,.2f}".format(totalClaim)
    print(f" Total Claim Amount:              {totalClaimDsp:>9s}")
    print(f" ------------------------------------------")
    print(f"")
    print(f"       Issued: {datetime.date.today()}")
    print(f"       Claim Reference: {firstName[0]}{lastName[0]}-{employeeNum[3:]}-{random.randint(0,9999)}")
    print(f"")
    print(f" ------------------------------------------")
    print() # Space for the next iteration

    # Prompt for next iteration
    while True:
        continuePrompt = input("Do you want to process another travel claim (Y / N): ").upper()
        
        if continuePrompt == "":
            print("Data Entry Error - Continue option cannot be blank.")
        elif continuePrompt != "Y" and continuePrompt != "N":
            print("Data Entry Error - Continue option must be a Y or N.")
        else:
            break
    
    if continuePrompt == "N":
        break
print("\nProgram ended.")


    



    