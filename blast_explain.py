sequence1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNYTPGPGIRYPLTF"
sequence2 = "MKTAYIAKQRQISFVKSHFSRQDILRLWIYHTHGYMPDWQNYTPGPGIRYPLTF"

aascore = {"A": 1, "C": 5, "D": 3, "E": 3.5, "F": 7, "G": 6, "H": 8, "I": 2, "K": 7.5, "L": 2, "M": 4, "N": 6, "P": 6, "Q": 4, "R": 8, "S": 4, "T": 6, "V": 3, "W": 10, "Y": 9}
hsp = {}

# Find triplets with average score > 3.0
for j in aascore.keys():
    for l in aascore.keys():
        for m in aascore.keys():
            # Print the current triplet of amino acids
            print(j, l, m)
            # Print the average score of the triplet
            print((aascore[j] + aascore[l] + aascore[m]) / 3)
            # Check if the average score is greater than 3.0
            if (aascore[j] + aascore[l] + aascore[m]) / 3 > 3.0:
                # Concatenate the amino acids to form a triplet string
                triplet_aa = j + l + m
                # Store the triplet in the dictionary with a value of 1
                hsp[triplet_aa] = 1

triplet_dict1 = {}
triplet_dict2 = {}

# Count triplets in sequence1
for i in range(0, len(sequence1) - 2):
    triplet = sequence1[i:i+3]
    if triplet in triplet_dict1:
        triplet_dict1[triplet] += 1
    else:
        triplet_dict1[triplet] = 1

# Count triplets in sequence2
for i in range(0, len(sequence2) - 2):
    triplet = sequence2[i:i+3]
    if triplet in triplet_dict2:
        triplet_dict2[triplet] += 1
    else:
        triplet_dict2[triplet] = 1

# Compare triplets in both sequences
for k in triplet_dict1.keys():
    if k in triplet_dict2.keys():
        # Print the third amino acid of the triplet if it exists in both sequences
        print(k[2], end=" ")
    else:
        # Print "-" if the triplet does not exist in both sequences
        print("-", end=" ")

print()
