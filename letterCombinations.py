import itertools

# class Solution:
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         for n in range(1, len(digits) + 1):
#             for i in itertools.combinations(digits, n):
#                 print(''.join(i))
#
#
# a = Solution()
# print(a.letterCombinations('123'))

# count()会创建一个无限的迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 
#     if n > 100:
#         break
#         

# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('A', 10)
# for n in ns:
#     print(n)

# 通过takewhile()等函数根据条件判断来截取出一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in ns:
#     print(n)

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))  # 为什么这里要用list()函数呢？

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))



for x in itertools.starmap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print(x)