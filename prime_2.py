# 用filter求素数
def _odd_iter():  # 生成自然数列表
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):  # 判断
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


def bodys():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


if __name__ == "__main__":
    bodys()