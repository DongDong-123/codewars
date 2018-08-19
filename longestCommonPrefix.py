class Solution:
    def longestCommonPrefix(self, strs):
        # from functools import reduce
        # from copy import deepcopy
        """
        :type strs: List[str]
        :rtype: str
        """
        self.short_str = None

        strs_long_list = list(map(self.strs_len, strs))
        if strs_long_list == []:
            return ''
        self.short_str = min(strs_long_list)
        if self.short_str == 0:
            return ''
        # print(self.short_str)
        strs_short_list = list(map(self.shortest_list, strs))
        if strs_short_list:
            # print('sss',list(strs_short_list),type(strs_short_list))
            # aa = deepcopy(strs_short_list)
            bb = list(zip(*strs_short_list))
            # print('aa', list(zip(*aa)))
            # t = list(map(lambda x: ''.join(x), list(zip(*strs_short_list))))
            cc = list(map(self.chick_str, bb))
            # print(cc)
            if cc.count(1) != 0:
                return strs[0][:cc.count(1)]
            else:
                return ''
        else:
            return ''

    def strs_len(self, s):
        return len(s)


    def shortest_list(self, s):
        if s[:self.short_str]:
            return s[:self.short_str]


    def chick_str(self, m):
        if len(set(m)) == 1:
            return len(set(m))


import collections
# str_list = ["flower","flow","flight"]
str_list = ["aca","cba"]
# str_list = ["dog","racecar","car"]
temp= Solution()
print(temp.longestCommonPrefix(str_list))