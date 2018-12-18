class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # if any(nums):
        #     z_num = nums.count(0)
        #     long = len(nums)
        #     for i in range(long-1, 0, -1):
        #         if nums[i] == 0:
        #             z_num -= 1
        #         else:
        #             for num in range(z_num):
        #                 z_index = nums.index(0)
        #                 nums.append(nums.pop(z_index))
        #             print(nums)
        #             break

        count = 0
        for num, elem in enumerate(nums):
            if elem != 0:
                nums[count] = elem
                count += 1
        for num in range(count, len(nums)):
            nums[num] = 0
        print(nums)


if __name__ == "__main__":
    res = Solution()
    res.moveZeroes([0,1,0,3,12,0,0,0])
    # res.moveZeroes([0,1,0,0,0,0,0,0])