a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
b = 'aaaabbbbccccddddeeee'

def find_vowl(l):
    c = []
    for i in b:
        if i in a:
            #print(i)
            c.append(i)
            #print(c)
            d = set(c)
            len(d)
    return len(d)

print(find_vowl(b))
