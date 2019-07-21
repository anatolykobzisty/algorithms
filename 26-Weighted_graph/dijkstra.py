'''
   Алгоритм Дейкстры - находит кратчайшие пути от одной из вершин 
   взвешенного графа до всех остальных, с очередью (без отрицательных ребер)

   теория
   https://youtu.be/2N6YbTc-USw?t=45
   
   https://youtu.be/5cX3SBItOBc?t=20
   
   реализация
   https://youtu.be/2N6YbTc-USw?t=2391
   
   https://youtu.be/5cX3SBItOBc?t=3745
'''

def main():
    G = read_graph()
    start = input("С какой вершины начать?")
    while start not in G:
        start = input("Такой вершины в графе нет. С какой вершины начать?")
    shortest_distances = dijkstra(G, start)
    finish =  input("С какой вершины построть путь?")
    while start not in G:
        start = input("Такой вершины в графе нет. С какой вершины построть путь?")
    shortest_path =  reveal_shortest_path(start,finish,shortest_distances)
    

def read_graph(G):
    M = int(input()) # количество ребер, далее - строки "A Б вес"
    G = ()
    for i  in range(M):
        a,b, weight = input().split()
        weight =float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
        
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a]  = {b: weight}
    else:
        G[a][b] = weight
        
def dijkstra(G, start):
    Q = deque() #  очередь
    S = {}  # словарь кратчайших расстоний
    S[start] = 0  #  расстояние от стартовой вершины
    Q.push(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if u not in S or S[v] + G[v][u] < S[u]:
                S[u] = S[v] + G[v][u]
                Q.push(u)
    return S        
        
