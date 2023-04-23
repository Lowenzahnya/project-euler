def fibonacci(n):  # Числа Фибоначчи в заданном диапазоне
    result = [1, 2]
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
        i = f1 + f2
        result += [i]
    return result


def sum_even(result):  # Сумма четных чисел из диапазона
    evensum = []
    for k in range(len(result)):
        if result[k] % 2 == 0:  # and result[k] < 4000000 (если по условию задачи)
            evensum.append(result[k])
    return sum(evensum)


n = int(input('Введите количество чисел: '))
print(fibonacci(n))
print(sum_even(fibonacci(n)))
kl = list(map(int, input('Введите числа через пробел').strip().split()))
print(sum_even(kl))  # Сумма произвольных чисел

""" Решение задачи простым способом:
f1 = f2 = 1
fib = 0
result = 0
while fib < 4000000:
    fib = f1 + f2
    if fib % 2 == 0:
        result += fib
    f1, f2 = f2, fib
print(result)
"""
