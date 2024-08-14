import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos/1',auth=('user', 'pass'))
r.status_code

r.headers['content-type']
r.encoding
r.text
r.json()

print("Hello World")