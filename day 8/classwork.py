# 1) შექმენით ციკლი რომელიც 0_დან მომხმარებლის მიერ შემოტანილი რიცხვის ჩათვლით გამოითვლის ჯამს და საბოლოოდ დაბეჭდეთ ეს ჯამი

number = int(input("please enter your number: "))
sum = 0

for i in range(number + 1):
    sum = sum + i

print(sum)

# 2) მომხმარებელს შემოატანინეთ რიცხვი, თქვენი დავალებაა 0_დან მაგ რიცხვის ჩათვლით ყველა ლუწი რიცხვის ჯამი გამოთვალოთ და დაბეჭდოთ ჯამი

number = int(input("Please enter number: "))
sum = 0

for i in range(0, number + 1, 2):
    sum = sum + i

print(sum)