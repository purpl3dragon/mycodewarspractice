#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)


def solution(number):
    #Check if number entered is negative
    if (number < 0):
        return 0
    
    list = []
    multiples = []
    
    #get a countdown list of the number you had starting with number-1 not including 0
    while (number >1):
        number = number - 1
        list.append(number)
        
    #check if number in list is multiple of 3 or 5 
    for x in list:
        if (x % 3 == 0 or x % 5 == 0):
            multiples.append(x)
            
    a = len(multiples)
    sum = 0
    
    #Add all of the multiples together and return sum
    while a > 0:
        a -= 1
        sum += multiples[a]
    return sum
            
