#1

def litres(time):
    return int(time // 2)

#2

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False

#3

def digitize(n):
    digits = []
    
    for digit in str(n):
        digits.append(int(digit))
    
    digits.reverse()
    
    return digits

#4

def square_digits(num):  
    result = ""
    for digit in str(num):
        result += str(int(digit) ** 2)
    return int(result)

#5

def disemvowel(string):
    result = ""
    
    for i in string:
        if i not in "aeiouAEIOU":
            result += i
    return result