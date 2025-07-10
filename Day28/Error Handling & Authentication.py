import requests

response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")

if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Error {response.status_code}: The requested resource was not found.")
