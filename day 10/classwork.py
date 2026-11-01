# #1
# age = int(input("please enter your number: "))

# if age <= 13:
#     print("you are child")
# elif age > 13 and age <= 17:
#     print("you are teenager")
# else:
#     print("you are adult")

# #2
# num = int(input("enter number: "))

# for i in range(1,num + 1):
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# #3
# correct_password = "python123"
# input_password = ""
# tries = 0

# while input_password != correct_password and tries != 3:
#     tries += 1
#     input_password = input("Please enter correct password: ")

#     if input_password == correct_password:
#         print("✅ Access granted!")
#     elif tries == 3:
#         print("You tried 3 times! Blocked")
#     else:
#         print("❌ Try again!")

#4

students_count = int(input("Please enter students quantity: "))

for i in range(1, students_count + 1):
    grade = int(input(f"Please enter {i} student score: "))

    if grade >= 90 and grade <= 100:
        print(f"{i} student's score is A")
    elif grade >= 80 and grade < 90:
        print(f"{i} student's score is B")
    elif grade >= 70 and grade < 80:
        print(f"{i} student's score is C")
    elif grade >= 60 and grade < 70:
        print(f"{i} student's score is D")
    elif grade >= 0 and grade < 60:
        print(f"{i} student's score is F")
    else:
        print("Incorect grade")
        break

#5

current_balance = 500

print(f"current balance: {current_balance} GEL")

while True:
    amount = float(input("Enter withdrawal amount: "))

    if amount == 0:
        print("ATM SYSTEM ended")
        break
    elif amount < 0:
        print("invalid amount")
    elif amount > current_balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print("Withdrawal successful")
        print(f"remaining balance: {current_balance} GEL")