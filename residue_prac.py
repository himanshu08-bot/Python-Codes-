file = open("1ltx.pdb",'r').readlines()

residues = []
amino_acids = {}

for line in file:
	if line.startswith('ATOM') and line[21] == 'B':
		residue = int(line[22:26].strip())
		amino_acid = line[17:20].strip()

		if residue not in residues:
			residues.append(residue)
			amino_acids[residue] = amino_acid
midpoint = len(residues) // 2
center_residue = residues[midpoint]
center_amino_acid = amino_acids[center_residue]

print ("The centre residue in chain B:", center_residue)
print ("The corrensponding amino aicds are:", center_amino_acid)
