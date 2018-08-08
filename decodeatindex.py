import re
class Solution():
    def decodeAtIndex(self, S, K):
        def process_char(S):
            pat = re.compile(r'\d')  # 使用正则提取字符串中的数字
            res = pat.search(S)
            if res is not None:  # 如果匹配到数字（需要继续解码）
                num = res.group()
                num_index = S.index(num)  # 获取数字的索引位置
                char = S[:num_index]  # 提取要解码的字符串，赋值为char
                # print(char)
                new_char = char * int(num)  # 解码
                Ss = new_char + S[num_index+1:]  # 组装新的字符串
                # print(S)
                return process_char(Ss)  # 递归调用
                # return S
            else:  # 如果没匹配到数字(完成解码)
                # print('S','-------',S)
                return S  # 返回

        b = process_char(S)  # 调用函数，并接收解码结果
        # print('b', b)
        return b[K-1]


# # 方案二
# class Solution():
#     def decodeAtIndex(self, S, K):
#         num_list = list(filter(str.isdigit, S))  # 使用filter过滤字符串中的所有数字，以列表形式返回
#         # print(num_list)
#         s = ''
#         for i in num_list:  # 循环取出数字
#             num_index = S.index(i)  # 找出数字在字符串中的位置
#             S = S.replace(i, '', 1)  # 删除这个数字
#             i = int(i)  # 转换成整形
#             new_char = (s + S[:num_index]) * i  # 数字前的字母，乘以数字
#             s = new_char  # s保存已解码的字符串
#             S = S[num_index:]  # 去除已解码的部分，给S重新赋值，
#
        # print(s)
#         if len(s) < 2**63:
#             s = s
#         else:
#             s = s[:2**63]
#
#         return s[K-1]  # 按要求返回解码字符串中第K个字母


# S = 'leet2code3'
# K = 10
S = 'ha22'
K = 5

a = Solution()
a.decodeAtIndex(S, K)
print(a.decodeAtIndex(S, K))


"""
给定一个编码字符串s，为了找出解码字符串并将其写入磁带，从编码字符串中每次读取一个字符，并采取以下步骤，
如果所读的字符是字母，则将该字母写在磁带上，
如果所读的字符是数字（例如d),则整个当前磁带总共会被重复写d-1次，现在，对于给定的编码字符串s和索引k，查找并返回解码字符串中的
第k个字母

示例：
输入：S= 'leet2code3',k = 10
输出：'o'
解码后字符串为：'leetleetcodeleetleetcodeleetleetcode'
字符串中的第10个字母是'0'
提示：
1. 2 <= S.length <= 100
2. S只包含小写字母与数字2到9
3. S以字母开头
4. 1 <= K <= 10**9
5. 解码后的字符串保证少于2**63个字符串

思路：找到S中第1个数字的索引，切片取出数字前的字母，乘以数字，拼接后面的字符串（或定义容器暂存，后面再拼接），重新给S赋值，
重复上面的步骤，直到没有数字
"""