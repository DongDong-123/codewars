# def min_max(lst):
#     lst.sort()
#     res = []
#     if len(lst)>=2:
#         lst1 = lst[0]
#         lst2 = lst[-1]
#         res.append(lst1)
#         res.append(lst2)
#     elif len(lst)==1:
#         lst1 = lst[0]
#         lst2 = lst[0]
#         res.append(lst1)
#         res.append(lst2)
#     return res

# 相同
# def min_max(lst):
#     lst.sort()
#     res = []
#
#     lst1 = lst[0]
#     lst2 = lst[-1]
#     res.append(lst1)
#     res.append(lst2)
#
#     return res


# 相同
# def min_max(lst):
#     lst.sort()
#     return [lst[0], lst[-1]]


list = [2, 1, 4, 5]
# list = [2334454 ,5]
min_max(list)