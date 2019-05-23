'''
   Быстрое возведение в степень n, где n - целое и  n > 0
   
   https://youtu.be/0Bc8zLURY-c?t=3929 
'''

def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n%2 == 1: #n - нечетное
        return pow(a, n-1)*a
    else: # n - четное
        return pow(a**2, n//2)