def digital_root(n):
    c = 0
    for i in str(n):
        #print("i的值是%s"%i)
        c += int(i)
    if c <= 9:
        return c
    else:
        a = digital_root(c)
        #print("c的值是%d"%a)
        return a

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))
print(digital_root(9))
