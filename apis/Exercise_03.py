'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

#body of .json tat needs to be updated
body = {
    "first_name" : "Tobi",
    "last_name" : "Schmid",
    "email" : "toby.schmid@migros.com"
}

response = requests.post(base_url, json=body)

print(f"Response code: {response.status_code}")

answer = requests.get(base_url)

#print(f"Response Content: {response.content}")

data = answer.json()


pprint(data)