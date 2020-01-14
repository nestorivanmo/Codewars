def tribonacci(signature, n):
	if n <= 3:
		return signature[0:n]
	for i in range(n-3):
		signature.append(sum(signature[i:i+3]))
	return signature

print(tribonacci([12, 1, 1], 1))