from collections import Counter
import profile


def fun1(arr):
    res = Counter(arr)

    tt = max(res.values())
    print(tt)
    for i, v in res.items():
        if v == tt:
            print(i)

    re = max(k for k, v in res.items() if v == tt)
    # print(re)
    return re


def fun2(arr):
    arr.sort(reverse=True)
    num = 0
    res = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            n = arr.count(arr[i])
            if n > num:
                num = n
                res = arr[i]

    # print(num)
    # print(res)
    return res


if __name__ == "__main__":
    arr = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]
    profile.run('fun1(arr)')
    profile.run('fun2(arr)')