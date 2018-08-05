import time


# 方案一： 循环
def shiftingLetters(S, shifts):
    list_s = []
    for i in range(len(S)):
        s_num = ord(S[i])
        # print(s_num)
        num2 = sum(shifts[i:]) % 26
        # print(num2)
        num3 = s_num + num2
        if num3 > 122:
            num3 = num3 - 26
        s_end = chr(num3)
        # print(s_end)
        list_s.append(s_end)

    aa = ''.join(list_s)
    print(aa)


# 方案二：递归；缺点：最大递归深度996（实测），不能满足要求（测试数据长度20000）
import re


# def shiftingLetters(S, shifts):
#     pat = re.compile(r'[a-z]')
#     res = pat.findall(S)
#     # print(res, type(res))
#
#     count = 0
#     list_s = []
#     def circle(lists, count):
#         if len(lists) != 0:
#             aa = lists.pop(0)
#             # print(aa)
#             s_num = ord(aa)
#             num2 = sum(shifts[count:]) % 26
#             num3 = s_num + num2
#             if num3 > 122:
#                 num3 = num3 - 26
#             s_end = chr(num3)
#             # print(s_end)
#             list_s.append(s_end)
#             count += 1
#             return circle(lists, count)
#         else:
#             pass
#
#     circle(res, count)
#     # print(char)
#     bb = ''.join(list_s)
#     print(bb)

S = 'ruu'
shifts = [26, 9, 17]

start = time.clock()
shiftingLetters(S, shifts)
end = time.clock()
print('use time:', end-start)
"""
示例：
输入：S = "abc", shifts = [3,5,9]
输出："rpl"
解释： 
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。
"""
