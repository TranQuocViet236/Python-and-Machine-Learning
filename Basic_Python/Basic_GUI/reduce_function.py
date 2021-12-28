import functools


letter = ("H", "E", "L", "L", "O")
word = functools.reduce(lambda x,y: x+y,letter)
print(word)
factorial = (1,2,3,4,5,6,7,8,9,10)
result = functools.reduce(lambda x, y: x+y, factorial)
print(result)
