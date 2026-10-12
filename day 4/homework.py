# 2) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს:

# სახელს
# გვარს
# ასაკს
# საყვარელ ფერს

# ყველა ინფორმაცია შეინახეთ შესაბამის ცვლადებში და გამოიტანეთ ტერმინალში შემდეგი ფორმით:
# User full name: Saba Dzidzikashvili
# User age: 17
# Favorite color: red

name = input("please enter your name")
last_name = input("please enter your last_name")
age = input("please enter your age")
favourite_color = input("please enter your favourite color")

print("user name: " + name)
print("user last_name: " + last_name)
print("user age: " + age)
print("user favourite_color: " + favourite_color)

# 3) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს:

# საყვარელ მანქანას;
# საყვარელ ბრენდს;
# საყვარელ სუნამოს;
# საყვარელ სპორტს.

# შემდეგ ინფორმაცია გამოიტანეთ ტერმინალში შემდეგი ფორმით:

# My favorite car: Porsche
# My favorite brand: Nike
# My favorite perfume: Stronger With You
# My favorite sport: Football

My_favorite_car = input("please enter your favourite_car") 
My_favorite_brand = input("please enter your favourite brand")
My_favorite_perfume = input("please enter your favorite_perfume") 
My_favorite_sport = input("please enter your favorite_sport")

print("My favorite car:" + My_favorite_car)
print("My favorite brand:" + My_favorite_brand)
print("My favorite perfume:" + My_favorite_perfume)
print("My favorite sport:" + My_favorite_sport)

# 4)შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს:

# სახელს;
# ასაკს;
# სასურველ პროფესიას;
# ქვეყანას, სადაც მომავალში ცხოვრება სურს;

# შემდეგ ინფორმაცია გამოიტანეთ ტერმინალში შემდეგი ფორმით:
# My name is Gio.
# I am 16 years old.
# My dream profession is Programmer.
# I want to live in Germany.

name = input("please enter your name")
age = input("please enter your age")
dream_profession = input("please enter your dream profession")
country =  input("please enter the country you want to live in")

print("My name is " + name)
print("I am " + age)
print("My dream profession is " + dream_profession)
print("I want to live in " + country)

# 5) დეტალურად განმარტეთ რას აკეთებს input() ფუნქცია, ასევე ახსენით snake_case-ის სინტაქსი რა არის და რისთვის გვჭირდება.

#input ფუნქციის დახმარებით ტერმინალში შეგვიძლია შევიტანოთ წარწერა რომლითაც მოვთხოვთ მომხმარებელს სასურველ მნიშვნელობას

#snake_case-ი არის ფუნქცია რომლის გამოყენების გარეშეც კოდში არცერთი წარწერის დაშორება არ შეგვიძლია და ამოაგდებს ტერმინალში error-ს