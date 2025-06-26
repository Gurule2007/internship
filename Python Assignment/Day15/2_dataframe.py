# 2.	Create a DataFrame
# o	Create a DataFrame called students with columns:
# 	Name (string), Age (int), Marks (float)
import pandas as pd
data = {
    'Name': ['Piyush', 'Aditya', 'Prasad'],
    'Age': [25, 30, 35],
    'Marks': [97, 98, 99]
}
df = pd.DataFrame(data)
print(df)