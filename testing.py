allAges = [22,21,33,24,19,20]
# array / list
totalAge = 0

for age in allAges:
    totalAge += age
    
print("Total age: ", totalAge)
print("Average age: ", totalAge/len(allAges))


ageOf = {"abhishek": 25, "abhinav": 29, "himanshu": 19, "sarthak": 12}

print("Himanshu: ", ageOf.get("abhinav"))