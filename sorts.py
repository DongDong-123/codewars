lists = [3, 4, 7, 6, 45, 23, 69, 9, 55, 21, 11, 8]


def sorts():
    for i in range(1, len(lists)):
        for v in range(i, len(lists)):
            if lists[i] > lists[v]:
                lists[i], lists[v] = lists[v], lists[i]
    return lists


print(sorts())
