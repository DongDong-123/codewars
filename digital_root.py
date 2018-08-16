# def digital_root(n):  # 时间复杂度O(n),空间复杂度O(1),
#     c = 0
#     for i in str(n):
#         #print("i的值是%s"%i)
#         c += int(i)
#     if c <= 9:
#         return c
#     else:
#         a = digital_root(c)
#         #print("c的值是%d"%a)
#         return a


# 优化方案,利用map函数拆分整数，使用递归,时间复杂度O(1),空间复杂度大于O(1)，约等于O(1)
def digital_root(n, num=1):
    digital_list = list(map(int, str(n)))
    digital = sum(digital_list)
    if digital > 9:
        num += 1
        digital = digital_root(digital, num)

    print('num', num)
    return digital

if __name__ == "__main__":
    # print(digital_root(16))  # O(1)
    # print(digital_root(942))  # O(2)
    # print(digital_root(132189))  # O(2)
    print(digital_root(493193253564758969098876543456677889987675445678898877656434567))  # O(3)
    # print(digital_root(9))
    # ----------------------------------


"""
把整数里的所有数字相加，直到变成个位数，返回
16-->7
942-->6
132189-->6
493193-->2
9-->9
"""