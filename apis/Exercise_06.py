'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.

Simplified version, based on cn user database
'''
import requests

#Functions
def request(body):
    url = "http://demo.codingnomads.co:8080/tasks_api/users"
    response = requests.post(url, json=body)
    return response

def user_data(fn, ln, mail):
    body = {
        "id" : "",
        "first_name" : fn,
        "last_name" : ln,
        "email" : mail
    }
    return body

def decision_tree(jsonbody):
    while True:
        uploadpermission = input("Do you want to upload your data? pls confirm with Yes or No: ")
        if uploadpermission == "Yes":
            return request(jsonbody)
            break
        elif uploadpermission == "No":
            print("you didnt want to upload your user data - thats fine")
            break
        else:
            print("pls confirm with either Yes or No")

# Program execution
firstname = input("pls enter your firstname: ")
lastname = input("pls enter your lastname: ")
email = input("pls enter your email: ")

decision_tree(user_data(firstname, lastname, email))






