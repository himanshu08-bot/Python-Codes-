count = 0
file = open('1ltx.pdb', 'r')
for line in file:
    if line.startswith('ATOM'):
        atom_name = line[12:16].strip()
        if atom_name == 'N':
            count += 1
file.close()
print(f"The number of nitrogen atoms is: {count}")
