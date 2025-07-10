import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "New Post",
    "body": "This is a test post.",
    "userId": 1
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print("Response:")
print(response.json())
