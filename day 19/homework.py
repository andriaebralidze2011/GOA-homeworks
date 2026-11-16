# 2) შექმენით ხილის Tuple, რომელშიც მინიმუმ 6 სხვადასხვა ხილი იქნება. დაბეჭდეთ Tuple-ის პირველი, მესამე და ბოლო ელემენტები. საბოლოოდ გამოიტანეთ Tuple-ის სრული სიგრძე len() ფუნქციის გამოყენებით.

fruits = ("apple", "banana", "orange", "strawberry", "watermelon", "pineapple")

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(len(fruits))

# 3) შექმენით მოსწავლეების Tuple, რომელშიც მინიმუმ 5 მოსწავლის სახელი იქნება. მომხმარებელს შეაყვანინეთ მოსწავლის სახელი და შეამოწმეთ in ოპერატორის გამოყენებით, არის თუ არა ეს მოსწავლე Tuple-ში. შესაბამისი შედეგი დაბეჭდეთ ტერმინალში.

students = ("andria", "aleqsandre", "saba", "luka", "nika")

student_input = input("please enter students name: ")


if student_input in students:
    print("this student is in your tuple")
else:
    print("this student is not in your tuple")
# 4) შექმენით რიცხვების Tuple, რომელშიც მინიმუმ 7 რიცხვი იქნება. გამოიყენეთ count() მეთოდი, რათა გაიგოთ, რამდენჯერ მეორდება კონკრეტული რიცხვი Tuple-ში. ასევე გამოიყენეთ index() მეთოდი, რათა იპოვოთ ამ რიცხვის პირველი გამოჩენის ინდექსი.

numbers = (1, 5, 3, 7, 5, 20, 13)

print(numbers.count(5))
print(numbers.index(5))

# 5) შექმენით ქალაქების Tuple, რომელშიც მინიმუმ 6 ქალაქი იქნება. გამოიყენეთ slicing, რათა დაბეჭდოთ Tuple-ის პირველი სამი ელემენტი, შემდეგ კი ბოლო სამი ელემენტი. საბოლოოდ დაბეჭდეთ მთლიანი Tuple.

citys = ("tbilisi", "batumi", "kutaisi", "zugdidi", "telavi", "sarfi")

print(citys[0:3])
print(citys[3:7])
print(citys)