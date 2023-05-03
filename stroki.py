def foo(s):
    first = s[:s.find('h')+1]
    middle = s[s.find('h')+1:s.rfind('h')]
    m_repl = middle.replace('h', 'H')
    last = s[s.rfind('h'):]
    return f'{first}{m_repl}{last}'
    # return first + m_repl + last


print(foo('hhh'))
print(foo('In the hole in the ground there lived a hobbit'))
