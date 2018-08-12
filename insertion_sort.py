import time


# 插入排序
def insertion_sort(data):
    move_count = 0  # 统计移动次数
    circle_count = 0  # 统计循环次数  for test
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            circle_count += 1  # for test
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                move_count += 1  # for test
            else:
                break
    print(data)
    print('move_count:', move_count)
    print('circle_count:', circle_count)


a = [3, 4, 7, 6, 45, 23, 69, 9, 55, 21, 11, 8]
start = time.clock()
insertion_sort(a)
end = time.clock()
print(end-start)

"""
原理：从索引位1开始遍历列表，每一个数字，都和前面的所有数字按从后到前的顺序进行比较，小于则交换位置，大于则不变，重复，直到
完成排序
"""