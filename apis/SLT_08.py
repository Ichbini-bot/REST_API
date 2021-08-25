import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()

for mail in data["data"]:
    print(mail["email"])

print("*************************")

def list(variable):
    mailinglist = [mail["email"] for mail["data"] in variable]
    return mailinglist

print(list(data))

'''
data2 = data["data"]

pprint(data2[0])

for mail in data2:
    print(mail["email"])
'''
    



#what happens if you print data['data'][0]['first_name']

'''
print(data["data"][0]["first_name"])
print(data["data"][0]["last_name"])

print(data["data"][1]["first_name"])
print(data["data"][1]["last_name"])
print(data["data"][1]["email"])

list = [{"name":"Tobi Schmid", "email":"tobi.schmid@me.com"},{"name":"Roli Stadler", "email":"roli@stadler.org"}]
dict = {"name":"Tobi Schmid", "email":"tobi.schmid@me.com", "name":"Roli Stadler", "email":"roli@stadler.org"}

print("XXXXXXXXXXXXXXX")

print(list[0]["email"])

for n in list:
    print(f"{n['name']}")

for n in list:
    print(n["email"])
'''



