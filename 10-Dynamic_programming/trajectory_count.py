'''
   Одномерное динамическое программирование
   Алгоритм нахождения количества траекторий

   https://youtu.be/EdhN_gEDfUM?t=2095
'''

def trajectory_count(N):
	K = [0, 1] + [0]*N
	for i in range(2, N + 1):
		K[i] = K[i - 1] + K[i - 2]
	return K[N]