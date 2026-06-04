#write a program: If the number is odd, it doubles its value and subtracts 1 unit and If the number is even, it halves its value.

n = int(input())
x = int(input())

for _ in range(n):
    if x % 2 == 1:
        x = x * 2 - 1
    else:
        x = x // 2
        
print(x)