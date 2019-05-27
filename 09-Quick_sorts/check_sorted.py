''' 
   Проверка упорядоченности массива за O(N).

   https://youtu.be/qf82-r9hl2Y?t=2997
'''

def check_sorted(A, s = 2 * int(ascerding) - 1): #по возрастанию
    for i in range(0, N-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag