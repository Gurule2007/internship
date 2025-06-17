#15. Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.
divisible_list = [num for num in range(1, 50+1) if num % 3 == 0 and num % 5 == 0]
print("Divisible List :", divisible_list)