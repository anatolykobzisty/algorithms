'''
   Одномерное динамическое программирование
   Алгоритм нахождения количества траекторий с запрещенными клетками

   https://youtu.be/EdhN_gEDfUM?t=2563
'''

def count_trajectories(N, allowed:list):
    K = [0,1, int(allowed[2])] + [0]*(N-3)
    for i in range(3, N + 1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]