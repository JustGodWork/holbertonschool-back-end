#!/usr/bin/python3
"""
    Using a REST API, for a given employee ID,
    returns information about his/her in CSV format
"""


import csv
import json
import requests
from sys import argv


def get_todo_list(user_name):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, params={"userId": argv[1]})

    if (response.ok):
        EMPLOYEE_NAME = user_name
        todo_data = json.loads(response.content)
        tasks = []
        for task in todo_data:
            tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": EMPLOYEE_NAME
            })
        with open(f"{argv[1]}.json", "w") as json_file:
            json.dump({argv[1]: tasks}, json_file)
    else:
        response.raise_for_status()


def setup():
    api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    response = requests.get(api_url)
    if (response.ok):
        user_data = response.json()
        get_todo_list(user_data['username'])
    else:
        response.raise_for_status()


if (__name__ == "__main__"):
    setup()
