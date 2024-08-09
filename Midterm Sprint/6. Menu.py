# Description: Midterm Sprint - Main menu
# Author: Adewale Gbadamosi/ Joshua Youden
# Date: February 22, 2024.

# importing library
import datetime, random, calendar

# Assigning constants
PER_DIEM_DAILY_RATE = 85.00
PER_KILOMETER_RATE = 0.17
RENTAL_DAILY_RATE = 65.00
MORE_THAT_3DAYS_BONUS = 100
EXTRA_KILOMETER_RATE = 0.04
EXECUTIVE_BONUS_RATE = 45.00
DEC15_22_BONUS = 50.00
HST_RATE = 0.15
CUR_DATE = datetime.date.today()

# Program counters for main menu
genCalendar = 0
travelClaim = 0
funQues = 0
empDetail = 0
equipService = 0

# Description: This program calculate the employee travel claim
def calTravelClaim():
    # Gathering the input
    global travelClaim
    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'.,-")
        print()
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

        travelClaim += 1

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
    
    print("\n Employee Travel Claim Program ended.")

# Description: This is loop that execute 100 times and displaying Fizz, Buzz and FizzBuzz if divisible by 5, 8 and (5 & 8) respectively.
def fizzBuzzProblem():
    while True:
        global funQues
        counter = 1
        while counter <= 100:
            if counter % 5 == 0 and counter % 8 == 0:
                print("FizzBuzz")
            elif counter % 5 == 0:
                print("Fizz")
            elif counter % 8 == 0:
                print("Buzz")
            else:
                print(counter)
            counter += 1

        funQues += 1

        while True:
            continuePrompt = input("Do you want to play another game (Y / N): ").upper()
            
            if continuePrompt == "":
                print("Data Entry Error - Continue option cannot be blank.")
            elif continuePrompt != "Y" and continuePrompt != "N":
                print("Data Entry Error - Continue option must be a Y or N.")
            else:
                break
        
        if continuePrompt == "N":
            break
    print("\nFizz Buzz Program ended.")

def createStringDate():
    global empDetail
    while True:
        # Employee information
        currentDate = datetime.datetime.now()
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
                startDate = datetime.datetime.strptime(startDateStr, "%Y-%m-%d")
            except:
                print("Data Entry Error - start date is not in a valid format.")
            else:
                break

        while True:
            try:
                birthDateStr = input("Enter the birthdate (YYYY-MM-DD):     ").strip()
                birthDate = datetime.datetime.strptime(birthDateStr, "%Y-%m-%d")
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
        nextBirthDay = datetime.datetime(currentDate.year, birthDate.month, birthDate.day)
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

        empDetail += 1

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

   
    print("\nEmployee Employement Details Program ended.")

