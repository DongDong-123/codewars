def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    print(data)


a = [3, 4, 2, 7, 1, 6, 9, 8, 5]
insertion_sort(a)