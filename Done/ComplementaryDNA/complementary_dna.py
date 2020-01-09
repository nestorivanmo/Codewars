
def DNA_strand(dna):
	dna = dna.upper()
	dna_complement = ""
	for letter in dna:
		dna_complement += get_complement(letter)
	return dna_complement


def get_complement(letter):
	if letter is "A": 
		return "T"
	if letter is "T":
		return "A"
	if letter is "C":
		return "G"
	if letter is "G":
		return "C"

def DNA_strand_other(dna):
	return dna.translate(str.maketrans('ATCG', 'TAGC'))

print(DNA_strand("ATTGC"))
print(DNA_strand_other("ATTGC"))