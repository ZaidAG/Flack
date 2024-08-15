import requests
import json
from urllib.parse import urlparse

def second_let(x):
    return x[1]

try:
    api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    api_respose_json = api_response.json()
    # Go through all of the todos and sort them by ascending alphabitcal order (a-z) based on the second letter in each todo's title
    
    
    for item in api_respose_json:
        print(second_let(item["title"]))
    
except Exception as error:
    print("There was an error with the request", error)

