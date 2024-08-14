import requests
import json
from urllib.parse import urlparse


try:
    api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    api_respose_json = api_response.json()
    print(api_respose_json)
    for item in api_respose_json:
        print(item)
    # Go through all of the todos and sort them by ascending alphabitcal order (a-z) based on the second letter in each todo's title
    
except Exception as error:
    print("There was an error with the request", error)


