# 1) შექმენით რიცხვების მასივი (მინიმუმ 20 რიცხვი), თქვენი დავალებაა for ციკლის დახმარებით გადაუაროთ მასივს და თითოეული რიცხვი რომელიც მდებარეობს ამ მასივში აიყვანოთ კვადრატში და შედეგე (ანუ ყველა კვადრატში აყვანილი რიცხვი) უნდა დააჯმამოთ.

nums = [7, 14, 23, 31, 42, 56, 63, 78, 85, 91,104, 117, 126, 139, 145, 158, 162, 174, 183, 199]

squared_nums = 0
for i in nums:
    squared_nums += i ** 2

print("the sum of squared nums is", squared_nums)

# 2) იმავე მასივს გადაუარეთ for ციკლის დახმარებით, თქვენი დავალებაა კენტი რიცხვები ცალკე დააჯამოთ და ლუწი რიცხვები ცალკე, საბოლოოდ გამოიტანეთ ლუწი და კენტი რიცხვების ჯამები ტერმინალში.

nums = [7, 14, 23, 31, 42, 56, 63, 78, 85, 91,104, 117, 126, 139, 145, 158, 162, 174, 183, 199]
even_sum = 0
odd_sum = 0

for i in nums:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("even numbers sum is",even_sum)
print("odd numbers sum is",odd_sum)    

# 3) შექმენით პროგრამა სადაც პირველრიგში მომხმარებელი შემოიტანს რიცვხების რაოდენობას, შემდეგ for ციკლის გამოყენებით მაგდენი რიცხვი შემოატანინეთ input და ჩასვით სიაში

# შემდეგ დაალაგეთ სიაში იპოვეთ მაქსიმალური და მინიმუალური რიცხვები (for ციკლის გამოყენებით აუცილებლად)

size = int(input("Please ender quanitity: "))

numbers = []

for i in range(size):
    num = int(input("Please enter number: "))
    numbers.append(num)

min = numbers[0]
max = numbers[0]

for num in numbers:
    if num < min: min = num
    if num > max: max = num

print(min, max)


# როგორ ვიპოვოთ მინიმალური რიცხვი მასივში

# numbers = [3, 4, 1, 10, 5]

# min_number = numbers[0]

# for num in numbers:
#     if num < min_number:
#         min_number = num

# print(min_number)


#4) მომხმარებელს შემოატანინეთ მოსწავლეების რაოდენობა (ერთი მთელი რიცხვი), შემდგომ მიეცით თითოეული მოსწავლისთვის ქულის შემოტანის შესაძლებლობა (ქულა 0-იდან 100-მდე) და თითოეული ქულა დაამატეთ მასივში, თქვენი დავალებაა, 
# რომ გამოითვალოთ მთლიანი ჯგუფის (ყველა მოსწავლის) საშუალო ქულა, იპოვოთ მაქსიმალური ქულა და ასევე მინიმალური ქულა და საბოლოოდ უნდა დაითვალოთ რამდენმა მოსწავლემ ჩააბარა გამოცდა (ქულა 60-ზე მეტია) და რამდენმა ვერ ჩააბარა (ქულა 60-ზე ნაკლებია).

num_students = int(input("Enter the number of students: "))

scores = []

for i in range(num_students):
    while True:
        score = int(input("Enter score for student"))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("Error! Score must be between 0 and 100. Try again.")

if len(scores) > 0:
    total_sum = 0
    max_score = scores[0]
    min_score = scores[0]
    passed_count = 0
    failed_count = 0

    for score in scores:
        total_sum += score
        
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
            
        if score > 60:
            passed_count += 1
        elif score < 60:
            failed_count += 1

    average_score = total_sum / len(scores)

    print("\n--- Statistical Report ---")
    print(f"All student scores: {scores}")
    print(f"Group average score: {average_score:.2f}")
    print(f"Maximum score: {max_score}")
    print(f"Minimum score: {min_score}")
    print(f"Passed (> 60): {passed_count} student(s)")
    print(f"Failed (< 60): {failed_count} student(s)")
else:
    print("The student list is empty.")