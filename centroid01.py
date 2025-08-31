pdb_file = open("1ltx.pdb", 'r')
sum_x = sum_y = sum_z = 0.0
atom_count = 0

for line in pdb_file:
    if line.startswith("ATOM"):
        x = float(line[30:38].strip())
        y = float(line[38:46].strip())
        z = float(line[46:54].strip())
        
        sum_x += x
        sum_y += y
        sum_z += z
        
        atom_count += 1

centroid_x = sum_x / atom_count
centroid_y = sum_y / atom_count
centroid_z = sum_z / atom_count

print(f'Centroid coordinates: ({int(centroid_x)}, {int(centroid_y)}, {int(centroid_z)})')
