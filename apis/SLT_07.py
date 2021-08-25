import requests

'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/user"
response = requests.get(base_url)
print(response.status_code)
'''
'''
response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users?email=ryan@codingnomads.co")
print(response.status_code)

#is the same as 

parameter = {
    "email": "ryan@codingnomads.co"
}

response = requests.get("http://demo.codingnomads.co:8080/tasks_api/users", params=parameter)
print(response.status_code)
'''
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

print(f"Response Content: {response.content}")
print(f"Response Status Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Response Encoding: {response.encoding}")
print(f"Response URL: {response.url}")
