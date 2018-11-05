class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for n in range(len(prices) - 1):
            if prices[n + 1] > prices[n]:
                profit += prices[n + 1] - prices[n]
        return profit


if __name__ == "__main__":
    arry = [7, 6, 4, 3, 1]
    # arry = [1,2,3,4,5]
    # arry = [7, 1, 5, 7, 3, 6, 4]
    res = Solution()
    print(res.maxProfit(arry))
    """
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    """
