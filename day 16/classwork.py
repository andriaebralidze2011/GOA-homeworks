# def greet():
#     print("Hello World!")

# greet()





#1) შექმენით 4 ფუნქცია მათემატიკურ ოპერაციებზე (+, -, /, *), თითოეული ფუნქცია უნდა იღებდეს არგუმენტად ორ რიცხვს და უნდა ატარებდეს მათ შორის შესაბამის მათემატიკურ ოპერაციებს.

def sum_numbers(num1, num2):
    return num1 + num2

result = sum_numbers(10,20)

print(result)

def sum(num1, num2):
    return num1 - num2

result = sum(10,20)

print(result)

def numbers(num1, num2):
    return num1 * num2

result = numbers(10,20)

print(result)

def nums(num1, num2):
    return num1 / num2

result = nums(10,20)

print(result)
# 2) შექმენით ორი ფუნქცია, სახელებად check_even და check_odd, თითოეული ფუნქცია უნდა იღებდეს ერთ არგუმენტს, რიცხვს. პირველი ფუნქცია უნდა აბრუნებდეს True-ს იმ შემთხვევაში თუ გადაცემული რიცხვი არის ლუწი და სხვა შემთხვევაში False-ს, მეორე ფუნქცია უნდა აბრუნებდეს True-ს იმ შემთხვევაში თუ გადაცემული რიცხვი არის კენტი, სხვა შემთხვევაში უნდა აბრუნებდეს False-ს



def check_even(number):
    return number % 2 == 0

def check_odd(number):
    return number % 2 != 0

print(check_even(8))
print(check_even(7))
print(check_odd(7)) 
print(check_odd(8)) 