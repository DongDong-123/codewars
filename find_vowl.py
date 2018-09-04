def find_vowl(l):
    """
    查找不重复元音的数量（区分大小写）
    :param l: str
    :return: 元音的数量
    """
    a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    c = []
    for i in b:
        if i in a:
            c.append(i)
    return len(set(c))


if __name__ == "__main__":
    b = 'aaaabbbUbccccddAddeeee'
    print(find_vowl(b))
