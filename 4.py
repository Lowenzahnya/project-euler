def compute():  # Красивый сворованный способ
    ans = max(i * j
              for i in range(100, 1000)
              for j in range(100, 1000)
              if str(i * j) == str(i * j)[:: -1])
    return str(ans)
