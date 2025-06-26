# 5.	Row Selection by Position
# o	Use .iloc to print the first 3 rows.



import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)
print("\nFirst 3 rows: \n", df.loc[:2] )