# 2) შექმენით პროგრამა, რომელშიც წინასწარ გექნებათ მოცემული 5 რიცხვისგან შემდგარი სია.

# პროგრამამ უნდა:

# - დაბეჭდოს სიის პირველი ელემენტი;
# - დაბეჭდოს სიის ბოლო ელემენტი;
# - დაბეჭდოს სიის მესამე ელემენტი;
# - for ციკლის გამოყენებით დაბეჭდოს სიის ყველა ელემენტი;
# - მომხმარებელს შეაყვანინოს ერთი რიცხვი და შეამოწმოს, ემთხვევა თუ არა ის სიის რომელიმე ელემენტს. თუ ემთხვევა, დაბეჭდოს შესაბამისი შეტყობინება.


list = [1, 2, 3, 4, 5]
#1
print(list[0])
#2
print(list[-1])
#3
print(list[2])
#4
for i in list:
    print(i)
#5
number = int(input("please enter number: "))

if number in list:
    print("This number is already in the list!Try again")
else:
    print("your number is added in the list ")

# 3) შექმენით სია, რომელშიც შეინახავთ 6 მოსწავლის ქულას.

# პროგრამამ უნდა:

# - for ციკლის გამოყენებით დაბეჭდოს ყველა ქულა;
# - დათვალოს, რამდენმა მოსწავლემ მიიღო 50 ან მეტი ქულა;
# - დათვალოს, რამდენმა მოსწავლემ მიიღო 50-ზე ნაკლები ქულა;
# - დაბეჭდოს მიღებული შედეგები.

grades = [35 ,60, 67, 39, 42, 50]
#1
for i in grades:
    print(i)
#2
count = 0

for grade in grades:
    if grade >= 50:
        count += 1
        
print("50 or more point were given to", count ,"students")
#3
count = 0

for grade in grades:
    if grade < 50:
        count += 1
        
print("lower than 50 points were given to", count ,"students")
# 4) მომხმარებელს შეაყვანინეთ 7 მთელი რიცხვი და შეინახეთ ისინი სიაში.

# პროგრამამ უნდა:

# - დაბეჭდოს ყველა შეყვანილი რიცხვი;
# - დათვალოს, რამდენი რიცხვია დადებითი;
# - დათვალოს, რამდენი რიცხვია უარყოფითი;
# - დათვალოს, რამდენი რიცხვია ნულის ტოლი;
# - დაბეჭდოს მიღებული შედეგები.

# BONUS
# ციკლისა და პირობითი ოპერატორების გამოყენებით იპოვეთ სიაში ყველაზე დიდი რიცხვი max() ფუნქციის გამოყენების გარეშე.


nums = [3, 6 ,-4, 9, -23, 45, 0]
#1
for i in nums:
    print(i)
#2
count = 0

for i in nums:
    if i > 0:
        count += 1
print(count,"numbers were higher than 0")
#3
count = 0

for i in nums:
    if i < 0:
        count += 1
print(count,"numbers were lower than 0")
#4
count = 0

for i in nums:
    if i == 0:
        count += 1
print(count,"number equals 0")
# 5) შექმენით პროგრამა, რომელშიც წინასწარ გექნებათ მოცემული 3 ფილმისგან შემდგარი სია.

# პროგრამამ უნდა:

# - დაბეჭდოს ყველა ფილმი for ციკლის გამოყენებით;
# - მომხმარებელს შეაყვანინოს ახალი ფილმის სახელი და დაამატოს ის სიაში (მოიძიეთ ინფორმაცია .append() მეთოდის შესახებ);
# - მომხმარებელს შეაყვანინოს ინდექსი და დაბეჭდოს ამ ინდექსზე არსებული ფილმი.

films = ["filmi1", "filmi2", "filmi3"]
#1
for i in films:
    print(i)
#2
new_film = input("enter your film: ")

films.append(new_film)

print(films)
#3
index = int(input("please enter your number: "))

if 0 <= index < len(films):
    print("film:", films[index])
else:
    print("this index doesnt exist!")