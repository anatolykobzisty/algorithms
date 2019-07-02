'''
   Алгоритм нахождения длины наибольшей возрастающей подпоследовательности

   теория
   https://youtu.be/m4HOkVeN4Mo?t=3650
   
   реализация
   https://youtu.be/m4HOkVeN4Mo?t=4324
'''

A = [1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,11]

def gis(A):
    F =[0]*(len(A) + 1)
    for i in range(1, len(A) + 1):
        m = 0
        for j in range(0, i):
            if A[i-1] > A[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(A)]

#запустить gis(A)
               
    