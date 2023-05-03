def foo(s):
    # g = ''
    # for i in range(len(s)):
    #     if i % 3 != 0:
    #         g += s[i]
    # return g
    return ''.join(s[i] for i in range(len(s)) if i % 3 != 0)


print(foo('In the hole in the ground there lived a hobbit'))
print(foo('Python'))
print(foo('Hello'))
