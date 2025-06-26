# 20.	Apply a Function
# o	Use .apply() to categorize marks:
# 	Marks >= 80: Excellent
# 	Marks >= 60: Good
# 	Marks >= 40: Pass
# 	Marks < 40: Fail
import pandas as pd

data = {
    'Name': ['Piyush', 'Shubham', 'Prasad', 'Sumedh', 'Ganesh', 'Tanish'],
    'Age': [25, 22, 35, 18, 21, 23],
    'Marks': [97, 98, 89, 80, 90, 91]
}

df = pd.DataFrame(data)

def categorize_marks(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 80:
        return "Good"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"

df['Category'] = df['Marks'].apply(categorize_marks)

print("\nData with Category Column: \n", df)


