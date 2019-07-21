'''
   Алгоритмы Флойда-Уоршелла - поиск в графе кратчайших путей между любыми парами вершин (динамическое программирование)
   
   теория
   https://youtu.be/2N6YbTc-USw?t=3829
   
   https://youtu.be/5cX3SBItOBc?t=5191
   
   реализация
   https://youtu.be/5cX3SBItOBc?t=7560
'''

#https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

def graph_input():
    N = int(input("Количество вершин в графе: "))
    weight = [[float('+inf')] * N for j in range(N)]
    M = int(input("Количество ребер в графе: "))
    for i in range(N):
        weight[i][i] = 0
    for i in range(M):
        a, b, w = input().split()
        a, b, w = int(a), int(b), float(w)
        weight[a][b] = w
        weight[b][a] = w
    return weight

def print_matrix(A):
    for i in range(len(A)):
        print(*A[i], sep="\t")
    print()
       
from copy import deepcopy    

def floyd(weight):
    N = len(weight)
    F = deepcopy(weight)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])
        print_matrix(F)
    return F

G = graph_input()
print_matrix(G)
floyd(G)
