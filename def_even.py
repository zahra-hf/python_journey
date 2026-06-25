def is_even(n):
            return (n % 2 == 0)
        
def any_even_in_list(nums):
    has_even = False
    for n in nums:
        if is_even(n):
            has_even = True
    return has_even

numbers = [1, 2, 3, 4]
print(any_even_in_list(numbers))