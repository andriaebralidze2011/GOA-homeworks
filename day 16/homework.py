# 2) შექმენით ფუნქცია სახელად check_number(), რომელსაც გადაეცემა ერთი რიცხვი. ფუნქციამ უნდა შეამოწმოს:

# - თუ რიცხვი დადებითია, დააბრუნოს "Positive".
# - თუ რიცხვი უარყოფითია, დააბრუნოს "Negative".
# - თუ რიცხვი ნულის ტოლია, დააბრუნოს "Zero".

# მომხმარებელს რიცხვი შეაყვანინეთ input()-ის დახმარებით და ფუნქციის დაბრუნებული შედეგი გამოიტანეთ ტერმინალში.

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-2))

# 3) შექმენით ფუნქცია სახელად calculate_sum(), რომელსაც გადაეცემა ერთი რიცხვი. ფუნქციამ for ციკლის დახმარებით უნდა შეკრიბოს 1-დან გადაცემულ რიცხვამდე არსებული ყველა მთელი რიცხვი და დააბრუნოს მათი ჯამი.

# მაგალითად: calculate_sum(5) -> 15, რადგან 1 + 2 + 3 + 4 + 5 = 15.

def calculate_sum(number):
    total = 0
    for i in range(1,number + 1):
        total += i
    return total

print(calculate_sum(5))

# 4) შექმენით ფუნქცია სახელად calculator(), რომელსაც გადაეცემა სამი არგუმენტი: პირველი რიცხვი, მეორე რიცხვი და მათემატიკური ოპერაცია (+, -, *, /).

# ფუნქციამ if/elif/else პირობების დახმარებით უნდა განსაზღვროს, რომელი ოპერაცია უნდა შეასრულოს:

# - თუ ოპერაცია არის +, შეკრიბეთ რიცხვები.
# - თუ ოპერაცია არის -, გამოაკელით.
# - თუ ოპერაცია არის *, გაამრავლეთ.
# - თუ ოპერაცია არის /, გაყავით.
# - თუ მომხმარებელი უცნობ ოპერაციას შეიყვანს, გამოიტანეთ "Invalid Operation".

# გაითვალისწინეთ ნულზე გაყოფის შემთხვევაც.

# მაგალითად: calculator(10, 5, "+") -> 15.

def calculator(num1, num2, mathematical_operation):
    if mathematical_operation == "+":
        return num1 + num2
    elif mathematical_operation == "-":
        return num1 - num2
    elif mathematical_operation == "*":
        return num1 * num2
    else:
        return num1 / num2

print(calculator(10, 5, "/"))  

# 5) შექმენით ფუნქცია სახელად password_checker(), რომელსაც გადაეცემა ერთი არგუმენტი - მომხმარებლის მიერ შეყვანილი პაროლი.

# ფუნქციამ უნდა შეამოწმოს, რამდენად ვალიდურია გადმოცემული პაროლი.

# პაროლი ითვლება ვალიდურად იმ შემთხვევაში, თუ:
# - პაროლის სიგრძე 8 სიმბოლოზე მეტია.
# - პაროლში არის მინიმუმ 1 ასო.
# - პაროლში არის მინიმუმ 1 რიცხვი.

# თუ ეს პირობები დააკმაყოფილა გადმოცემულმა პაროლმა - დააბრუნეთ ფუნქციის True, სხვა შემთხვევაში False.

def password_checker(password):
    has_letter = False
    has_number = False
# char.isalpha amowmebs parolshi aris tu ara nebismieri aso
# char.isdigit amowmebs parolshi aris tu ara ricxvi
    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    return len(password) > 8 and has_letter and has_number

print(password_checker("LukaLukal"))