'''
   Алгоритм циклического сдвига вправо.
   
   https://youtu.be/3I6OjxoeSS8?t=3984
'''

A = [1, 2, 3, 4, 5]
N = 5
def circular_left_shift(A, N):
tmp = A[N-1]
for k in range(N-2,-1,-1): 
    A[k+1] = A[k]
A[0] = tmp
print(A)
if A == [2, 3, 4, 5, 1]:
    print("#test1 - ok")


circular_left_shift(A, N)