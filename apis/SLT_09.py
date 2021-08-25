import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name" : "Tobi",
    "last_name" : "Schmid",
    "email" : "toby.schmid@migros.com"
}

response = requests.post(base_url, json=body)

print(f"Response code: {response.status_code}")

response = requests.get(base_url)

#print(f"Response Content: {response.content}")

data = response.json()


pprint(data)