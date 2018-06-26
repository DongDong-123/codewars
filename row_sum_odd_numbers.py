def row_sum_odd_numbers(n):
    # your code here
    sum = 0
    # total= 0
    # li = []
    # for i in range(1, n + 1):
    #     # print(i)
    #     sum += i
    # print(sum)
    # for m in range(1, sum*2, 2):
    #     print(m)
    #     li.append(m)
    #
    # # print(li)
    # print(len(li))
    # a = li[-n:]
    # print(a)
    # for aa in a:
    #     total += aa
    # print(total)

    for bb in range(n**2-n+1, n**2+n+1, 2):
        sum += bb
    print(sum)
row_sum_odd_numbers(41)

# begin(n) = n ** 2 - (n-1)
# num = n
# step = 2
# end = n**2 +n
# n * 2
