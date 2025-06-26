# 6.	Row Selection by Label
# o	Set Name as the index and use .loc to fetch a student by name.
import pandas as pd
data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)
df.set_index('Name', inplace=True)
print("\nFetch by name: \n",df.loc['Piyush'])
