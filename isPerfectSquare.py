import time
# def isPerfectSquare():
#
#     n = 18446744073709551616
#     sum = 0
#     lis = []
#     for num in range(1, n+1, 2):
#         sum += num
#         lis.append(num)
#         if sum == n:
#             # return True
#             print('yes',sum)
#             break
#         elif sum > n:
#             print('no',sum)
#             break
#         # time.sleep(1)
#         # print((num+1)//2, sum, lis)
#         print('\r' + '1第{}次循环'.format((num + 1) // 2),sum, end='', flush=True)


# def isPerfectSquare():
#     n = 2147483647
#     num = 1
#     sum = 0
#     while sum <= n:
#         sum += num
#         num += 2
#         print('\r' + '2第{}次循环'.format((num + 1) // 2), end='', flush=True)
#         if n == sum:
#             print('ok', sum)
#             return True
#
#     else:
#         print('no', num)
#         return False


def isPerfectSquare():
    num = 18446744073709551616
    left = 0
    right = num
    count = 1
    while left <= right:
        middle = left + (right - left) // 2
        t = middle * middle
        if t == num:
            print('ok', num)
            break
            # return True
        elif t < num:
            left = middle + 1
        elif t > num:
            right = middle -1
        count += 1
        print('\r' + '3第{}次循环'.format(count), end='', flush=True)
    return False


# tests()
# test()
isPerfectSquare()
# for i in range(1000000):
    # time.sleep(2)
    # twoDivide(i)
