class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, 0

        sum = 0
        m = 1
        n = 0
        # for i in range(len(height)):
        while True:
            if height[m-1] > 0:
                start = height[m-1]  # 起点
                n = m
                mid = 0
                while True:

                    if height[n] < start:
                        mid += height[n]
                    else:
                        break
                    n += 1
                sum += start * (n-m) - mid
                m = n
            m += 1

    print(sum)







if __name__ == "__main__":
    lis = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution()
    print(res.trap(lis))