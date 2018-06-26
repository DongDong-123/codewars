def remove_smallest(numbers):
    if numbers == False:
        return []
    else:
        x = numbers[:]
        x.sort()
        y = x[0]
        numbers.remove(y)
        return numbers


numbers = [1, 2, 3, 4, 5]
a = remove_smallest(numbers)
print(a)
    
