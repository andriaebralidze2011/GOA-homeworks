# 1) შექმენით პროგრამა რომელიც while ციკლის მეშვეობით დაბეჭდავს თქვენს სახელს 5 ჯერ

i = 0

while i < 5:
    print("andria")
    i += 1

# 2) შექმენით პროგრამა რომლითაც დაითვლით 0დან 10ის ჩათვლით რიცხვთა ჯამს

total_sum = 0
i = 0

while i <= 10:
    total_sum += i
    i += 1
    
print(total_sum)    
# 3) მომხმარებელს შემოატანინეთ რიცხვი თქვენი დავალებაა ნულიდან მაგ რიცხვის ჩათვლით გამოთვალოთ მხოლოდ ლუწების ჯამი (გამოიყტენეთ whle ციკლი არანაირი if-else არ გჭირდებათ)

num = int(input("please enter your number: "))

total_sum = 0
i = 0

while i <= num:
    total_sum += i
    i += 2
    
print(total_sum)


#4) შექმენით ცვლადი სახელად saved_password სადაც შეინახავთ თქვენს სასურველ პაროლს მაგალითად "123", შემდეგ მომხმარებელს შემოატანინეთ პაროლი password_input ცვლადში, თქვენი დავალებაა მომხმარებელს იქამდე შემოატანინოთ პაროლი *სანამ შემოტანილი პაროლი არ იქნება შენახული პაროლის ტოლი

saved_password = "123"

password_input = input("enter password: ")

while password_input != saved_password:
    password_input = input("password is incorrect try again: ")

print("password is correct")


# 5) მომხმარებელს შემოაყვანინეთ თავისი ასაკი, შემდგომ იმ შემთხვევაში თუ მისი ასაკი მეტია 18-ზე დაეწერეთ "You are adult!", ყველა სხვა შემთხვევაში დაუწერეთ "You are not adult!".

age = int(input("please enter your number: "))

if age>= 18:
    print("you are adult")
else:
    print("you are not adult")

# 6) მომხმარებელს შემოაყვანინეთ ერთი რიცხვი, შემდგომ შეამომწეთ, იმ შემთხვევაში თუ რიცხვი ლუწია გამოუტანეთ ტერმინალში "Your number is even!" ყველა სხვა შემთხვევაში "Your number is odd!"

num = int(input("please enter your number: "))

if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd") 

# 7) მომხმარებელს შემოაყვანინეთ სამი რიცხვი, თქვენი დავალებაა გაარკვიოთ ამ სამიდან რომელი რიცხვი არის ყველაზე დიდი, გამოიყენეთ if, elif და else.

num1 = int(input("please enter num1: "))
num2 = int(input("please enter num2: "))
num3 = int(input("please enter num3: "))

if num1 > num2 and num1 > num3:
    print("num1 is biggest")
elif num2 > num1 and num2 > num3:
    print("num2 is biggest")
else:
    print("num3 is biggest")