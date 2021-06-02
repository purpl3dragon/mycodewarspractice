def solution(number):
    list = []
    multiples = []
    while (number > 1):
        number = number - 1
        list.append(number)
    for x in list:
        if (x % 3 == 0):
            multiples.append(x)
        if (x % 5 == 0):
            multiples.append(x)
    a = len(multiples)
    print(multiples)
    total = 0
    while a > 0:
        a -= 1
        total += multiples[a]
    return total
