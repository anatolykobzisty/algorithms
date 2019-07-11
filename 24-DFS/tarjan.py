'''
   Алгоритм Тарьяна - топологическая сортировка,
   методом DFS (Depth-first search) - обхода графа в глубину  

   теория
   https://youtu.be/sBJ7ana1fgI?t=3383
   
   реализация
   https://youtu.be/sBJ7ana1fgI?t=3822
'''

def dfs(start, G, visited, ans):
    visited[start] = True
    for u in G[start]:
        if not visited[u]:
            dfs(u, G, visited, ans)
    ans.append(start)

visited = set()
ans =[]

for vertex in G:
    if vertex not in visited:
        dfs(vertex, G, visited, ans)
ans[:] = ans[::-1]