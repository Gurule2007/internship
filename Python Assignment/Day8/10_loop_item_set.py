
#10. Use a loop to print all items in a set.

numbers = [1, 2, 2, 3, 4, 4, 5]
print("\nOriginal List :",numbers)
num_set = set(numbers) #Created a set from a list 
print("All items of set :", end = " ")
for i in num_set:
    print(i, end = " ")