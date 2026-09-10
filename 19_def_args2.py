#A function that takes an unlimited number of numbers as input.
#Return only even numbers as a list.
#If there are no even numbers, return an empty list [].

def pick_evens(*args):
    even_numbers = []
    
    for num in args:
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers
    
numbers = list(map(int, input().split()))
print(pick_evens(*numbers))