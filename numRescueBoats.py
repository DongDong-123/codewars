# 方案一，递归，缺点：最大递归深度限制
# class Solution:
#     def numRescueBoats(self, people, limit):
#         """
#         :type people: List[int]
#         :type limit: int
#         :rtype: int
#         """
#         one_boat = people.count(limit)
#         if one_boat != 0:
#             for i in range(one_boat):
#                 people.remove(limit)
#         people.sort()
#         def auto_count(boat_sum):
#             if len(people) > 1:
#                 weight = people[0] + people[-1]
#                 if weight > limit:
#                     people.pop(-1)
#                     boat_sum += 1
#                     boat_sum = auto_count(boat_sum)
#                 else:
#                     people.pop()
#                     people.pop(0)
#                     boat_sum += 1
#                     boat_sum = auto_count(boat_sum)
#             else:
#                 boat_sum += len(people)
#                 return boat_sum
#             return boat_sum
#         boat_sum = auto_count(0)
#         print(boat_sum + one_boat)
#         return boat_sum + one_boat


from collections import deque
import time


# 方案二 迭代循环，使用双向队列，降低删除头尾元素是的时间复杂度
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boat_num = people.count(limit)  # 定义救生艇数量，统计最大载重人数，赋值
        if boat_num != 0:
            for i in range(boat_num):  # 删除所有最大的载重人数
                people.remove(limit)
        people.sort()  # 按升序排序
        people = deque(people)  # 将列表转换为双向队列
        # print(type(people))
        length = len(people)
        for i in range(length):
            if len(people) > 1:
                weight = people[0] + people[-1]  # 最小体重加最大体重
                if weight > limit:  # 若体重大于最大载重
                    wei_num = people.count(people[-1])  # 统计最大体重的数量
                    for i in range(wei_num):  # 循环删除最大体重
                        people.pop()
                        boat_num += 1  # 每删除一个，增加一个救生艇
                else:
                    boat_num += 1
                    people.popleft()  # 删除最左侧元素（最小体重）
                    people.pop()  # 删除最右侧元素（最大体重）
            elif len(people) == 1:  # 当只剩下一个人时，救生艇加1后删除
                boat_num += 1
                people.pop()
            else:  # 没有人了，结束
                break

        # print(boat_num)
        return boat_num

# 测试数据
people = [1, 2, 3,2, 3, 3]
limit = 3

# people = [3,2,2,1]
# limit = 3

# people = [3,5,3,4]
# limit = 5

start = time.clock()
a = Solution()
# a.numRescueBoats(people, limit)
print(a.numRescueBoats(people, limit),len(people))
end = time.clock()
print(end - start)


"""
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

示例 1：
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：
输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：
1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

思路：先统计体重等于救生艇最大载重的人数a，记录后删除，排序后，迭代，如果人数大于1，定义总体重等于最小体重加最大体重，
如果大于最大载重体重，删除最大体重，救生艇数量加1，如果小于或等于最大载重体重，两个都删除，救生艇数量加1，循环；当剩余人
数等于1时，删除，救生艇数量加1，人数等于0时，中断循环，返回救生艇数量
"""