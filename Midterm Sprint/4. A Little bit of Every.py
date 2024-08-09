# Description: This program calculates equipment amortization
# Author: Adewale Gbadamosi
# Date: February 16, 2024

# importing library
from datetime import datetime, timedelta

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
            purchaseDate = datetime.strptime(purchaseDate, '%Y-%m-%d')
        except:
                print("Data Value Error - invalid date input")
        else:
                break

    def calMaintenanceDates(purchaseDate):
        # Calculate maintenance dates
        cleaningDate = purchaseDate + timedelta(days=10)
        tubeFluidCheckDate = purchaseDate + timedelta(weeks=3)
        majorInspectionDate = purchaseDate + timedelta(days=180)

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
print("\nProgram ended.")







