def count_num(array):
    # 方法一
    # dicts = dict()
    # for i in array:
    #     dicts[i] = array.count(i)
    #
    # return dicts

    # 方法二
    # from collections import Counter
    # return Counter(array)

    # 方法三
    return {i:array.count(i) for i in array}



lists = ['a', 'a', 'b', 'b', 'b']
res = count_num(lists)
print(res)