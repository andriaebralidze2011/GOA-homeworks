# 2) შეიყვანეთ ნებისმიერი მთელი დადებითი რიცხვი. თქვენი დავალებაა, პროგრამის საშუალებით დაითვალოთ ამ რიცხვის ციფრების რაოდენობა, ციფრების ჯამი და რამდენი ლუწი და კენტი ციფრია მასში. საბოლოოდ გამოიტანეთ შედეგები და დამატებით განსაზღვრეთ, ციფრების ჯამი ლუწია თუ კენტი.

n = int(input("please enter number: "))

count = 0
total = 0
even = 0
odd = 0

while n > 0:
    digit = n % 10

    count += 1
    total += digit

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print("Number of digits:", count)
print("Sum of digits:", total)
print("Even digits:", even)
print("Odd digits:", odd)

if total % 2 == 0:
    print("The sum of digits is even.")
else:
    print("The sum of digits is odd.")

# 3) მომხმარებელს შემოაყვანინეთ 15 სხვადასხვა რიცხვი. პროგრამამ უნდა იპოვოს მათ შორის ყველაზე დიდი და ყველაზე პატარა რიცხვი, დაითვალოს დადებითი, უარყოფითი და ნულის ტოლი რიცხვების რაოდენობა. ასევე გამოთვალოს ყველა შეყვანილი რიცხვის საშუალო არითმეტიკული და დაადგინოს, საშუალო დადებითია, უარყოფითი თუ ნულის ტოლი.

numbers = []
positive_nums = 0
negative_nums = 0
zero = 0
for i in range(15):
    num = int(input("Enter number: "))

    while num in numbers:
        num = int(input("Enter a different number: "))

    numbers.append(num)

print("max numbers", max(numbers))
print("min numbers", min(numbers))

for num in numbers:
    if num > 0:
        positive_nums += 1
    elif num < 0:
        negative_nums += 1
    else:
        zero += 1

print("positive nums are", positive_nums)
print("negative nums are", negative_nums)
print("nums that equal zero are", zero)

average = sum(numbers) / 15

print("average is:", average)

if average > 0:
    print("The average is positive.")
elif average < 0:
    print("The average is negative.")
else:
    print("The average is zero.")

# 4) პროგრამაში წინასწარ განსაზღვრეთ ერთი საიდუმლო რიცხვი, მაგალითად 37. მომხმარებელს მიეცით 7 მცდელობა მის გამოსაცნობად. ყოველი მცდელობის შემდეგ პროგრამამ უნდა შეამოწმოს შეყვანილი რიცხვი და მომხმარებელს აცნობოს, საიდუმლო რიცხვი უფრო დიდია თუ უფრო პატარა. თუ მომხმარებელი სწორად გამოიცნობს, პროგრამამ უნდა შეწყვიტოს ციკლი და გამოიტანოს წარმატების შეტყობინება. თუ 7 მცდელობა ამოიწურა, გამოიტანოს შეტყობინება, რომ თამაში დასრულდა და აჩვენოს სწორი პასუხი.

secret_number = 37

for i in range(7):
    guess = int(input("please enter your guess: "))
    if guess == secret_number:
        print("you got it! congretulations")
        break
    elif guess < secret_number:
        print("secret number is higher")
    else:
        print("secret number is lower")
     
print("you didn't get it")
print("the correct number was", secret_number)

# 5) შეიყვანეთ საწყისი და საბოლოო რიცხვები. პროგრამამ უნდა გაიაროს ამ დიაპაზონში არსებული ყველა მთელი რიცხვი და თითოეული მათგანი შეამოწმოს. თუ რიცხვი იყოფა 3-ზე და 5-ზე ერთდროულად, გამოიტანოს „FizzBuzz“; თუ მხოლოდ 3-ზე იყოფა — „Fizz“; თუ მხოლოდ 5-ზე იყოფა — „Buzz“; სხვა შემთხვევაში გამოიტანოს თავად რიცხვი. დამატებით დაითვალეთ, რამდენი Fizz, Buzz და FizzBuzz შეგხვდათ მოცემულ დიაპაზონში.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(start, end + 1):
    if i % 3 and i % 5:
        print("FizzBuzz")
        fizzbuzz += 1
    elif i % 3:
        print("Fizz")
        fizz += 1
    elif i % 5:
        print("Buzz")
        buzz += 1 
    else:
        print(i)

print("fizzbuzz count = ", fizzbuzz)
print("fizz count = ", fizz)
print("buzz count = ", buzz)