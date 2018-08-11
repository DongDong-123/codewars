# 求素数 埃氏筛法
def prime_circle():
    n = 1
    while True:
        n = n + 2
        yield n


def prime_body():
    res_list = [2]
    tt = prime_circle()
    while res_list[-1] < 1000:
        a = 0
        n = next(tt)
        for i in res_list:
            if n % i != 0:
                a += 1

        if a == len(res_list):
            res_list.append(n)
            # print(n)
    return res_list[:-1]


if __name__ == "__main__":
    print(prime_body())
