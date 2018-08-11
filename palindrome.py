# 方案一
def is_palindrome(n):
    temp = list(map(str, str(n)))
    # print(temp)
    sign = 0
    for i in range(len(temp)//2):
        if temp[i] == temp[-i-1]:
            sign += 1

    if sign == len(temp) // 2:
        a = "".join(temp)
        return int(a)


for i in range(10000):
    if is_palindrome(i):
        print(is_palindrome(i))


# 方案二  转成字符串后，判断是否和反转前相等
def palindrome():
    for i in range(10000):
        if str(i) == str(i)[::-1]:
            print(i)
            return i