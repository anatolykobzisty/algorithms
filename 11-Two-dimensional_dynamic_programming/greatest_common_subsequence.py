'''
   Алгоритм нахождения длины наибольшей общей подпоследовательности
   
   теория
   https://youtu.be/m4HOkVeN4Mo?t=1710
   
   реализация
   https://youtu.be/m4HOkVeN4Mo?t=3034
'''
A = [1,2,3,4,5,6,7,8,9,10]
B = [1,2,3,4,5,6,7]

def gcs(A,B):
    F = [[0]*(len(B) + 1) for i in range(len(A) + 1)]
    for i in range (1, len(A) + 1):
        for j in range (1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 +F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]  

# запусть gcs(A,B)