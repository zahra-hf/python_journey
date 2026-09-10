#A function receives an unlimited number of numbers as input.
#Calculates the sum of these numbers and returns it.
#If no numbers are passed, it returns 0.

def sum_numbers(*args):
    total = 0
    for num in args:
        total +=  num
    return total
    
numbers = list(map(int, input().split()))
print(sum_numbers(*numbers))