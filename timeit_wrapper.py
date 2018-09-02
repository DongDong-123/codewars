import time


def timeit(func):
    """
    计时装饰器
    :param func:
    :return:
    """
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print('used:', end - start)

    return wrapper
