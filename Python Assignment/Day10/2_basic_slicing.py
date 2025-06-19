'''2.	Basic Slicing
From the same string:
o	Print the substring "Python"
o	Print the substring "Programming"
o	Print every second character (::2)
o	Reverse the string using slicing'''

text = "PythonProgramming"
print("\nSubstring \"Python\" : ",text[:6])
print("Substring \"Programming\" : ",text[6:])
print("Every second character : ",text[::2])
print("Reverse string : ", text[::-1])
