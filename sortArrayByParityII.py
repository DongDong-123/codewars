class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # i = 0
        # j = 1
        # j_list = []
        # len_a = len(A)
        # while j <= len_a:
        #     if A[j] % 2 == 0:
        #         j_list.append(j)
        #     j += 2
        #
        # while i < len_a:
        #     if A[i] % 2 != 0:
        #         t = j_list.pop()
        #         A[i], A[t] = A[t], A[i]
        #     i += 2
        # print(A)

        # i = 0
        # j = 1
        # t_list = [num for num in range(len(A))]
        # for elem in A:
        #     if elem % 2 == 0:
        #         t_list[i] = elem
        #         i += 2
        #     else:
        #         t_list[j] = elem
        #         j += 2
        #
        # print(t_list)
        # ou = [2,4,6]
        # # ou = [i for i in A if i % 2]
        # # ji = [i for i in A if not i % 2]
        # ji = [1,3,5]
        # tt = [7,8,9]
        # print(zip(ji, ou))
        # for i in zip(ji,tt,ou):
        #     print(i)
        #     for t in i:
        #         print(t)
        # return [i for n in zip(ji, ou) for i in n]
        # max_nums = max(nums)
        # max_sum = len(nums) * (len(nums) + 1) // 2
        # sum_nums = sum(nums)
        # if 0 not in nums:
        #     return 0
        # elif max_sum - sum_nums == 0:
        #     return max_nums + 1
        # else:
        #     return max_sum - sum_nums
        # print(c)
        # return A



if __name__ == "__main__":
    import profile
    res = Solution()
    # profile.run('res.sortArrayByParityII([1,2,5,6,7,4])')
    cc =res.sortArrayByParityII([1,2,5,6,7,4])
    # print(cc)

