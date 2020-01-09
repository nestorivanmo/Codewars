def row_sum_odd_numbers(n):
	s = 0
	max_number = max(n)
	min_number = max(n-1) + 1
	return sum_odd(min_number, max_number)

def max(n):
	if n is 1:
		return 1
	if n is 0:
		return 0
	else:
		return max(n-1) + n

def sum_odd(low, high): 
	odds = []
	for i in range(1, high+1):
		odds.append((i*2)-1)
	s = 0
	for i in range(low-1, high):
		s += odds[i]
	return s

print(row_sum_odd_numbers(13))