'''
   Алгоритм циклического сдвига влево

   https://youtu.be/3I6OjxoeSS8?t=3819
'''

A = [1, 2, 3, 4, 5]
N = 5
def circular_left_shift(A, N):
tmp = A[0]
for k in range(N-1): 
    A[k] = A[k+1]
A[N-1] = tmp
print(A)
if A == [2, 3, 4, 5, 1]:
    print("#test1 - ok")

circular_left_shift(A, N)