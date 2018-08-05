import time


# 冒泡排序
def bubble_sort():
    move_count = 0  # 统计移动次数
    circle_count = 0  # 统计循环次数
    n = len(lists)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            circle_count += 1
            if lists[i] > lists[i + 1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]
                count += 1
                move_count += 1
        if count == 0:
            break
    print('move_count:', move_count)  # for test
    print('circle_count:', circle_count)  # for test
    return lists


lists = [3, 4, 7, 6, 45, 23, 69, 9, 55, 21, 11, 8]
start = time.clock()
print(bubble_sort())
end = time.clock()
print(end-start)


# run result

# move_count: 22
# circle_count: 60
# [3, 4, 6, 7, 8, 9, 11, 21, 23, 45, 55, 69]
# 7.439309457039811e-05