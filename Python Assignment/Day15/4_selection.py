# 4.	Column Selection
# o	From the students DF, select the Name column and print it.

import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)


print("Name Column: \n",df['Name'])




