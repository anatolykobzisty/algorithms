'''
   Алгоритм выделения и подсчёта компонент связности неориентированного графа, 
   методом DFS (Depth-first search) - обхода графа в глубину  
   
   теория
   https://youtu.be/sBJ7ana1fgI?t=2
   
   реализация
   https://youtu.be/sBJ7ana1fgI?t=1593
'''

def dfs(vertex, G, used):
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

used = {}
N = 0

for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1
print(N)