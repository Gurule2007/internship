# 18.	Rename Columns
# o	Rename columns Name -> Student Name, Marks -> Total Marks.
import pandas as pd


data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}
df = pd.DataFrame(data)

df = df.rename(columns={'Name':'Student Name', 'Marks':'Total Marks'})
print("\nRenamed Columns: ",df)
