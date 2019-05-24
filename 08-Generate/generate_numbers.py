'''
   Рекурсивная генерация всех чисел (с лидирующими нулями) длины M
   в N-ричной системе счисления (N <= 10)

   теория
   https://youtu.be/2XFaK3bgT7w?t=37

   практика 
   https://youtu.be/2XFaK3bgT7w?t=1634
'''
def generate_numbers(N:int, M:int, prefix=None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit  in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
    
generate_numbers(4,3)