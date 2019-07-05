'''
   Алгоритм нахождения суммы чисел Фибоначчи, методом динамического программирования
   
   Разница между рекурсией и динамическим программированием
   https://youtu.be/aN15vtKjdP4?t=587
'''

def fibonachi(n):
    assert n >= 0
    f = [None] * (n + 1)
    f[:2] = [0, 1]
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return print(f[n])

fibonachi(1000)
        
    
    
