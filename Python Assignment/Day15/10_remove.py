# 10.	Remove a Column
# o	Drop the Age column and print the resulting DF.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)
df = df.drop('Age',axis=1)
print("Remove Age column: \n",df)