tup =(1,4,7,5,4,3,2,3,18)
repeated = []
for i in tup:
    if tup.count(i) > 1 and i not in repeated:
        repeated.append(i)

print(repeated)
    
