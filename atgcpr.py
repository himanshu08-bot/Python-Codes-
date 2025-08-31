file = open('gene.fasta', 'r')
seq = file.read().replace('\n', '')
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'ERROR': 0}
for base in seq :
	if base == 'A':
		counts['A'] += 1
	elif base == 'T':
		counts['T'] += 1
	elif base == 'C':
		counts['C'] += 1
	elif base == 'G':
		counts['G'] += 1
	else:
		counts['error'] += 1
total_count = sum(counts.values())
print("BC")
for base, count in counts.items():
	print (f"{base}:{count}")


