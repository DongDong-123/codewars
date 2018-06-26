b = []
def longest(s1,s2):
    d = s1 + s2 
    for i in d:
        b.append(i)
    c = set(b)
    a= list(c)
    a.sort()
    return a
m = "dsalskdfjalfkjaigjahgajff"
n = "ajaoigjoagjkaljdajdkajdl"
x = longest(m,n)
print(x)


def longest(s1,s2):
    d = s1 + s2
    for i in d:
        a = i 
