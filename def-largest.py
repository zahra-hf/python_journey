def largest_numbers(nums):
    largest_numbers = nums[0]
    for n in nums:
        if largest_numbers < n:
            largest_numbers = n
    return largest_numbers

my_nums = [1, 5, 7, 11, 2]
print(largest_numbers(my_nums))