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
        print(*prefix)
        return
    for digit  in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
    
generate_numbers(4,3)

''' 
   Выписать список всевозможных 3-х буквенных слов из букв А О У.
   
   https://www.youtube.com/watch?v=d-BKnmcEmKg&list=PLRDzFCPr95fKhaTGXZzpo6ldJYTgDARZI&index=11
'''

def generate_letter(N, prefix=""):
    if N == 0:
        print(prefix)
        return
    for letter in 'А', 'О', 'У':
        generate_letter(N-1, prefix + letter)
        

generate_numbers(4,3)

generate_letter(3)
