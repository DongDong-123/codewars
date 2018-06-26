def square_digits(num):
    b = str(num)
    c = int(b[0])**2
    d = b.replace(b[0],str(c))
    e = int(d)
    return e
  
x = square_digits(9119)
print(x)
