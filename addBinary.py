class Solution:
    def addBinary(self, a, b):
        """
        给定两个二进制字符串，返回他们的和（用二进制表示）。
        输入为非空字符串且只包含数字 1 和 0。
        :type a: str
        :type b: str
        :rtype: str
        """
        res = bin(int(a, base=2) + int(b, base=2))
        return res[2:]


if __name__ == "__main__":
    a = '10101'
    b = '100010'
    res = Solution()
    print(res.addBinary(a, b))
