def count_nitrogen(pdb_file):
	count = 0
	file = open (pdb_file, 'r')
	for line in file:
		if line.startswith('ATOM'):
			atom = line[12:16].strip()
			if atom == 'N':
				count += 1
	return count
pdb_file = '1ltx.pdb'
nitrogen_count = count_nitrogen(pdb_file)
print (nitrogen_count)
