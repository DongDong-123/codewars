def f(n):
    sum = 0
    for i in range(n+1):
        sum += i

    return sum


print(f(1))
print(f(100))
        
print(type(f(1)))