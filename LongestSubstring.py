a = "abcabagkalajghjhgjdahahuhuahjabvddahjdkdjdjaddgddadsaqwertyuijhgfdsazxcvbcbb"


resault = []
def LongestSubstring(strs):
    se = set()
    num = 0
    i_start = 0
    for i, v in enumerate(strs):
        se.add(v)
        num += 1
        if len(se) != num:
            i_end = i
            b = strs[i_start:i_end]
            resault.append((len(b), b))
            # print(b)
            # print(resault)
            LongestSubstring(strs[i_end:])
            break
    res = list(sorted(resault))
    return res[-1][1]


print(LongestSubstring(a))

"""
给定一个字符串，找出不含有重复字符的最长子串。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" 。

给定 "bbbbb" ，最长的子串就是 "b" 。

给定 "pwwkew" ，最长子串是 "wke" 。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""

"""思路：定义一个函数，设置一个形参接收参数，利用集合去重的原理，遍历字符串，添加进集合中，定义一个计数变量num，
集合的长度和num相同，当不相同时，则出现重复，定义开始遍历字符串位置的索引，定义重复位置索引，取出不重复的字符串，
和字符串的长度组成元组，然后递归调用函数，参数为字符串剩下的部分，最后对列表中的元组排序，取出最长的子串"""