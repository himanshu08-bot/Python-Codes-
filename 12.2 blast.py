sequence1 = "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFPDWQNYTPGPGIRYPLTF"
sequence2 = "QFTAYIAKQRQISFVKSHFSRQDILRLWIYHTHGYMPDWQNYTPGPGIRYPQRF"


triplet_dict1 = {}
triplet_dict2 = {}

for i in range(0, len(sequence1) - 2):
    triplet = sequence1[i:i+3]
    if triplet in triplet_dict1.keys():
        val = triplet_dict1[triplet]
        val = val + 1
        triplet_dict1[triplet] = 1
    else:
        triplet_dict1[triplet] = 1

for i in range(0, len(sequence2) - 2):
    triplet = sequence2[i:i+3]
    if triplet in triplet_dict2.keys():
        val = triplet_dict2[triplet]
        val = val + 1
        triplet_dict2[triplet] = val
    else:
        triplet_dict2[triplet] = 1

for k in triplet_dict1.keys():
    if k in triplet_dict2.keys():
        print (k[2], end= " ")
    else:
        print ("-", end= " ")
        
print()