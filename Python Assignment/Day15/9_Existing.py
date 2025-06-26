# 9.	Modify an Existing Column
# o	Increase every student’s marks by 5.
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [21, 22, 20, 18, 17],
    'Marks': [74, 73, 80, 70, 22]
}
df = pd.DataFrame(data)
df['Marks'] = df['Marks']+5
print("\n Marks Increased by 5: \n",df)
