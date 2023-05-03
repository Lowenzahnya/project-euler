def sumkrat35(n):
    summa = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            summa += i
    return summa


while True:
    try:
        n = int(input('Введите максимальное число: '))
        if type(n) == int:
            print(sumkrat35(n))
            break
    except:
        print("Это не число")
