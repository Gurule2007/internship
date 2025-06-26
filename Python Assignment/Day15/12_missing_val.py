# 12.	Check for Missing Values
# o	Use .isnull() and .sum() to count NaNs.
import pandas as pd
import numpy as np

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [25, np.nan, 35, 18, np.nan],
    'Marks': [97, 98, np.nan, 80, 90]

}
df = pd.DataFrame(data)
print("Data with missing values: \n",df)
print("Missing values: ",df.isnull().sum())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
