class Solution:

    def plusOne(self, digits):
        """
        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。最高位数字存放在数组的首位，
        数组中每个元素只存储一个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头。
        如：输入: [1,2,3]  输出: [1,2,4]  解释: 输入数组表示数字 123。
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(map(str, digits))
        digits = ''.join(digits)
        digits = int(digits) + 1
        digits = list(str(digits))
        digits = list(map(int, digits))

        return digits


if __name__ == "__main__":
    arry = [2, 3, 4, 5]
    res = Solution()
    print(res.plusOne(arry))
