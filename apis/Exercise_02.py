'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url).json()

def mailing(data):
    emaillist = [mail["email"] for mail in data["data"]]
    return emaillist

print(mailing(response))

'''
#CROWBAR METHOD: convert response into .json and "strip" from "data" - easier to access - Q: CAN I DO THAT DIRECTLY?
data = response.json()
data = response.json()["data"]

#1.) Common approach

maillist = []
for mail in data:
    maillist.append(mail["email"])
print(maillist)

print("***********************")

#2.) Function approach via list comprehension

#Approach via function including list comprehension - "stripped" of data - Q: HOW TO DO, WHEN NOT "STRIPPED" FROM DATA (I SHOULD KNOW NOW, BUT STILL NOT ABLE...?) 

def email(variable):
    mailinglist = [mail["email"] for mail in variable]
    return mailinglist
print(email(data))

#ELEGANT / DIRECT WAY:

#3.) Directly via list comprehension:

list = []
for mail in data["data"]:
    list.append(mail["email"])
print(list)
'''


