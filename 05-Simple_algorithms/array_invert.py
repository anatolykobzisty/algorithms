'''
   Алгоритм обращения массива
   
   https://youtu.be/3I6OjxoeSS8?t=2958
''' 

def invert_array(A, N):
    ''' 
        Обращение массива (поворот задом-наперед)
        в рамках индексов от 0 до N-1 
    '''
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k] 

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)  # печатаем результат тестирования
    invert_array(A1, 5)
    print(A1)  # печатаем результат тестирования    
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")   
        
    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)  # печатаем результат тестирования
    invert_array(A2, 8)
    print(A2)  # печатаем результат тестирования    
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_invert_array()