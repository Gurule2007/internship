# 8.	Add a New Column
# o	Add a column Pass which is True if Marks >= 40 else False.


import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)


df['Pass'] = df['Marks'] >= 40
print("Add Column Pass: \n")
print(df)
