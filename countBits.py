
def count_bits(n):
    global b
    c = []
    a = bin(n)
    for i in a:
        c.append(i)
        b = c.count("1")
    return b

d = count_bits(0)
print(d)
e = count_bits(9)
print(e)
f = count_bits(10)
print(f)

# the best way


def count_bit(n):
    return bin(n).count("1")


d = count_bit(0)
print(d)
e = count_bit(9)
print(e)
f = count_bit(10)
print(f)
