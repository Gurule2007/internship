'''5.	Loop Through Dictionary
Write a loop to print each key and its value in the student dictionary.'''
print("\nLooping thorugh dictionary - ")
student = {"name" : "Alice", "age" : 20, "course" : "Python"}
for key, value in student.items():
    print(f"{key}:{value}")
