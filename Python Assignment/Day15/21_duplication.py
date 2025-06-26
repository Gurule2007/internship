# 21.	Check Duplicates
# o	Identify and remove duplicate rows in the DF.
import pandas as pd


data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}
df = pd.DataFrame(data)
print("\nDuplicate Rows: ",df[df.duplicated()])


df.loc[len(df)] = df.iloc[0]
print("\nDuplicate Row: ",df)



df = df.drop_duplicates()
print("\nRemoving Duplicates: ",df)

