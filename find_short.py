import profile
# from memory_profiler import profile


# @profile  # memory_profiler测试
def find_short(strs):
    """
    查找最短的单词
    :param s: 字符串格式的一段话
    :return: 最短的单词长度
    """
    # s = "bitcoin take over the world maybe who knows perhaps"
    list_a = strs.split()
    list_temp = []
    for i in list_a:
        len_i = len(i)
        list_temp.append(len_i)

    list_temp.sort()
    return list_temp[0]


if __name__ == "__main__":
    temp = "bitcoin take over the world maybe who knows perhaps"
    result = find_short(temp)
    print(result)
    profile.run("find_short(temp)")

    # import doctest, find_short
    # doctest.testmod(find_short)
    # y = find_short("turns out random test cases are easier than writing out basic ones")
    # z = find_short("lets talk about javascript the best language")
    # m = find_short("i want to travel the world writing code one day")
    # n = find_short("Lets all go on holiday somewhere very cold")
    # print(y, z, m, n)
