#1
number = int(input("Please enter number: "))
count = 0

for i in range(1, 11):
    result = i * number

    if result % 3 == 0:
        print(f"{number} X {i} = {result}   |  Divisible by 3")
        count += 1
    else:
        print(f"{number} X {i} = {result}   |  Not divisible by 3")

print("Total divisible by 3:", count)

#2

balance = 0
success_withdrawl = 0
success_deposit = 0


while True:
    print (
    """
    ====== BANK SYSTEM ======
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Transaction Summary
    5. Exit
    =========================
    """
    )

    choice = int(input("Please enter choice: "))

    if choice == 1:
        # We show user current balance
        print("Current balance:", balance)
    elif choice == 2:
        # Make user to input deposit money
        deposit = int(input("Please enter deposit money: "))

        # If deposit is valid then add to balance else tell user that its invalid 
        if deposit > 0:
            balance += deposit
            print("Succesfully deposit:", deposit)
            print("Current balance:", balance)

            # Increment quantity of success deposit by one
            success_deposit += 1
        else:
            print("Deposit money is invalid! try again!")
    elif choice == 3:
        # First make user input withdrawl money
        withdrawl = int(input("Please enter withdrawl money: "))

        # Second check if it is valid
        if withdrawl > 0 and withdrawl <= balance:
            # Subtract widthrawl money to balance
            balance -= withdrawl
            print("Succsesfully withdrawl:", withdrawl)
            success_withdrawl += 1
        else:
            print("withdrawl money is invalid or more then balance! try again!")
    elif choice == 4:
        print (
    f"""
    ====== TRANSACTION SUMMARY ======
    Current Balance: {balance} GEL
    Total Deposits: {success_deposit}
    Total Withdrawals: {success_withdrawl}
    Money Deposited: 500 GEL
    Money Withdrawn: 200 GEL
    =================================
    """
    )
    elif choice == 5:
        print("👋 Thank you for using our bank!")
        break
    else:
        print("Invalid option! try again!")