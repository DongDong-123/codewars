def multiplier(factor):
    """
    闭包
    :param factor:
    :return:
    """
    def multiplyByFactor(number):
        nonlocal factor  # 使用nonlocal可以给外部函数变量赋值，不使用，则在函数内新建了一个局部变量
        factor = 6
        return number * factor
    print(factor)
    return multiplyByFactor


# test = multiplier(3)
# print(test(4))
# print(multiplier(4)(5))
# print(multiplier(4)('ert'))

