'''
   Алгоритм Кнута-Морриса-Пратта
   
   теория префикс функции "Pi" строки
   https://youtu.be/rEPggzaPoUw?t=3240
   
   реализация
   https://youtu.be/rEPggzaPoUw?t=4281
   
   
Префикс--функция строки pi[i] - массив длинной строки, где pi[i] - длина наибольшего по длине собственного суффикса подстроки (среза) начиная от начала и до позиции (s[:i+1])

     "a  a  a  a  a"
pi = [0, 1, 2, 3, 4]

     "a  b  a  c  a  b  a"
pi = [0, 0, 1, 0, 1, 2, 3]

'''
s = 'abacabadabacabafabacabadabacabadabacabafaba'

sub = 'abac'

def prefix(s):
    n = len(s)
    pi = [0]*n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

#запустить prefix(s)     
     
#http://py-algorithm.blogspot.com/2013/04/blog-post_19.html

def kmp(s, sub):
    pi = {0:0}
    template = sub + '#' + s
    for i in range(1, len(template)):
        j = pi[i-1] #незачем смотреть всю строку, можно посмотреть со сдвига прошлой подстроки
        while j > 0 and template[j] != template[i]:
            j = pi[j-1]
        if template[j] == template[i]:
            j += 1
        pi[i] = j
        if j == len(sub):
            return i
    return None 

#запустить prefix(s, sub)     
