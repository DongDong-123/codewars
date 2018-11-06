import profile
# from memory_profiler import profile
import pychecker.checker
from collections import UserString
@profile
def find_short():
    """
    查找最短的单词
    :param s: 字符串格式的一段话
    :return: 最短的单词长度
    """
    s = "bitcoin take over the world maybe who knows perhaps"
    a = s.split()
    b = []
    for i in a:
        c = len(i)
        b.append(c)

    b.sort()
    return b[0]


if __name__ == "__main__":
    y = "bitcoin take over the world maybe who knows perhaps"
    x = find_short(y)
    print(x)
    # profile.run("find_short(y)")
    # y = find_short("turns out random test cases are easier than writing out basic ones")
    # z = find_short("lets talk about javascript the best language")
    # m = find_short("i want to travel the world writing code one day")
    # n = find_short("Lets all go on holiday somewhere very cold")
    # print(y, z, m, n)
