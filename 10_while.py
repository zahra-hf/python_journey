#write a program that takes an initial number n as input and show how the machine gets to 1.
#If the current number is divisible by 2, it halves it.
#If the current number is not divisible by 2, it multiplies the number by 3 and adds 1 to it.

n = int(input())

while True:
    print(n)
    
    if n == 1:
        break
    
    if n % 2 == 0:
        n //= 2
        
    else:
        n = 3 * n + 1