def o_ji_li_de(m, n):
    """
    m,n都是正整数且m>n
    :param m:
    :param n:
    :return: 两个数的最大公约数
    """
    r = m % n
    if r != 0:
        m = n
        n = r
        o_ji_li_de(m, n)
    else:
        print(n)


o_ji_li_de(15, 5)

"""
欧几里得算法，求两个数的最大公约数
"""