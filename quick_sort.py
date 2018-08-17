def quick_sort(arrys, left, right):

    if left >= right:
        return arrys

    key = arrys[left]
    # 将左边第一位定位基准数，以此数将序列分为两部分
    low = left
    high = right
    while left != right:
        # 从最右边开始查（一定要从最右边开始查），查找比基准值小的数
        while left < right and arrys[right]>=key:
            right -= 1
        arrys[left] = arrys[right]
        # 从最左边开始查，查找比基准值大的数
        while left < right and arrys[left] <= key:
            left += 1
        arrys[right] = arrys[left]

    arrys[right] = key

    # 分别对两部分数据再调用quick_sort函数
    quick_sort(arrys, low, left-1)
    quick_sort(arrys, left+1, high)

    return arrys


lis = [1, 2, 5, 3, 8, 29, 3]
n = len(lis)
quick_sort(lis, 0, n-1)
# print(quick_sort(lis, 0, n-1))