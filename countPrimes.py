class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <= 2:
            return 0

        # tt = [2]
        num = 1
        for i in range(3, n, 2):
            for j in range(3, int(math.sqrt(i))+1, 2):
                if i % j == 0:
                    break
            else:
                num += 1
                # tt.append(i)
        # print(num, tt, len(tt))
        print(num)

res = Solution()
res.countPrimes(999983)