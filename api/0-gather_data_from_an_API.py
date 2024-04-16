#!/usr/bin/python3
"""
    Using a REST API, for a given employee ID,
    returns information about his/her
"""


import requests
from sys import argv


def get_todo_list(user_name):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, params={"userId": argv[1]})

    if (response.ok):
        EMPLOYEE_NAME = user_name
        todo_data = response.json()
        TOTAL_NUMBER_OF_TASKS = len(todo_data)
        NUMBER_OF_DONE_TASKS = sum(
            1 for task in todo_data if task['completed'])
        print("Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME,
            NUMBER_OF_DONE_TASKS,
            TOTAL_NUMBER_OF_TASKS
        ))
        for task in todo_data:
            if (task['completed']):
                print(f"\t {task['title']}")
    else:
        response.raise_for_status()


def setup():
    api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    response = requests.get(api_url)
    if (response.ok):
        user_data = response.json()
        get_todo_list(user_data['name'])
    else:
        response.raise_for_status()


if (__name__ == "__main__"):
    setup()
