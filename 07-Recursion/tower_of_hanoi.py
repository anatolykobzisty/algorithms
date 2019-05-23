'''
   Ханойская башня
   
   https://youtu.be/0Bc8zLURY-c?t=4526
'''

def hanoi(n, i=1, k=2):
    if n == 1:
        print('переставить 1', 'блин с', i, 'на', k, 'стержень')
    else:
        hanoi(n - 1, i, 6 - i - k)
        print('переставить', n, 'блин c', i, 'на', k, 'стержень')
        hanoi(n - 1, 6 - i - k, k)
            
            
        
    