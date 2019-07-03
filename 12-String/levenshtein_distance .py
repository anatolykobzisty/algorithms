'''
   Расстояние Левенштейна (редакционное расстояние между строками)
   
   теория
   https://youtu.be/rEPggzaPoUw?t=271
   
   реализация
   https://youtu.be/rEPggzaPoUw?t=1460
'''
s = 'колокол'
t = 'молоко'

def levenshtein_distance(A,B):
    F = [[i+j if i*j == 0 else 0 for j in range(len(B) + 1)] 
         for i in range(len(A) + 1)]
    for  i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]

#запустить levenshtein_distance(s,t) 