
def find_short(s):
    
    a=s.split()
    print(a)
    b=[]
    for i in a:
        print(i)
        c = len(i)
        print(c)
        b.append(c)
    
    print("-------")
    b.sort()
    print(b)
    return b[0]
  


y = "bitcoin take over the world maybe who knows perhaps"
x = find_short(y)
print(x)
y = find_short("turns out random test cases are easier than writing out basic ones")
z = find_short("lets talk about javascript the best language")
m = find_short("i want to travel the world writing code one day")
n= find_short("Lets all go on holiday somewhere very cold")
print(y,z,m,n)
def find_short(s):
    a = s.split()# your code here
    b = []
    for i in a:
        b.append(len(i))
        b.sort()
    return b[0]
    
x = find_short("bitcoin take over the world maybe who knows perhaps")
print(x)
