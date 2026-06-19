#The power function is used. Can use any assignment.

def power(n, t):
    answer = 1
    for i in range(t):
        answer *= n
        
    return answer

print(power(2, 2))