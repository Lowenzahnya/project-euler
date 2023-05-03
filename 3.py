def simpleDividers(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


print(simpleDividers(13195))  # [5, 7, 13, 29]
print(simpleDividers(600851475143))  # [71, 839, 1471, 6857]
print(simpleDividers(812485742653))  # [13, 43, 10663, 136309]
print(simpleDividers(734681))  # [271, 2711]
