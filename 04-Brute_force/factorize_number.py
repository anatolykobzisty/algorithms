'''
   теория
   https://youtu.be/DvsCUI5FNnI?t=3710
   
   практика
   https://youtu.be/DvsCUI5FNnI?t=4216
'''

def factorize_number(x):
    ''' Раскладывает число на множители.
        Печатает их на экран.
        x - целое положительное число.
    '''
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1