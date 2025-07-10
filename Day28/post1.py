import requests
# API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"
# New post data
new_post = {
    "title": "My New Post",
    "body": "This is the body of my new post",
    "userId": 1
}
# Send POST request
response = requests.post(url, json=new_post)
# Print response status code and new post
print(f"Status Code: {response.status_code}")
print("New Post:")
print(response.json())
