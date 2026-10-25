# 2) მომხმარებელს შემოაყვანინეთ რაიმე რიცხვი, თქვენი დავალებაა გაიგოთ მომხამრებლის რიცხვი დადებითია, უარყოფითი თუ ნულის ტოლი და გამოუტანეთ შესაბამისი შეტყობინება ტერმინალში ყოველი პირობისთვის.
num = int(input("please enter your number: "))

if num > 0:
    print("your number is higher than 0")
elif num < 0:
    print("your number is lower than 0")
else:
    print("your number equals 0")

# 3) მომხმარებელს შემოაყვანინეთ ქულა, შემდგომ შეამოწმეთ ქულის დიაპაზონი და გამოუტანეთ შესაბამისი შეფასებები:

# 90–100 ქულა — A
# 80–89 ქულა — B
# 70–79 ქულა — C
# 60–69 ქულა — D
# 0–59 ქულა — F

# თუ მომხმარებელი შეიყვანს არასწორ ქულას (0-ზე ნაკლებს ან 100-ზე მეტს), პროგრამამ უნდა გამოიტანოს შესაბამისი შეტყობინება.

grade = int(input("please enter your grade: "))

if grade > 90 and grade < 100:
    print("A")
elif grade > 80 and grade < 89:
    print("B")
elif grade > 70 and grade < 79:
    print("C")
elif grade > 60 and grade < 69:
    print("D")
else:
    print("F")

# 4) შექმენით პროგრამა, რომელშიც წინასწარ განსაზღვრავთ ერთ საიდუმლო რიცხვს. მომხმარებელმა უნდა გამოიცნოს ეს რიცხვი while ციკლის გამოყენებით, იქამდე სანამ მომხმარებელი არ გამოიცნობს რიცხვს - ციკლი არ გათიშოთ და მოსთხოვეთ ყოველი შეცდომის შემდეგ რიცხვის კიდევ ერთხელ შემოყვანა, თუ გამოიცნო რიცხვი - "You guessed the number!"

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:
    print("Wrong number! Try again.")
    guess = int(input("Guess the number: "))

print("You guessed the number!")

# 5) მომხმარებელს შემოაყვანინეთ 2 რიცხვი და ერთი რაიმე ოპერატორი (+, -, *, /) და ოპერატორიდან გამომდინარე მომხმარებელს გამოუტანეთ ტერმინალში მათემატიკური ოპერაციის შედეგი ამ ორ რიცხვს შორის.

num1 = float(input("please enter your number: "))
num2 = float(input("please enter your number: "))
operator = input("please enter your operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
else:
    print(num1 / num2)