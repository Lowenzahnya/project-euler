# Длина отрезка в системе координат
def lensec():
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

x1, y1, x2, y2 = [float(n) for n in input('координаты').split()]
print(lensec())

# Рекурсия обратного вывода (1 2 3 -> 3 2 1), Стек данных
def reverse():
    n = int(input('Neponyatna'))
    if n != 0:
        reverse()
    print(n)

reverse()

# Заполнение двумерного массива циферками
m = [[int(j) for j in input('j').split()] for i in range(int(input('n')))]
print(m)

# Матрица из 0 4х4
a = [[0]*4 for i in range(4)]
for row in a:
    print(' '.join([str(elem) for elem in row]))

a = [[0]*4 for i in range(4)]
for i in range(4):
    a[i][i] = 1
    for j in range(i):
        a[i][j] = 2
    for j in range(i+1, 4):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))

for row in [[j*0 for j in range(6)] for i in range(5)]:
    print(' '.join([str(elem) for elem in row]))

# Шахматная доска
n = int(input('dlina'))
m = int(input('visota'))
k = [['.']*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if (i+j) % 2 != 0:
            k[i][j] = '*'
for row in k:
    print(' '.join(row))

print(len(set(input('S').split()))) # Количество уникальных элементов
print(len(set(input('S').split()) & set(input('K').split()))) # Количество совпадений множеств
print(set(input('S').split()) - set(input('K').split()))
print(set(input('S').split() + input('K').split()))
print(*sorted(set(input('S').split()) & set(input('K').split())))
