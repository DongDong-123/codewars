def longestchildlist(arr):
    arr2 = arr[::-1]
    res = []
    for i in range(1, len(arr)):
        b = []
        for v in arr2[i-1:]:
            if len(b):
                if v < b[0]:
                    b.insert(0, v)
            else:
                b.insert(0, v)

        if len(b) > len(res):
            res = b

    return res


if __name__ == "__main__":
    a = [1,7,3,5,9,6,8,4,2,9,7,5]
    print(longestchildlist(a))