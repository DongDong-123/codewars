class Solution:
    resault = []
    def longestPalindrome(self, strs):
        """
        :type s: str
        :rtype: str
        """
        strs_list = []
        for i in range(1, len(strs)):
            aa = self.search_str(i, strs)
            if aa:
                strs_list.append((len(aa), aa))

        strs_list.sort()
        print(strs_list)
        if strs_list:
            return strs_list[-1][1]
        else:
            return ''


    def search_str(self, index, strs):
        res_str = ''
        for i in range(1,len(strs)):
            if i <= index and index + i < len(strs):
                if strs[index - i] == strs[index + i]:
                    res_str = strs[index - i:index + i + 1]
                    print('1',res_str)
                elif strs[index - i + 1] == strs[index + i]:
                    res_str = strs[index - i +1:index + i + 1]
                    print('2',res_str)
        return res_str



test = "abaabadda"
bb = Solution()
print(bb.longestPalindrome(test))