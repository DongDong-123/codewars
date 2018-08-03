class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            b = str(x)[1:]
            c = list(map(str, b))
            c.reverse()
            d = int('-' + ''.join(c))
        elif x == 0:
            d = 0
        else:
            b = str(x)
            c = list(map(str, b))
            c.reverse()
            d = int("".join(c))

        if d < -2 ** 31 or d > 2 ** 31 - 1:
            return 0
        else:
            return d


test = Solution()
x = -123
# x=2340
# x = 2147483647
print(test.reverse(x))

"""
7.反转整数
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
    输入: 123
    输出: 321
示例 2:
    输入: -123
    输出: -321
示例 3:
    输入: 120
    输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""