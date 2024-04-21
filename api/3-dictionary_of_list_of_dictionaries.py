#!/usr/bin/python3
"""
    Using a REST API, for a given employee ID,
    returns information about his/her in CSV format
"""


import csv
import json
import requests
from sys import argv


def get_todo_list(users):
    users_data = {}
    for user in users:
        user_id = user['id']
        user_name = user['username']
        api_url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(api_url, params={"userId": user_id})
        todo_data = json.loads(response.content)
        users_data[user_id] = []
        for task in todo_data:
            users_data[user_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(users_data, json_file)


def setup():
    api_url = f"https://jsonplaceholder.typicode.com/users"

    response = requests.get(api_url)
    if (response.ok):
        users = response.json()
        get_todo_list(users)
    else:
        response.raise_for_status()


if (__name__ == "__main__"):
    setup()
