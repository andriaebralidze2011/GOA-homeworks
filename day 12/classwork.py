# # 1) მომხმარებელს შემოაყვანინეთ თავისი სახელი, გვარი, ასაკი და საყვარელი ფერი, შემდგომ შექმენით ლისტი სახელად "user_info" და შეინახეთ ამ ლისტში მომხმარებლისმიერ შემოყვანილი ინფორმაცია.

first_name = input("please enter your name: ")
last_name = input("please enter your name: ")
age = int(input("please enter your age: "))
favourite_color = input("please enter your favourite color: ")


list = [first_name, last_name, favourite_color , age]

print(list)
# 2) შექმენით მასივი რომელშიც შეინახავთ მინიმუმ 10 სახელს, შემდგომ 3 მათგანი ჩაანაცვლეთ სხვა სახელებით პროგრამულად.

names = ["andria" , "saba", "luka", "aleqsandre", "nika", "avtandili", "ivane", "merabi", "jemali", "romani"]

names[3] = "giga"
names[4] = "guga"
names[7] = "gaga"

print(names)
# 3) მოიძიეთ ინფორმაცია იმის შესახებ, თუ როგორ უნდა გადაუაროთ ლისტს for ციკლის დახმარებით, შემდგომ წინა დავალებაში შექმნილ ლისტს გადაუარეთ for ციკლის დახამრებით და გამოიტანეთ ყველა სახელი რიგ-რიგობით ტერმინალში.

names = ["andria" , "saba", "luka", "aleqsandre", "nika", "avtandili", "ivane", "merabi", "jemali", "romani"]

names[3] = "giga"
names[4] = "guga"
names[7] = "gaga"

for i in names:
    print(i)


