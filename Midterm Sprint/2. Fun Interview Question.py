# Description: This is loop that execute 100 times and displaying Fizz, Buzz and FizzBuzz if divisible by 5, 8 and (5 & 8) respectively.
# Author: Adewale Gbadamosi
# Date: February 16, 2024

    
while True:
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
print("\nProgram ended.")