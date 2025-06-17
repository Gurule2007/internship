'''11.	Given:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
Perform and print:
•	Union of a and b
•	Intersection of a and b
•	Difference: a - b and b - a'''

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union of a and b :", a.union(b)) 
print("Intersection of a and b :", a.intersection(b))
print("Difference a - b :", a.difference(b)) #or a - b
print("Difference b - a :", b.difference(a)) #or b - a