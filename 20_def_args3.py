#A function takes a number of integers (heights of buildings) as input.
#Find and return the largest number among them.
#If no number is entered, return the value 0.

def skyline(*args):
    maximum = 0
    
    for num in args:
        if num > maximum:
            maximum = num
            
    return maximum
    
numbers = list(map(int, input().split()))
print(skyline(*numbers))