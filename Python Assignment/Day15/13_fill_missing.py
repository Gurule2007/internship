# 13.	Fill Missing Values
# o	Fill NaN in the Marks column with the average marks.
import pandas as pd
import numpy as np

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [25, np.nan, 35, 18, np.nan],
    'Marks': [97, 98, np.nan, 80, 90]

}
df = pd.DataFrame(data)
print("Fill missing values: \n",df)
