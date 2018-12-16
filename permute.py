import itertools
from itertools import *


def permute(nums):
    return list(itertools.permutations(nums))


# num = [1,2,3]
# print(permute(num))

itertoolss = ['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject',
              'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle',
              'dropwhile',
              'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee',
              'zip_longest']
count_ = count(10, 3)  # count 方法，进行无限生成器，惰性方法，需要 进行循环才行，2个参数，1.起始数字，2.步长
# for num in count_:
#     print(num)
# print(count_)

cycle_ = cycle('afgdfghj')  # cycle方法，无限生成器，对传入的参数（字符串）进行迭代，无限循环，
# print(cycle_)
# for num in cycle_:
#     print(num)

repeat_ = repeat(10, 3)  # 重复，2个参数，1、要重复的字符串，2、重复的次数。
# print(repeat_)
# for num in repeat_:
#     print(num)

chain_ = chain('abc', 'edf')  # 连接， 多个参数，把参数连接到一起
# print(chain_)
# for num in chain_:
#     print(num)


compress_ = compress

dropwhile_ = dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])  # 删除，直到符合条件，输出
# print(dropwhile_)
# for num in dropwhile_:
#     print(num)
a = {'a': 1, 'b': 4, 'c': 9, 'd': 5}
d1 = {'name': 'zhangsan', 'age': 20, 'country': 'China'}
d2 = {'name': 'wangwu', 'age': 19, 'country': 'USA'}
d3 = {'name': 'lisi', 'age': 22, 'country': 'JP'}
d4 = {'name': 'zhaoliu', 'age': 22, 'country': 'USA'}
d5 = {'name': 'pengqi', 'age': 22, 'country': 'USA'}
d6 = {'name': 'lijiu', 'age': 22, 'country': 'China'}
lst = [d1, d2, d3, d4, d5, d6]

d = groupby(lst, key=a.values)  # 就是将相邻的并且相同的键值划分为同一组，配合sort使用，等同于Counter，
# for num in d:
#     print(num)

c = filter(lambda x: x % 2, range(10))  # ==> 1,3,5,7,9  # 过滤，返回由真组成的列表  ，参数1，过滤的规则，参数2，可迭代对象
# for num in c:
#     print(num)
filterfalse(lambda x: x % 2, range(10))  # ==> 0,2,4,6,8  # 过滤，返回由假组成的列表

islice_ = islice('ABCDEFG', 2, None)  # 切片，参数1，可迭代对象；参数2，起始索引，可选；参数3，结束索引，None代表到尾部，
# print(list(islice_))
# for num in islice_:
#     print(num)

map_ = map(pow, [1, 2, 3], [2, 3, 4])  # ==> [1, 8, 81]
# print(list(map_))


permutations_ = permutations([3,4,5,6])
for num in permutations_:
    print(num)



