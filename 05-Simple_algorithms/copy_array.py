'''
   Алгоритм копирование массива
   
   https://youtu.be/3I6OjxoeSS8?t=1628
'''

N = int(input())
A = [0]*N  #  заранее известен размер массива
B = [0]*N
for k in range(N):
    A[k] =int(input())
for k in range (N):
    B[k] = A[k] 