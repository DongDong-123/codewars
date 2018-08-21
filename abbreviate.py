# coding=utf-8
def abbreviate(s):
    if len(s) < 4:  # 当s长度小于4时，不转换
        return s
    else:
        if "-" in s:  # 如果是连接词
            # a = s.split("-")
            # print(a)
            # b = []
            # for i in a:
            #     b.append(abbreviate(i))
            # return "-".join(b)
            return "-".join([abbreviate(i) for i in s.split("-")])  # 分割，遍历，递归调用自身转换，使用“-”拼接
        else:
            return s[0] + str(len(s)-2) + s[-1]  # 不是连接词，直接切片拼接转换


if __name__ == "__main__":
    print(abbreviate('sist'))  # Out: e6t-r2e
    print(abbreviate("internationalization"))  # Out: i18n
    print(abbreviate('Accessibility'))  # Out: A11y

"""
Question:
这个词i18n是internationalization开发人员社区中的常见缩写，用于代替输入整个单词并尝试正确拼写。
同样，a11y是的缩写accessibility。
编写一个函数，它接受一个字符串并将长度为4或更大的字符串中的任何和所有“单词”（见下文）转换为缩写，遵循以下规则：
“单词”是一系列字母字符。通过这个定义，任何其他字符如空格或连字符（例如“elephant-ride”）将一系列字母分成两个单词
（例如“elephant”和“ride”）。
该单词的缩写版本应该有第一个字母，然后是删除的字符数，然后是最后一个字母（例如“elephant ride”=>“e6t r2e”）。
"""