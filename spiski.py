# Поиск в строке символов(в данном примере цифр) и добавление в отдельный список
s = 'ab12c59p7dq'
digits = []
for i in s:
    if '1230456789'.find(int(i)) != -1:
        digits.append(i)
print(digits)

# Все элементы с четными индексами
s = [int(s) for s in input('S').split()]
k = [s[i] for i in range(0, len(s), 2)]
print(k)

# Четные элементы списка
s = [int(s) for s in input('S').split() if int(s) % 2 == 0]
print(s)

# Больше предыдущего
s = [int(s) for s in input('S').split()]
k = [s[i] for i in range(len(s)) if s[i] > s[i-1]]
print(k)

# Соседи одного знака
s = [int(s) for s in input('S').split()]
for i in range(1, len(s)):
    if (s[i] > 0 and s[i-1] > 0) or (s[i] < 0 and s[i-1] < 0):
        print(s[i-1], s[i])
        # break (По условию нужно выдать первое значение)

# Больше своих соседей
s = [int(s) for s in input('S').split()]
j = 0
for i in range(len(s)-1):
    if s[i-1] < s[i] > s[i+1]:
        j += 1
print(j)

# Перестановка соседних элементов
s = [int(s) for s in input('S').split()]
for i in range(1, len(s), 2):
    s[i], s[i-1] = s[i-1], s[i]
print(s)

# Перестановка мин и макс значений
s = [int(s) for s in input('S').split()]
print(s)
s_min_index = s.index(min(s))
s_max_index = s.index(max(s))
s[s_min_index], s[s_max_index] = s[s_max_index], s[s_min_index]
print(*s)  # =print(' '.join(map(str, s)))

# Вставка элемента по индексу
s = [int(s) for s in input('S').split()]
# s.insert(int(input('Index')), int(input('Digit'))) - Решение в одну строку
k = int(input('Digit'))
i = int(input('Index'))
s.append(0)
for j in range(len(s)-1, i, -1):
    s[j] = s[j-1]
s[i] = k
print(s)
