def friend(x):
    b = []
    for i in x:
        if len(i) == 4:
            b.append(i)

    return b


a = friend(["Ryan", "Kieran", "Mark",])
print(a)

#别人的方法，
# def friend(x):
#     return [f for f in x if len(f) == 4]
#
# a = friend(["Ryan", "Kieran", "Mark",])
# print(a)
