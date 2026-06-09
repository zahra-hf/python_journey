#Write programs that take an integer as input and determine whether it is magical, cursed, legendary, or ordinary.
#Input: An integer n
#Output: If n is divisible by 3, print: "magical"
        #If n is divisible by 5, print: "cursed"
        #If n is divisible by both, print: "legendary"
        #Otherwise, print: "ordinary".


n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("افسانه ای")
elif n % 3 == 0:
    print("جادویی")
elif n % 5 == 0:
    print("نفرین شده")
else:
    print("معمولی")