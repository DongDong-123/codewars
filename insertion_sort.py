import time


# 插入排序
def insertion_sort(data):
    move_count = 0  # 统计移动次数
    circle_count = 0  # 统计循环次数
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            circle_count += 1
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                move_count += 1
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