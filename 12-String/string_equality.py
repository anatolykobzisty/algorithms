'''
   Наивный алгоритм проверки равенства строк
   
   теория + реализация
   https://youtu.be/rEPggzaPoUw?t=2197
   
'''

s = 'колокол'
t = 'молоко'

def string_equal(A,B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True
        
    
#запустить string_equal(s,t)