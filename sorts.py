import time


def sorts():
    move_count = 0  # 统计移动次数
    circle_count = 0  # 统计循环次数
    for i in range(1, len(lists)):
        for v in range(i, len(lists)):
            circle_count += 1
            if lists[i-1] > lists[v]:
                lists[i-1], lists[v] = lists[v], lists[i-1]
                move_count += 1
    print('move_count：', move_count)  # for test
    print('circle_count：', circle_count)  # for test
    return lists


lists = [3, 4, 7, 6, 45, 23, 69, 9, 55, 21, 11, 8]
start = time.clock()
print(sorts())
end = time.clock()
print(end-start)


# run result

# move_count： 22
# circle_count： 66
# [3, 4, 6, 7, 8, 9, 11, 21, 23, 45, 55, 69]
# 7.329907847377462e-05