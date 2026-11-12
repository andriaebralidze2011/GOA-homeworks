#1

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2

print(basic_op("/", 10, 5))

#2

def abbrev_name(name):
    words = name.split()
    first = words[0][0].upper()
    second = words[1][0].upper()
    return first + "." + second

#3

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False