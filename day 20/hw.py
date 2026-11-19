# 2) შექმენით პროგრამა, რომელშიც თავდაპირველად იქნება 6 სხვადასხვა ხილი Set-ის სახით. მომხმარებელს შეაყვანინეთ ახალი ხილის სახელი და გამოიყენეთ add() მეთოდი მის დასამატებლად. საბოლოოდ დაბეჭდეთ განახლებული Set.

fruits = {"apple", "banana", "orange", "grape", "mango", "kiwi"}

fruits.add("watermelon")

print(fruits)

# 3) შექმენით მოსწავლეების Set, რომელშიც მინიმუმ 5 მოსწავლის სახელი იქნება. მომხმარებელს შეაყვანინეთ მოსწავლის სახელი და in ოპერატორის გამოყენებით შეამოწმეთ, არის თუ არა ეს მოსწავლე Set-ში. შესაბამისი შედეგი დაბეჭდეთ ტერმინალში.

students = {"andria", "aleqsandre", "saba", "luka", "nika"}

students_input = input("please enter student: ")

if students_input in students:
    print("he is in set")
else:
    print("he is not in set")

# 4) შექმენით რიცხვების Set, რომელშიც მინიმუმ 7 სხვადასხვა რიცხვი იქნება. მომხმარებელს შეაყვანინეთ რიცხვი და შეამოწმეთ, არის თუ არა ის Set-ში. შემდეგ გამოიყენეთ remove() მეთოდი ამ რიცხვის Set-იდან წასაშლელად. საბოლოოდ დაბეჭდეთ განახლებული Set.

nums = {1, 2, 3, 4, 5, 6, 7}

number = int(input("please enter number: "))

if number in nums:
    print(True)
else:
    print(False)

nums.remove(number)

print(nums)

# 5) შექმენით ცხოველების Set, რომელშიც მინიმუმ 6 სხვადასხვა ცხოველი იქნება. გამოიყენეთ len() ფუნქცია, რათა გაიგოთ, რამდენი ელემენტია Set-ში. შემდეგ მომხმარებელს შეაყვანინეთ ახალი ცხოველის სახელი და add() მეთოდის გამოყენებით დაამატეთ Set-ში. საბოლოოდ დაბეჭდეთ განახლებული Set და მისი სიგრძე.

animals = {"lion", "zebra", "girraffe", "tiger", "dog", "cat"}

print(len(animals))

animals_input = input("please enter animal: ")

animals.add(animals_input)

print(len(animals))
print(animals)

# 6) შექმენით პროგრამა, რომელშიც თავდაპირველად იქნება 5 სხვადასხვა ფერის Set. მომხმარებელს შეაყვანინეთ ორი ფერის სახელი. გამოიყენეთ in ოპერატორი, რათა შეამოწმოთ, არის თუ არა ორივე ფერი Set-ში. თითოეული შემოწმების შედეგი ცალ-ცალკე დაბეჭდეთ ტერმინალში.

colors = {"red", "blue", "green", "yellow", "pink"}

colors_input1 = input("please enter color: ")
colors_input2 = input("please enter color: ")

if colors_input1 in colors:
    print("first color is in set")
else:
    print("first color is not in set")

if colors_input2 in colors:
    print("second color is in set")
else:
    print("second color is not in set")