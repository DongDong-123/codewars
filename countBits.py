def count_bits(n):
    a = bin(n)
    b = a.count("1")
    return b


# def count_bit(n):  # the best way
#     return bin(n).count("1")


if __name__ == "__main__":
    d = count_bits(0)
    print(d)
    e = count_bits(9)
    print(e)
    f = count_bits(10)
    print(f)


"""
把数字转换为二进制，统计有1出现的次数
"""
