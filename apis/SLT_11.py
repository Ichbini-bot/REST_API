import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users/419"

response = requests.delete(url)

print(response.status_code)

