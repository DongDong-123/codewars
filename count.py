def count_num(array):
    """
    统计给定列表中元素的数量
    :param array: 指定的列表
    :return: 返回一个字典，键为列表中的元素，值为改元素的数量
    """
    # 方法一
    # dicts = dict()
    # for i in array:
    #     dicts[i] = array.count(i)  # 直接创建键值对
    #
    # return dicts

    # 方法二
    # from collections import Counter  # 使用collections模块中的Counter方法
    # return Counter(array)  # 直接返回结果

    # 方法三
    return {i: array.count(i) for i in array}  # 使用生成器，原理等同于方法一


lists = ['a', 'a', 'b', 'b', 'b']
res = count_num(lists)
print(res)
