'''
   Вычисление чисел Фибоначчи и проблема перевычислений
   Динамическое программирование (рекурсия вывернутая наоборот)
   
   https://youtu.be/EdhN_gEDfUM?t=1542
'''

n = int(input())

def fib(n):
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    print(*f)
    
fib(n)