def DetAmortization():
    global equipService
    while True:
    # Input cost and purchase date
        while True:
            try:
                cost = float(input("Enter the cost of the equipment: "))
            except:
                print("Data Value Error - invald input")
            else:
                break
        
        while True:
            try:
                purchaseDate = input("Enter the purchase date (YYYY-MM-DD): ")
                # Convert purchaseDate string to datetime object
                purchaseDate = datetime.datetime.strptime(purchaseDate, '%Y-%m-%d')
            except:
                    print("Data Value Error - invalid date input")
            else:
                    break

        def calMaintenanceDates(purchaseDate):
            # Calculate maintenance dates
            cleaningDate = purchaseDate + datetime.timedelta(days=10)
            tubeFluidCheckDate = purchaseDate + datetime.timedelta(weeks=3)
            majorInspectionDate = purchaseDate + datetime.timedelta(days=180)

            return cleaningDate, tubeFluidCheckDate, majorInspectionDate

        def calAmortization(cost):
            global salvageValue
            # Calculate salvage value (10% of the purchase cost)
            salvageValue = 0.10 * cost
            # Calculate number of months in the useful life (15 years)
            numMonths = 15 * 12
            # Calculate monthly amortization
            amortization = (cost - salvageValue) / numMonths

            return amortization

        # Calculate maintenance dates
        cleaningDate, tubeFluidCheckDate, majorInspectionDate = calMaintenanceDates(purchaseDate)

        # Calculate amortization
        amortization = calAmortization(cost)

        # Print formatted output
        print(f" \n                   XYZ Equipment")
        print(f"               131 Elizabeth Avenue")
        print(f"               --------------------")
        print(f" \nMaintenance Schedule")
        print(f"\n Basic Cleaning (10 days):        {cleaningDate.strftime('%B %d, %Y')}")
        print(f" Tube and Fluid Checks (3 weeks): {tubeFluidCheckDate.strftime('%B %d, %Y')}")
        print(f" Major Inspection (6 months):     {majorInspectionDate.strftime('%B %d, %Y')}")
        print(" \nMonthly Amortization")
        costDsp = "${:,.2f}".format(cost)
        salvageValueDsp = "${:,.2f}".format(salvageValue)
        amortizationDsp = "${:,.2f}".format(amortization)
        print(f"\n Cost of Equipment:                {costDsp:>10s}")
        print(f" Salvage Value:                    {salvageValueDsp:>10s}")
        print(f"\n Monthly Amortization:             {amortizationDsp:>10s}")
        print(f"\n --------------------------------------------")
        print() # Space for the next iteration

        equipService += 1

        # Prompt for next iteration
        while True:
            continuePrompt = input("Do you want to process another amortization (Y / N): ").upper()
            
            if continuePrompt == "":
                print("Data Entry Error - Continue option cannot be blank.")
            elif continuePrompt != "Y" and continuePrompt != "N":
                print("Data Entry Error - Continue option must be a Y or N.")
            else:
                break
        
        if continuePrompt == "N":
            break
    print("\nEquipment Service Details Program ended.")

# Description: This program calculates the program with a new feature
def showCalendar():
    global genCalendar
    while True:
        # Enter a year that the code can display (and make sure it's a number NOT a letter)
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

        genCalendar +=1

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
    print("\nShow Calendar Program ended.")

while True:
    print()
    print("**********************************************")
    print("This is the beginning of a new program session ")
    print("**********************************************")
    print("")
    print("Quick Problems Solving - Main Menu")
    print(f"Date: {CUR_DATE}")
    print(f"Session totals:  Travel Claim: {travelClaim} Fun Question: {funQues} Employee Details: {empDetail} Equipment Srevice: {equipService}  Calendar: {genCalendar}")
    print()
    print("1. Employee Travel Claim.")
    print("2. Fun Interview Question - Fizz/Buzz.")
    print("3. Employee Employment Details.")
    print("4. Equipment Service Details and Amortization.")
    print("5. Displaying Calendar.")
    print("6. Quit")
    print()
   
    while True:
        try:
            Choice = input("Enter choice (1 - 9): ")
            Choice = int(Choice)
        except:
            print("Data Entry Error - must be a valid number between 1 and 6.")
        else:
            if Choice < 1 or Choice > 6:
                print("Data Entry Error - must be a valid number between 1 and 6.")
            else:
                break
            
    if Choice == 1:
        calTravelClaim()
    elif Choice == 2:
        fizzBuzzProblem()
    elif Choice == 3:
       createStringDate()
    elif Choice == 4:
        DetAmortization()
    elif Choice == 5:
        showCalendar()
    else:
        break
 
# Any housekeeping duties at the end of the program.
print("\nProgram ended.")
print("Thanks for using Quick Problems Solving.")
print("\nSummary of your session: ")
print(f"Travel Claim: {travelClaim} \nFun Question: {funQues} \nEmployee Details: {empDetail} \nEquipment Srevice: {equipService}  \nCalendar: {genCalendar}")
print("Total Sessions: ", travelClaim + funQues + empDetail + equipService + genCalendar)