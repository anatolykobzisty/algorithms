'''
    "Решето Эратосфена" - алгоритм нахождения всех простых чисел до некоторого 
    целого числа n 

    Рассмотрим два множества: 
       A - изначальное множество 
       A1- пустое множество
    1. Выберем самое маленькое число из множества A и поместим 
       его во множество A1.
    2. Затем вычеркнем из первого множества это число и все числа 
       кратные ему.
    3. Продолжаем процесс до тех пор, пока первое множемтво не станет  
       пустым. А второе множество заполнится простыми числами.  
    
    https://youtu.be/3I6OjxoeSS8?t=4245
'''
N = 10
A = [True]*N
A[0]=A[1]=False
for k in range (2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
for k in range(N):
    print(k,'-', "простое" if A[k] else "составное")
