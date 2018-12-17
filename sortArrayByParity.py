class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # A1 = [num for num in A if num % 2]
        # A1.extend([num for num in A if num % 2])
        # # print(A1)
        # return A1



if __name__ == "__main__":
    res = Solution()
    tt = res.sortArrayByParity([3,1,2,4])
    print(tt)
