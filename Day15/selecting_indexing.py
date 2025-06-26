import pandas as pd

data = {
    "Name": ["Piyush", "Shubham", "Prasad", "Sumedh", "Aditya"],
    "Age": [28, 35, 42, 25, 38],
    "City": ['Delhi', 'Mumbai', 'Bangalore','Nashik','pune']
}

df = pd.DataFrame(data)

# Select only the Name column
print("Name column:")
print(df["Name"])

# Select the first 3 rows using .iloc
print("\nFirst 3 rows:")
print(df.iloc[:3])

# Select people older than 30
print("\nPeople older than 30:")
print(df[df["Age"] > 30])
