'''7.	Get with Default
o	Use get() to retrieve "grade" from the dictionary.
Provide default value "Not Assigned".'''
student = {"name" : "Alice", "age" : 20, "course" : "Python"}
print("\nGrade : ", student.get("grade", "Not Assigned"))