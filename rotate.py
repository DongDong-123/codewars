class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # -----------------------
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)

        # ----------------------
        # for i in range(k):
        #     num = nums[:-1]
        #     num.insert(0, nums[-1])
        #     nums = num
        # -------------------
        for i in range(k):
            num = nums[-1]
            nums.reverse()
            nums.remove(num)
            nums.reverse()
            nums.insert(0, num)



        return nums


if __name__ == "__main__":
    # nums = [-1, -100, 3, 99]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = Solution()
    print(res.rotate(nums, k))
    """
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    输入: [1,2,3,4,5,6,7] 和 k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]
    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    要求使用空间复杂度为 O(1) 的原地算法。
    """