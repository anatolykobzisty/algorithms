'''
   Алгоритм нахождения факториала, методом динамического программирования
   
   Разница между рекурсией и динамическим программированием
   https://youtu.be/aN15vtKjdP4?t=1
'''

def factorial(n):
    f = [1]*(n+1)
    for i in range(1, n+1):
        f[i]= f[i-1]*i
    return print(f[n])

factorial(10)