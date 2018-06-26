def fold_to(distance):
    sum = 0.0001
    n = 0
    if distance< 0:
        return None
    while sum <= distance:
        sum = 2*sum
        n += 1
    else:
        return n

a = fold_to(0)
print(a)
a = fold_to(348000000)
print(a)