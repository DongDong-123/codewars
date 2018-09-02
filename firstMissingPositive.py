class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 1
        while n in nums:
            n += 1
        else:
            return n


if __name__ == "__main__":
    lis = [1, 4, 5]
    res = Solution()
    res.firstMissingPositive(lis)
    """
    41. 缺失的第一个正数
    给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

    示例 1:    
    输入: [1,2,0]
    输出: 3
    示例 2:    
    输入: [3,4,-1,1]
    输出: 2
    示例 3:    
    输入: [7,8,9,11,12]
    输出: 1
    说明:    
    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。     
    """