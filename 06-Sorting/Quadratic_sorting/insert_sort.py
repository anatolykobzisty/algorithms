'''
   Сортировка списка A вставками
   
   теория
   https://youtu.be/NLq7nB9bV0M?t=1140
   
   практика
   https://youtu.be/NLq7nB9bV0M?t=3573
'''

def insert_sort(A):
     N = len(A)
     for top in range(1, N):
          k = top
          while k > 0 and A[k-1] > A[k]:
               A[k], A[k-1] = A[k-1], A[k]
               k -= 1

def test_sort(sort_algorithm):
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    
    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")
    
    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")   

test_sort(insert_sort)
    


