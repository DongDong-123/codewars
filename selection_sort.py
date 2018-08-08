# 选择排序
def selection_sort(list):
    n = len(list)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if list[min_index] > list[j]:
                min_index = j  # 保持min_index指向的数字始终是最小的

        if i != min_index:  # 如果i=min_index,则表示位置正确，不需要交换
            list[min_index], list[i] = list[i], list[min_index]
    return list


li = [1, 35, 3, 66, 33, 22, 98, 73]
print(selection_sort(li))

"""
使用循环嵌套，使列表中的每一个数都和剩余所有的数进行比较，如果大于，则后续使用较小的数字和后面的数字继续比较，完成一次内循环，
找到当前列表中最小的数字，和外循环中的数字交换，然后，外循环指针向后移动，从后面找新的最小数字，换位，直到完成排序
"""