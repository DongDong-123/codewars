def revrot(strng, sz):
    if sz <= 0 or strng is None or sz > len(strng):
        return ""
    length = len(strng)//sz
    list_a = []
    for i in range(length+1):
        blunks = strng[(i-1)*sz:sz*i]
        sum = 0
        b1=str()
        for temp in blunks:
            sum += (int(temp) ** 3)
            if sum % 2 == 0:
                b1 = blunks[::-1]
            else:
                b1 = blunks[1:] + blunks[0]
        list_a.append(b1)

    return ''.join(list_a)



# s = "733049910872815764"
# res = revrot(s, 5)
res = revrot('3345678909988767655434455', 4)



print(res)