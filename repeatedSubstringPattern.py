class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_long = len(s)
        num = 1
        while num <= s_long // num:
            if num * (s_long // num) == s_long:
                if s[:num] * (s_long // num) == s and s_long // num > 1 or s[:s_long // num] * num == s and num > 1:
                    print('ok')
                    return True
            num += 1
        else:
            print('no')
            return False


if __name__ == "__main__":
    res = Solution()
    s = 'abab'
    res.repeatedSubstringPattern(s)
