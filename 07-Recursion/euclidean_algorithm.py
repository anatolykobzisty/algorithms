'''
   Aлгоритм Евклида
   
   https://youtu.be/0Bc8zLURY-c?t=3083
'''

def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)