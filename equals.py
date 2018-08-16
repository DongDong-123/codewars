# def f(n):  # 方案一，时间复杂度O(n)
#     sums = 0
#     for i in range(n+1):
#         sums += i
#
#     return sums


def f(n):  # 方案二  时间复杂度O(1)
    """
    # 求n以下（含n）的所有整数和
    :param n:
    :return: sum
    """
    sums = (n + 1) * n // 2
    return sums

if __name__ == "__main__":
    print(f(1))
    print(f(100))

# print(type(f(1)))