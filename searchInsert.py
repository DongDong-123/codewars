class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums.count(target):
            nums.append(target)
            nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    lis = [1, 3, 5, 6]
    num = 2
    res = Solution()
    res.searchInsert(lis, num)

    """
    35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    
    你可以假设数组中无重复元素。
    
    示例 1:
    
    输入: [1,3,5,6], 5
    输出: 2
    示例 2:
    
    输入: [1,3,5,6], 2
    输出: 1
    """