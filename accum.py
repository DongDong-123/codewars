def accum(s):
    """
    指定字符串切割后，单个部分首字母大写，后面添加索引数个该字母的小写
    :param s: 字符串
    :return: 处理拼接后的字符串
    """
    word_list = []
    for i, e in enumerate(s):
        #word_list.append(e.upper() + e.lower() * i)
        word_list.append((e * (i + 1)).title())  # 字符串乘以（索引数字加一），再首字母大写

    return '-'.join(word_list)  # 列表中的元素使用-连接


aa = 'abkdg'
res = accum(aa)
print(res)
