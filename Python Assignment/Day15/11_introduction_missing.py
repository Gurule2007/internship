# 11.	Introduce Missing Values
# o	Create a DF with columns Name, Age, Marks where some Age and Marks values are NaN.
import pandas as pd
import numpy as np

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad','Sumedh','Ganesh'],
    'Age': [25, np.nan, 35, 18, np.nan],
    'Marks': [97, 98, np.nan, 80, 90]

}
df = pd.DataFrame(data)

