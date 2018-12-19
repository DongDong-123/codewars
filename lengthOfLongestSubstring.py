# class Solution():
#     resault = []
#     def lengthOfLongestSubstring(self, strs):
        # se = set()
        # num = 0
        # i_start = 0
        # for i, v in enumerate(strs):
        #     se.add(v)
        #     num += 1
        #     if len(se) != num:
        #         i_end = i
        #         b = strs[i_start:i_end]
        #         self.resault.append(len(b))
        #         # print(len(b))
        #         # print(resault)
        #
        #         self.lengthOfLongestSubstring(strs[i_end:])
        #         break
        #
        # return max(self.resault)
# -------------------------------------------------------------------------
#         max_long = 0
#         for indexs, elem in enumerate(strs):
#             double = strs.count(elem)
#             if double > 1:
#                 second = strs.index(elem, indexs+1)
#                 if second > max_long:
#         if not strs:
#             return 0
#         if len(strs)==1:
#             return 1
#         res = []
#         second = 0
#         for indexs, elem in enumerate(strs):
#             if elem in strs[second:indexs]:
#                 res.append(indexs-second)
#                 second = indexs
#             elif indexs == len(strs) -1:
#                 second
#
#
#         if not res:
#             return len(strs)
#         tt = max(res)
#         return tt
        # for indexs, elem in enumerate(strs):
        #     if elem in strs[:indexs]:
        #         copy_s = strs[:indexs]
        #         copy_s = copy_s[::-1]
        #         long = copy_s.index(elem) + 1
        #         print(long)
from collections import Counter
# def con():
#
#     s = "dddccdbba"
#     if s and s.count(s[0])==1:
#         return 0
#     s_dict = Counter(s)
#     num = len(s) + 1
#     for elem in s_dict:
#         if s_dict[elem] == 1:
#             elem_index = s.index(elem)
#             if elem_index <= num:
#                 num = elem_index
#                 if num == 0:
#                     break
#     if num < len(s) + 1:
#         return num
#     else:
#         return -1


# print(con())

# def con():
#     s1 = ' '
#     s2 = ' '
#     elem1 = Counter(s1)
#     elem2 = Counter(s2)
#     if elem1 == elem2:
#         print('lo')
#         return True
#     else:
#         print('er')
#         return False
import re
# def con():
#     s = 'A man, a plan, a canal: Panama'
#     s = s.lower()
#     res = re.sub(r'[^0-9a-z]','',s)
#     print(res,type(res))
#     if res == res[::-1]:
#         return True
#     else:
#         return False

import profile

# def con():
#     st = "2147483648"
    # st = st.strip()
    # 
    # # print(st)
    # # patt = re.compile(r'\+\-\d+')
    # res = re.match(r'(\+?|\-?)\d+',st)
    # if res:
    #     num = int(res.group())
    #     if num >= 2**31:
    #         return 2**31 -1
    #     elif num < -2**31:
    #         return -2**31
    #     else:
    #         return num
    # else:
    #     print(1)
    #     return 0
# def myAtoi():
#     """
#     :type str: str
#     :rtype: int
#     """
#     import re
#     str = "+2147483648"
#     str = str.strip()
#     # pat = re.compile(r'[\-+]?\d+')
#     res = re.match(r'[\-+]?\d+',str)
#     if res is not None:
#         print(res.group())
#         resault = int(res.group())
#     else:
#         return 0
#     if resault < -2 ** 31:
#         resault = -2 ** 31
#     elif resault > 2 ** 31 - 1:
#         resault = 2 ** 31 - 1
#     return resault
#
#
# # profile.run('con()')
# profile.run('myAtoi()')
# print(myAtoi())
# print(con())


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    re = ''
    if n > 1:
        n -= 1
        re += countAndSay(n)

    else:
        m = str(n)
        number = len(m)
        elem = m
        # for aa in m:

        return number+m
dock = ''
def process(m):
    long = len(m)
    count = 0

    pat = m[0]
    strs = ''
    for i in range(long):
        if m[i] == pat:
            count += 1
            strs = m[i]
            # dock.append(str(count) + strs)
            global dock
            dock = str(count) + strs
        else:
            process(m[i])

    # result = ''.join(dock)
    return dock

print(process('21'))


# n = 3
# countAndSay(n)
# class Solution:
#     """
#
#     """
#     def firstUniqChar():
#         for elem in s:
#             if s.count(elem) == 1:
#                 return s.index(elem)
#
#         return -1



#
# if __name__ == "__main__":
#     test_data = "bbbbbbbb"
    # test_data = "aab"
    # test_data = "abcabcbb"

    # test_data = "abcabagkalajghjhgjdahahuhuahjabvddahjdkdjdjaddgddadsaqwertyuijhgfdsazxcvbcbb"
    # obs = Solution()

    # print(obs.lengthOfLongestSubstring(test_data))

"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""

"""思路：定义一个函数，设置一个形参接收参数，利用集合去重的原理，遍历字符串，添加进集合中，定义一个计数变量num，
集合的长度和num相同，当不相同时，则出现重复，定义开始遍历字符串位置的索引，定义重复位置索引，取出不重复的字符串，
把长度添加进列表，然后递归调用函数，参数为字符串剩下的部分，最后返回列表中的最大值"""