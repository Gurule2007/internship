# 17.	Sorting
# o	Sort the DF by Marks in ascending and then in descending order.
import pandas as pd


data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}
df = pd.DataFrame(data)

\
df_sorted_asc = df.sort_values(by='Marks', ascending=True)
print("\nSort by Marks in Ascending Order: ",df_sorted_asc)

df_sorted_desc = df.sort_values(by='Marks', ascending=False)
print("\nSort by Marks in Descending Order: ",df_sorted_desc)








