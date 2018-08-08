count = 0
def move(n, a, b, c):
    global count
    count += 1
    if n == 1:
        print(a, '->', c)
    else:
        move(n-1, a, c, b)
        print(a, '->', c)
        move(n-1, b, a, c)

    print(count)
move(3, 'A', 'B', 'C')