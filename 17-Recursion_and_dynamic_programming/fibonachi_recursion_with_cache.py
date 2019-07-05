'''
   Алгоритм находения чисел Фибоначчи - рекурсия с кэшированием 
   (динамическое программирование)
   
   теория + реализация
   https://youtu.be/aN15vtKjdP4?t=2283
'''

F = [None]*1000    

def fib(n:int):
    assert n >= 0 and n < 1000
    if F[n] is None:
        if n <= 1:
            F[n] = n
        else:
            F[n] = fib(n-1) + fib(n-2)
    return F[n]
    
print(fib(999))