'''
   Рекуррентная сортировка (Быстрая сортировка)
   Сортировка Тони Хоара
   
   теория
   https://youtu.be/2XFaK3bgT7w?t=3448
   
   реализация
   https://youtu.be/qf82-r9hl2Y?t=2000
'''

def hoare_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoare_sort(L)
    hoare_sort(R)    
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

M = [2, 4, 15, -4, 33, 9, 0, 4, 8]

hoare_sort(M)
                
print(M)
