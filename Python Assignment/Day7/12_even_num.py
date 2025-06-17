#12. From a list of numbers 1 to 20, create a new list that contains only even numbers using list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even = [num for num in numbers if num % 2 == 0]
print("\nEven Numbers List :", even)

