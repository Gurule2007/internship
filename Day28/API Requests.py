import requests

# API endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")

