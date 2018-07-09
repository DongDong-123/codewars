def sum_dig_pow(a, b):  # 方法一
    """
    找出所有满足该条件（如：135=1**1+3**2+5**3；89=8**1+9**2）的数字，并且当数字为个为时，直接输出
    :param a: 开始数字
    :param b: 结束数字
    :return:返回满足条件数字组成的列表
    """
    list_r = []
    if b <= 10:
        return [i for i in range(a, b)]
    elif a >= 10:
        for i in range(a, b+1):
            lens = len(str(i))
            list_s = []
            for t in range(lens):
                list_s.append(int(str(i)[t])**(t+1))
            if sum(list_s) == i:
                list_r.append(i)
    elif a < 10:
        for i in range(a, 10):
            list_r.append(i)
        for i in range(10, b+1):
            lens = len(str(i))
            list_s = []
            for t in range(lens):
                list_s.append(int(str(i)[t])**(t+1))
            if sum(list_s) == i:
                list_r.append(i)

    return list_r


# 使用列表生成式优化
# def sum_dig_pow(a, b):
#     list_r = []
#     if b <= 10:
#         return [i for i in range(a, b)]
#     elif a >= 10:
#         for i in range(a, b+1):
#             lens = len(str(i))
#             list_s = [int(str(i)[t])**(t+1) for t in range(lens)]
#             if sum(list_s) == i:
#                 list_r.append(i)
#     elif a < 10:
#         for i in range(a, 10):
#             list_r.append(i)
#         for i in range(10, b+1):
#             lens = len(str(i))
#             list_s = [int(str(i)[t]) ** (t + 1) for t in range(lens)]
#             if sum(list_s) == i:
#                 list_r.append(i)
#     return list_r


# 测试数据
print(sum_dig_pow(10, 89))  # 应输出结果[89]
# sum_dig_pow(1, 10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_dig_pow(1, 100)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# sum_dig_pow(10, 100)  # [89]
# sum_dig_pow(90, 100)  # []
# sum_dig_pow(89, 135)  # [89, 135]

# 要求：给定a，b，两个参数，a和b之间的数字，满足下面条件时，所有满足条件的数字以列表形式返回
# 1，当数字为各位时，
# 2，当数字的每一个数，以它的位置为指数的和，等于该数字时，如：135=1**1+3**2+5**3；89=8**1+9**2

# 思路：1：若b小于10，则a也小于10，返回a到b的列表，
#      2：若a大于等于10，则b大于10，遍历ab之间的所有数据，输出满足条件的数字，添加到列表里
#       3：若a小于10，b大于10，取a到10之间的数字加入列表，遍历10到b之间的所有数据，输出满足条件的数字，添加到列表里，