class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # List = []
        # if right < 10:
        #     return [num for num in range(left, right+1)]
        # else:
        #     for i in range(left, right+1):
        #         for d in str(i):
        #             if int(d) == 0 or i % int(d) != 0:
        #                 break
        #         else:
        #             List.append(i)
        #
        # return List


ss = lambda i: int(d) == 0 or i % int(d) != 0

res = Solution()
tt = res.selfDividingNumbers(1, 22)

print(tt)
