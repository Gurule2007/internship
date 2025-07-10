import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print("First Post:")
print(response.json()[0])


