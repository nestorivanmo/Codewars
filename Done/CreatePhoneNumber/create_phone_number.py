def create_phone_number(n):
	string = ""
	counter = 0
	for index in n:
		if counter is 0:
			string += "("
		elif counter is 3:
			string += ") "
		elif counter is 6:
			string += "-"		
		string += str(index)
		counter += 1
	return string

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))