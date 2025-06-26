# 3.	Check Properties
# o	Print:
# 	.shape
# 	.columns
# 	.dtypes
# 	.info()
# 	.describe() (for numeric columns)
import pandas as pd
data = {
    'Name': ['Piyush', 'Aditya', 'Prasad'],
    'Age': [25, 30, 35],
    'Marks': [97, 98, 99]
}
df = pd.DataFrame(data)
print(df)

print("Shape: ",df.shape)
print("Columns: ",df.columns)
print("Datatype: ",df.dtypes)
print("Info: ",df.info())
print("Summary: ",df.describe())
