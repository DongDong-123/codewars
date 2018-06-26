def remove_smallest(l):
    b = l[ : ]
    b.sort()
    #a = b[0]
    l.remove(b[0])
    return l



    
l1 = [1,2,3,4,5]
l2 = [5,3,2,1,4]
l3 = [2,2,1,2,1]
l4 = [2]
x = remove_smallest(l1)
y = remove_smallest(l2)
z = remove_smallest(l3)
m = remove_smallest(l4)
print(x)
print(y)
print(z)
print(m)
