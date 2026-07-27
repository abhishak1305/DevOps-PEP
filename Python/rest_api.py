import requests
# ---------------------------------------------------- get -------------------------------------------------
# url = 'https://jsonplaceholder.typicode.com/todos/1'
# response = requests.get(url)
# print(response.status_code)
# print(response.json())

# ---------------------------------------------------- post -------------------------------------------------
# url = 'https://jsonplaceholder.typicode.com/posts'

# data = {
#   "userId": 9,
#   "id": 9,
#   "title": "MEIN HOON GIYAAN",
#   "completed": True
# }

# response = requests.post(url , json = data)
# print(response.status_code)
# print(response.json())

# ---------------------------------------------------- put -------------------------------------------------

url = 'https://jsonplaceholder.typicode.com/posts/1'

data = {
  "title": "DOREMON",
}

response = requests.put(url , json = data)
print(response.status_code)
print(response.json())