def getCount(inputStr):
    num_vowels = 0
    vowels = ['a','e','i','o','u']
    for i in inputStr and vowels:
        print(type(i))
        num_vowels = inputStr.count(i)

    return num_vowels

#inputStr = "abracadabra"
a = getCount("abracadabra")
print(a)