class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for m in range(len(nums)):
            for n in range(m+1, len(nums)):
                a = -(nums[m] + nums[n])
                if a in nums[n+1:]:
                    b = [nums[m], nums[n], a]
                    b.sort()
                    if b in res:
                        pass
                    else:
                        res.append(b)


        print(res)
        return res



nums = [-1, 0, 1, 2, -1, -4]
# nums = [3,-2,1,0]
a = Solution()
a.threeSum(nums)
print(len(nums))
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
