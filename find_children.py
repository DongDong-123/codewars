import time


def time_count(func):
    def _test(*args, **kw):
        start = time.clock()
        # print('s', start)
        func(*args, **kw)
        end = time.clock()
        # print('e', end)
        times = end - start
        print(times)
    return _test

# @time_count
# def find_children(dancing_brigade):
#     result = []
#     dancing_brigade = [x for x in dancing_brigade]
#     dancing_brigade.sort()
#     for words in dancing_brigade:
#         if words.isupper():
#             child_num = dancing_brigade.count(words.lower())
#             result.append(words)
#             result.append(words.lower()*child_num)
#
#     return "".join(result)

# @time_count
# def find_children(dancing_brigade):
#     result = []
#     dancing_brigade = sorted(dancing_brigade)
#     for words in dancing_brigade:
#         if words.isupper():
#             child_num = dancing_brigade.count(words.lower())
#             result.append(words)
#             result.append(words.lower()*child_num)
#
#     return "".join(result)

@time_count
def find_children(dancing_brigade):

    return ''.join(sorted(sorted(dancing_brigade), key=str.lower))
    # return ''.join(sorted(dancing_brigade, key=lambda l: (l.lower(), l)))
    # return ''.join(sorted(dancing_brigade, key=lambda c: (c.upper(), c.islower())))

print(find_children("BAaabbbaaZazbbzz"))

# # 带参数装饰器
# def use_logging(func):
#     def _deco(*args, **kwargs):
#         print("%s is running" % func.__name__)
#         func(*args, **kwargs)
#     return _deco
#
#
# @use_logging
# def bar(a, b):
#     print('i am bar:%s' % (a + b))
#
#
# @use_logging
# def foo(a, b, c):
#     print('i am bar:%s' % (a + b + c))
#
#
# # bar(1, 2)
# # foo(1, 2, 3)
#
#
#
# def timeit(func):
#     def wrapper():
#         start = time.clock()
#         print(start)
#         func()
#         end =time.clock()
#         print(end)
#         result = end - start
#         print(result)
#     return wrapper
#
#
# @timeit
# def foo():
#     print('函数执行时间')

#
# foo()
