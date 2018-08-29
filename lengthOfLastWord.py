class Solution:
    def lengthOfLastWord(self, s):
        """
        给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
        如果不存在最后一个单词，请返回 0 .
        说明：一个单词是指由字母组成，但不包含任何空格的字符串。
        :type s: str
        :rtype: int
        """
        res = s.strip().split(' ')
        if any(res):
            return len(res[-1])
        else:
            return 0


if __name__ == '__main__':
    s = 'ajgakj  kajga  gkajg  lakjgk   '
    temp = Solution()
    print(temp.lengthOfLastWord(s))
