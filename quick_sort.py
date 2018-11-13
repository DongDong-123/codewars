#
# def quick_sort(arrys, left, right):
#     if left >= right:
#         return arrys
#
#     key = arrys[left]
#     # 将左边第一位定位基准数，以此数将序列分为两部分
#     low = left
#     high = right
#     while left != right:
#         # 从最右边开始查（一定要从最右边开始查），查找比基准值小的数
#         while left < right and arrys[right]>=key:
#             right -= 1
#         arrys[left] = arrys[right]
#         # 从最左边开始查，查找比基准值大的数
#         while left < right and arrys[left] <= key:
#             left += 1
#         arrys[right] = arrys[left]
#
#     arrys[right] = key
#
#     # 分别对两部分数据再调用quick_sort函数
#     quick_sort(arrys, low, left-1)
#     quick_sort(arrys, left+1, high)
#
#     return arrys
#
#
# if __name__ =="__main__":
#
#     lis = [1, 2, 5, 3, 8, 29, 3]
#     n = len(lis)
#     quick_sort(lis, 0, n-1)
#     # print(quick_sort(lis, 0, n-1))


def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = int(n / 2)
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = int(gap / 2)

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)