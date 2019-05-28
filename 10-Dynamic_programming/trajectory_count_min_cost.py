'''
   Одномерное динамическое программирование
   Алгоритм нахождения суммы наименьшей стоимости на траектории
   
   https://youtu.be/EdhN_gEDfUM?t=3078
'''

def count_min_cost(n, price:list):
    C = [float("-inf"), price[1],price[1] + price[2]] + [0]*(n-2)
    for i in range (3, n+1):
        C[i]=price[i] + min(C[i-1], C[i-2])
    return C[n]