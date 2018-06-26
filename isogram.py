def isogram(s):
    a = []
    e = []
    for i in s:
        for j in range(0,10):
            b = str(j)
            e.append(b)
            print(e)
            #print(type(b))
            #print(b)
            if i == b:
                print("____3___")
                print(j)
                return False
        
        a.append(i)
    print(a)
    print("---------")
    if len(a) == len(set(a)):
        return True
    else:
        return False


a = "Dermatoglyphics"
print(isogram(a))
a = "aba" 
print(isogram(a))
a = "moOse"
print(isogram(a))
