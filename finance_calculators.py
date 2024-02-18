import math

# display menu
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment      - to calculate the amount of interest you'll earn on interest")
print("bond            - to calculate the amount you'll have to pay on a home loan")
choice = input("\nYour choice: ")
print()

# if the user chooses investment
if choice.lower() == "investment":
    # input the amount of money that they are depositing
    P = float(input("Enter the deposit amount: "))
    # input the interest rate
    r = float(input("Enter the interest rate: "))
    r /= 100
    # input the number of years they plan on investing for
    t = int(input("Enter the number of years: "))
    # input whether they want simple or compound interest
    interest = input("Enter the type of interest to be applied(simple/compound): ")

    # variable to store the computed interest amount
    A = 0
    # if the user chooses simple interest
    if interest.lower() == "simple":
        # compute the simple interest using the given formula
        A = P * (1 + r * t)
    # else if the user chooses compound interest
    elif interest.lower() == "compound":
        # compute the compound interest using the given formula
        A = P * math.pow((1 + r), t)
    print()

    # print out the computed interest amount
    print(f"The {interest} interest is: {A:.2f}")

# else if the user chooses bond
elif choice.lower() == "bond":
    # input the present value of the house
    P = float(input("Enter the house value: "))
    # input the interest rate
    r = float(input("Enter the annual interest rate: "))
    # input the number of months they plan to take to repay the loan
    n = int(input("Enter the number of months: "))

    # compute the monthly interest rate
    i = (r / 12) / 100

    # compute the monthly payment using the given formula
    x = (i * P) / (1 - math.pow((1 + i),(-n)))
    
    print()
    # print out the computed monthly payment
    print(f"The monthly payment is: {x:.2f}")

# else the user selects an invalid choice
else:
    print("Invalid choice!")