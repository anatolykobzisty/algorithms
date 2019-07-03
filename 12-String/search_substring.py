'''
   Наивный алгоритм поиска подстроки в строке
   
   теория
   https://youtu.be/rEPggzaPoUw?t=2557
'''

s = 'abacabadabacabafabacabadabacabadabacabafaba'
sub = 'dabac'


def string_equal(A,B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

def search_substring(s,sub):
    for i in range(0,len(s)-len(sub)):
        if string_equal(s[i: i + len(sub)], sub):
            print(i)
            
#запустить search_substring(s,sub)