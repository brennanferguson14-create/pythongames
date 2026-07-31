#converting a list into a set
numlist = [34,61,89,44,73,24]
numset = set(numlist)
print(numset)
#do sets have index numbers
#print(numset[2])
#check is a certain element exists in the set
if 44 in numset:
    print("yes")
else:
    print("no")

#how to add an element to a set
numset.add(90)
numset.add(60)

print("numset")

numset.remove(89)
print(numset)
numset.discard(45)

a = {3,8,1,2}
b = {2,4,3,9}
aub = {1,2,3,4,8,9}