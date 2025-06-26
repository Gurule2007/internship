# 16.	Grouping
# o	Add a column Class (e.g., Class A or Class B).
# o	Group the DF by Class and compute the average marks per class.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]

}
df = pd.DataFrame(data)

df['Class'] = ['A','B','A','B','A','B']
print("Adding class column: \n",df)


a_marks = df.groupby('Class')['Marks'].mean()
print("\nAverage Marks per Class: ",a_marks)
