'''   
   Алгоритм реккурентной функции для вычисления суммы n чисел Фибоначчи
   https://youtu.be/EdhN_gEDfUM?t=1129
'''

n = int(input())

def fib(n):
    if n <= 1:
        return n
    return(fib(n-1) + fib(n-2))
for i in range(n):
        print(fib(i), end = " ")

