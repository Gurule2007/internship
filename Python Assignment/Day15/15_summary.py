# 15.	Summary Stats
# o	Find the total, average, max, and min marks from the DF.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]

}
df = pd.DataFrame(data)

print("Total of marks: ",df['Marks'].sum())
print("Maximum Mark: ",df['Marks'].max())
print("Minimum Marks: ",df['Marks'].min())
print("Average marks: ",df['Marks'].mean())


