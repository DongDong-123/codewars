# import math
# def quadratic(a,b,c):
#     # (x + (b/2a))**2 =
#     x1 = math.sqrt(-c/a + (b/(2*a))**2) - b/(2*a)
#     x2 = -math.sqrt(-c/a + (b/(2*a))**2) - b/(2*a)
#     if x1 == x2:
#         return x1
#     else:
#         return (x1, x2)
#     # print(x1,x2)
#
#
#
# quadratic(1,3,-4)
# print(quadratic(2,3,1))
# print(quadratic(1,2,1))

# def product(x, *number):
#     res = x
#     for i in number:
#         res *= i
#     return res
#
#
# print(product(5))
#
# def triangles():
#     p = [1]
#     while True:
#         yield p
#         p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# from functools import reduce
# def fn(x, y):
#     return x *10 + y
# # a = reduce(fn, [1,3,5,6,8])
# # print(a)
#
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
# b = reduce(fn, map(char2num, '13579'))
# print(b)

# x = 5
# y = 4
# if not 2+2==y or x==5 and 10==9:
#     print("yes")
# elif x > y:
#     print('no')

# def peach(x):
#     aa = ((x-1)%5)
#     if aa == 0:
#         aa = aa*4
#         for i in range(5):
#             bb = peach(aa)
#             print(bb)
#
#
#     # if type(bb) is int:
#     #     return bb
#
#
# for i in range(1,100000,5):
#     peach(i)
# #
# def norma(name):
#     name.lower()
#     print(name.lower().capitalize())

# norma('LoewE')
#
from functools import reduce
# def char3(s):
#     a = s.split(".")
#     b = list(map(int, a))
#     c = b[1] / 10**len(a[1])
#     return b[0] + c
#
#
#
# print(char3('123.456'))
# s = '123.456'
#
#
# def fn(x,y):
#     return int(x) + int(y) / 10 ** len(y)
#
# print(reduce(fn, s.split(".")))

# def aisi():
#     list_re = [2,3]
#     for i in range(3,1000,2):
#         if i % 3 != 0:
#             list_re.append(i)


# 用filter求素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
#
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 回文
# def is_palindrome(n):
#     temp = list(map(str, str(n)))
#     # print(temp)
#     sign = 0
#     for i in range(len(temp)//2):
#         if temp[i] == temp[-i-1]:
#             sign += 1
#
#     if sign == len(temp) // 2:
#         a = "".join(temp)
#         return int(a)
#
# def palindrome(n):
#     if str(n) == str(n)[::-1]:
#         return n
# for i in range(10000):
#     if is_palindrome(i):
#         # print(is_palindrome(i))
#         print(palindrome(i))

# 求素数 埃氏筛法
# def prime_circle():
#     n = 1
#     while n < 1000:
#         n = n + 2
#         yield n
#
#
# def prime_body():
#     res_list = [2]
#     tt = prime_circle()
#     while res_list[-1] < 1000:
#         a = 0
#         n = next(tt)
#         for i in res_list:
#             if n % i != 0:
#                 a += 1
#
#         if a == len(res_list):
#             res_list.append(n)
#             print(n)
#
#
# prime_body()
# def outer(some_func):
#     def inner():
#         print("before some_func")
#         ret = some_func()  # 1
#         return ret + 1
#
#     return inner
#
#
# def foo():
#     return 1
#
#
# decorated = outer(foo)  # 2
# # print(decorated)
# print(decorated())


# [1, 3, 5, 7, 9, 11, 13, 4, 8, 12, 6, 2, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#
# card_list = [1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10, 7]
# card_list = [1, 3, 5, 7, 9, 11, 13, 4, 8, 12, 6, 2, 10]

#
# def turn_card(card_list):
#     res = card_list[:]
#     temp = []
#
#     while len(card_list):
#         temp.append(card_list.pop(0))
#         if len(card_list) != 0:
#             card_list.append((card_list.pop(0)))
#
#     for i, v in enumerate(temp):
#         if i+1 != v:
#             res[v-1] = i+1
#
#     return res
#
#
# if __name__ == "__main__":
#     card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
#     print(turn_card(card_list))


# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         self.short_str = None
#
#         strs_long_list = list(map(self.strs_len, strs))
#         self.short_str = min(strs_long_list)
#         strs_short_list = list(map(self.shortest_list, strs))
#         if strs_short_list:
#             bb = list(zip(*strs_short_list))
#             cc = list(map(self.chick_str, bb))
#             return strs[0][:cc.count(1)]
#         else:
#             return ''
#     def strs_len(self, s):
#             return len(s)
#
#     def shortest_list(self, s):
#         if s[:self.short_str]:
#             return s[:self.short_str]
#
#     def chick_str(self, m):
#         if len(set(m)) == 1:
#             return len(set(m))


def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)
