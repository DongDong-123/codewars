def sum_dig_pow(a, b):  # 方法一
    """
    找出所有满足该条件（如：135=1**1+3**2+5**3；89=8**1+9**2）的数字
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