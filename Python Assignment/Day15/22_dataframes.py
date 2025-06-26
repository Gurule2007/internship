# 22.	Merge Two DataFrames
# o	Create another DF with columns Name and Class Teacher.
# o	Merge both DFs on the Name column.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}

df = pd.DataFrame(data)

data2 = {
    'Student Name': ['Piyush', 'Shubham', 'Prasad', 'Rohan', 'Aryan'],
    'Class Teacher': ['Ms. Gaidhani', 'Mr. Sangle', 'Ms. Suslade', 'Ms. Waghchoure', 'Mr. Mahajan']
}

df2 = pd.DataFrame(data2)

print("\nDataFrame 1: \n", df)
print("\nDataFrame 2: \n", df2)

merged_df = pd.merge(df, df2, left_on='Name', right_on='Student Name', how='left')

print("\nMerged DataFrame:")
print(merged_df)

