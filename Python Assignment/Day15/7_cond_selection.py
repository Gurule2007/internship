# 7.	Conditional Selection
# o	Select students with Marks > 75.
# o	Select students with Age <= 20.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)

print("\nStudents with marks greater than 75: \n")
print(df[df['Marks'] > 75])
print("\nStudents which age less than 20: ")
print(df[df['Age'] <= 20])
