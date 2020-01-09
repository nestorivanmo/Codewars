def longest(s1, s2):
    unique = []
    unique = ap(s1, unique)
    unique = ap(s2, unique)
    sorted_array = sorted(unique)	    
    s = ''.join(sorted_array)
    return s
    

def ap(s, unique):
	for letter in s:
		if letter.isalpha():
			if letter in unique:
				pass
			else:
				unique.append(letter)
	return unique
print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))