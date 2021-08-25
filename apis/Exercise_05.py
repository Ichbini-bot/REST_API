'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users/430"

response = requests.delete(url)

url2 = "http://demo.codingnomads.co:8080/tasks_api/users"
answer = requests.get(url2).json()

#print(response.status_code)
pprint(answer)