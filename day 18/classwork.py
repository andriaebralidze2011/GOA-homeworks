#1

def positive_sum(arr):
    total = 0
    for i in arr:
        if i > 0:
            total += i
    return total

print(positive_sum([1, -4, 7, 12]))

#2

def square_sum(numbers):
    total = 0
    
    for i in numbers:
        total += i ** 2
    return total

print(square_sum([1, 2, 2]))

#3

def get_count(sentence):
    count = 0
    
    for i in sentence:
        if i in "aeiou":
            count += 1
    return count

#4

def xo(s):
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    else:
        return False