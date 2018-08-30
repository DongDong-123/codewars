class Solution:
    def isPalindrome(self, s):
        """
        给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
        说明：本题中，我们将空字符串定义为有效的回文串
        示例 1: 输入: "A man, a plan, a canal: Panama"， 输出: true
        :type s: str
        :rtype: bool
        """
        import re
        pat = re.compile(r'[\W_]')
        res = pat.sub('', s)
        res = res.lower()
        # print(res)
        if res == res[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    # a = 'kagjkj agjalga rT45RSJFKSJF6algj4567akg__ggkj_'
    a = "A man, a plan, a canal: Panama"
    res = Solution()
    print(res.isPalindrome(a))