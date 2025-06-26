import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "Products": ["Laptop", "Smartphone", "Tablet", "phones", "Mouse"],
    "Price": [1000, 800, 600, 200, 400],
    "Stock": [10, 20, 15, 30, 25]
})

print(df)

# head
print("Head:")
print(df.head())

# tail
print("\nTail:")
print(df.tail())

# information
print("\nInfo:")
print(df.info())

# Describe
print("\nDescribe:")
print(df.describe())
