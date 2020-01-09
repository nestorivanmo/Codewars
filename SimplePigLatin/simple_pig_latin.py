def pig_it(text):
	word = ""
	new_text = ""
	i = -1
	for letter in text:
		i += 1
		if letter.isalpha():
			word += letter
			if i is len(text) - 1:
				arr = get_array_from(word)
				nw = convert(arr)
				new_text += nw
		else:
			arr = get_array_from(word)
			converted_word = convert(arr)
			if i is len(text)-1:
				word += letter
				new_text += letter
				break
			else:
				new_text += converted_word + " "
			word = ""
	return new_text

def get_array_from(word):
	array = []
	for letter in word:
		array.append(letter)
	return array

def convert(array):
	if len(array) > 0:
		first = array[0]
		arr = array[1:]
		word = ""
		arr.append(first + "ay")
		for l in arr:
			word += l
		return word
	return []

print(pig_it("This is my string"))