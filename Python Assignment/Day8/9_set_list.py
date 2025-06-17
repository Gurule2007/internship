'''9.	Create a set from a list with repeated values:
numbers = [1, 2, 2, 3, 4, 4, 5]
o	Use set() to remove duplicates'''

numbers = [1, 2, 2, 3, 4, 4, 5]
print("\nOriginal List :",numbers)
num_set = set(numbers) #Created a set from a list 
print("Removed Duplicates (list converted into set):",num_set) #Removed the duplicates