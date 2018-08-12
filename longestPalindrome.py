class Solution:
    resault = []
    def longestPalindrome(self, strs):
        """
        :type s: str
        :rtype: str
        """
        strs_list = []
        for i in range(0, len(strs)):  # 遍历所有字母
            aa = self.search_str(i, strs)  # aa接收符合条件的字符串
            if aa:
                strs_list.append((len(aa), aa))  # 字符串长度和字符串组成元组，添加进列表

        strs_list.sort()  # 根据字符串的长度排序
        print(strs_list)
        if strs_list:  # 如果不为空，返回最长的字符串
            return strs_list[-1][1]
        elif len(strs) == 0:  # 如果为空，返回空字符串，
            return ''
        else:
            return strs[0]

    # 定义处理函数
    def search_str(self, index, strs):
        res_str = ''
        num1 = 1  # 标识符
        num2 = 1
        for i in range(1, len(strs)):
            if i <= index + 1 and index + i < len(strs):
                if strs[index - i + 1] == strs[index + i] and num1 == i:  # 本次判断必须从第一个开始（使用表示符限制）
                    res_str = strs[index - i + 1:index + i + 1]  # 判是否为baab型
                    # print('2',res_str)
                    num1 += 1
                elif i <= index and index + i < len(strs) and num2 == i:  # 从1开始
                    if strs[index - i] == strs[index + i]:  # 判断是否为bab型
                        res_str = strs[index - i:index + i + 1]
                        # print('1',res_str)
                        num2 += 1

        return res_str


if __name__ == "__main__":
    test = "abaabadda"
    # test = "bb"
    bb = Solution()
    print(bb.longestPalindrome(test))

    """
    思路：遍历字符串中所有字母（从1开始），每一个字母（索引为index)，
    1.循环（从1开始）判断index-i和index+i的值是否相等，相等则继续循环，直到不相等，得出所有“aba”型的回文字符串，
    2.循环（从1开始）判断index和index+i的值是否相等，相等则继续循环，直到不相等，得出所有“baab”型的回文字符串，
    注意：循环进入判断必须从1开始，否则会出现外层相同内层不同的情况，如“cbaac","cabc"；
    注意边界问题。
    """