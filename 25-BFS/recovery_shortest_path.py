'''
   Алгоритм восстановления кратчайшего пути в незвешанном графе, 
   методом BFS (Breadth-First Search) - обхода графа в ширину

   https://youtu.be/S-hjsamsK8U?t=1942
'''
N, M = map(int,input().split())

graph = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
    
from collections import deque 
distances = [None] * N
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])
    
parents = [None] * n

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
print(path[::-1])