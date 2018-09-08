def test_func(num_list):
    '''
    求数组中最大子序列的和，子序列可以不连续
    （也可以写成if判断语句只累加整数即可）
    '''
    length = len(num_list)
    dp = [0] * length
    dp[0] = num_list[0]
    for i in range(length):
        dp[i] = max(dp[i - 1] + num_list[i], dp[i - 1])
    print(dp[-1])


def test_func2(num_list):
    '''
    求数组中最大子序列的和，子序列必须连续
    '''
    length = len(num_list)
    max_value = -10000000000
    tmp = 0
    for i in range(length):
        tmp = max(tmp + num_list[i], num_list[i])
        max_value = max(max_value, tmp)
    print(max_value)


def test_func3(num_list):
    '''
    求数组中和最大的子序列，子序列必须连续
    '''
    length = len(num_list)
    max_value = -10000000000
    tmp = 0
    begin = 0
    end = 0
    for i in range(length):
        if tmp <= tmp + num_list[i]:
            tmp = tmp + num_list[i]
            end = i
        else:
            begin = i

        # tmp = max(tmp + num_list[i], num_list[i])
        max_value = max(max_value, tmp)
    print(max_value)
    print(num_list[begin:end])




if __name__ == '__main__':
    num_list = [-4, 3, 56, -15, 34, 0, -14, 4]
    # test_func(num_list)
    # print('----------------------------------------------------')
    # test_func2(num_list)
    test_func3(num_list)
