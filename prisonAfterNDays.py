# class Solution:
#     def prisonAfterNDays(self, cells, N):
#         """
#         :type cells: List[int]
#         :type N: int
#         :rtype: List[int]
#         """

        # if N == 0:
        #     print(cells)
        #     return cells
        # N = N % 14
        # if N == 0:
        #     N = 14
        #
        # n = 0
        # while n < N:
        #     copy = cells[::]
        #     for num in range(1, 7):
        #         if (cells[num-1] and cells[num+1]) or (not cells[num-1]and not cells[num+1]):
        #             # copy[num] = (cells[num] + 1) % 2
        #             copy[num] = 1
        #         else:
        #             copy[num] = 0
        #     if cells[-1] == 1:
        #         copy[-1] = 0
        #     if cells[0] == 1:
        #         copy[0] =0
        #     n += 1
        #     cells = copy
        # print(copy)
        # # return copy
class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # tt = 0
        # lis = []
        # for num in zip(*A):
        #     print(num)
        #     lis.append(num)
        #     # if list(num) == sorted(num):
        #     #     tt += 1
        # chr()

        for str in A:
            lis = []
            for i in str:
                lis.append(ord(i))

            print(lis)
if __name__ == "__main__":
    res = Solution()
    # cells = [0, 1, 0, 1, 1, 0, 0, 1]
    # cells = [1,0,0,1,0,0,1,0]
    # N = 1000000000
    res.minDeletionSize(["babca","bbazb"])