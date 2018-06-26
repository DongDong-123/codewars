def find(n):
    sum = n
    for i in range(n):
        if i % 3 ==0 or i % 5 == 0:
            sum += i
    return sum
