file = open("1ltx.pdb", 'r')
charge_atom = {
    'ASP' : -1,
    'GLU' : -1,
    'LYS' : 1,
    'HIS' : 1             
}
total_charge = 0
for line in file:
    if line.startswith("ATOM"):
        atom = line[17:20].strip()
        if atom in charge_atom:
            total_charge += charge_atom[atom]
print(total_charge)
