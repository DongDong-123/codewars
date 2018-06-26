def getCount(inputStr):
    #num_vowels = 0
    inputStr = inputStr.lower()
    vowels = ['a','e','i','o','u']
    b = []
    for i in inputStr:
        b.append(i)
    for j in b and vowels:
        num_vowels = inputStr.count(i)

    return num_vowels

#inputStr = "abracadabra"
a = getCount("abracadabra")
print(a)
