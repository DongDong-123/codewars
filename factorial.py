# def factorial(n):
#     """
#     求n的阶乘
#     :param n: n大于等于1
#     :return: n的阶乘
#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# 方法二
def factorial(n):
    """
    求n的阶乘
    :param n:n大于等于1
    :return: n的阶乘
    """
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factorial(6))
