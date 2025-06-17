set1 ={1,2,3,4,5}
set2 ={6,7,4,8,2}

print(set1.intersection(set2))
print(set1)
print(set1-set2)
print(set2-set1)
print(set1.union(set2))
print(set1.symmetric_difference(set2))


tup = ([1,2],[3,4])
tup[0][1] = 99
print(tup)