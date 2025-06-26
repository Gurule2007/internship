# 19.	Export DF
# o	Export the final DF to a .csv file named student_records.csv.
import pandas as pd


data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}
df = pd.DataFrame(data)
df.to_csv('student_records.csv',index=False)
print("\nExported to student_records.csv")
