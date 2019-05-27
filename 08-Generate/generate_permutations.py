'''
   Рекурсивная генерация всех перестановок N чисел 
   в M позициях с префиксом
   
   https://youtu.be/2XFaK3bgT7w?t=2327
'''

def find(number, A):
    '''
       ищет number в A и возвращает True, если такой есть 
       False если такого нет
    '''
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_permutations1(N:int, M:int=-1, prefix=None):
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations1(N, M-1, prefix)
        prefix.pop()

'''
   Рекурсивная генерация всех перестановок N чисел 
   от 1 до N
   
   https://youtu.be/d-BKnmcEmKg?t=1769
'''

def generate_permutations2(N, prefix=[]):
        if len(prefix) == N:
                print(*prefix)
                return
        for x in range(1, N+1):
                if x not in prefix:
                        generate_permutations2(N, prefix + [x])
                        

generate_permutations1(2)

generate_permutations2(3)


