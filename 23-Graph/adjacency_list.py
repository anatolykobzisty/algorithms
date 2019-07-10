'''
   Считывание списка ребер с помощью списка смежности
   
   Теория
   https://youtu.be/rg7DX6U0v9k?t=1890
   
   Реализация
   https://youtu.be/rg7DX6U0v9k?t=3647
'''
#  N - количество вершин
#  M - количество ребер

M,N = [int(x) for x in input().split()]

G = {}
for i  in range(N):
    v1,v2 = input().split()
    for v,u in (v1,v2), (v2,v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)
    ...