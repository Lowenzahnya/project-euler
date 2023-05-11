"""
Максимальный элемент и его индекс
n = int(input('a'))
maximum = 0
i = 0
while n != 0:
    i += 1
    if n > maximum:
        maximum = n
    n = int(input('n'))
print(maximum)
print(i-1)
"""

""" 
Количество четных элементов
i = 0
n = int(input('n'))
while n != 0:
    if n % 2 == 0:
        i += 1
    n = int(input('n'))
print(i) 
"""

""" 
Количество элементов, которые больше предыдущего
n = int(input('a'))
maximum = 0
i = -1
while n != 0:
    if n > maximum:
        maximum = n
        i += 1
    else:
        maximum = n
    n = int(input('n'))
print(i) 
"""

""" 
Максимальное число идущих подряд равных элементов
n = int(input('n'))
r = 0
i = 1
while n != 0:
    if n == r:
        i += 1
    r = n
    n = int(input('N'))
print(i)
"""