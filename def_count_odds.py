def is_even(n):
    return n % 2 == 0

def get_odds(nums):
    odds = []
    count = 0
    
    for num in nums:
        if not is_even(num):
            odds.append(num)
            count += 1
            
    return count, odds

my_list = [1, 2, 3, 4, 5, 6]
odds_count, my_odds = get_odds(my_list)
print(odds_count, my_odds, sep = '/')