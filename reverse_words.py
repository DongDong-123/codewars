def reverse_words(str):
    
    d = []
    for i in str.split(" "):
        b = []
        #print(i)
        for j in i:
            #print(j)
            b.append(j)
            #print(b)
        b.reverse()
        #print(b)
        c = "".join(b)
        #print(c)
        d.append(c)
        #print(d)
        e = " ".join(d)
        
    return e

x = "This is a pen"
print(reverse_words(x))


def reverse_word(str):
    return ' '.join(s[::-1] for s in str.split(' '))

y = "This is a pen"
print(reverse_word(y))
