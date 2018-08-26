# def f1(x): return x*2
# def f2(x): return x+2
# def f3(x): return x**2
#
# def f4(x): return x.split()
# def f5(xs): return [x[::-1].title() for x in xs]
# def f6(xs): return "_".join(xs)
#
#
# def chained(functions):
#     def chain(input):
#         for f in functions:
#             input = f(input)
#         return input
#
#     return chain
#
#
# chained([f1, f2, f3])


# def search(sequence, number, lower=0, upper=None):
#     if upper is None:
#         upper = len(sequence) - 1
#     if lower == upper:
#         assert number == sequence[upper]
#         return upper
#     else:
#         middle = (lower + upper) // 2
#         if number > sequence[middle]:
#             return search(sequence, number, middle + 1, upper)
#         else:
#             return search(sequence, number, lower, middle)
#
#
# seq = [4, 8, 34, 67, 95, 100, 123]
# # seq.sort()
# # print(seq)
# print(search(seq, 100))

seq = [23, 56, 86, 6, 33, 4, 8, 34, 67, 95, 100, 123]
# a = seq.pop(0)
# print(a)
se = []

for i, v in enumerate(seq):
    n = 0
    for t in seq:
        if t > seq[i]:
            n += 1
    [n]
print(se)


print(se)



