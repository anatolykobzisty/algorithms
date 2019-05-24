'''
   Сортировка подсчетом
   
   теория
   https://youtu.be/NLq7nB9bV0M?t=4310
   
   практика
   https://youtu.be/L-8Nxs4bWhI?t=2460
'''
frequency = [0]*10
digit = int(input())
while 0 <= digit <= 9:
	frequency[digit] += 1
	digit = int(input())
	for digit in range(10):
		print(*[digit]*frequency[digit], end=' ')