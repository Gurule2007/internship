'''3.	Custom Substring
Input a string from the user and print:
o	First 3 characters
o	Last 3 characters
o	Middle 5 characters'''

string = input("Enter the string : ")
print("First 3 characters : ",string[:3])
print("Last 3 characters : ", string[-3:])
middle = len(string) // 2
print("Middle 3 characters : ", string[middle-2:middle+3])