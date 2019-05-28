'''
   Бинарный поиск в массиве A
   
   теория
   https://youtu.be/qf82-r9hl2Y?t=3472
   
   реализация
   https://youtu.be/EdhN_gEDfUM
'''

def left_board(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_board(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


            
                