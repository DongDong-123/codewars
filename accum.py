def accum(s):
    word_list = []
    for i, e in enumerate(s):
        #word_list.append(e.upper() + e.lower() * i)
        word_list.append((e * (i + 1)).title())

    return '-'.join(word_list)



aa = 'abkdg'
res = accum(aa)
print(res)
