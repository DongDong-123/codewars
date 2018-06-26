def unique_in_order(s):
    num = 0
    lis = [None]
    for i in s:
        if i != lis[num]:
            lis.append(i)
            num +=1
    lis.remove(lis[0])
    return lis

a =[None,None,1,1,2,2,3,3]
print(unique_in_order(a))
            
            
