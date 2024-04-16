#!/usr/bin/python3
"""
    Using a REST API, for a given employee ID,
    returns information about his/her
"""


import requests
from sys import argv
from typing import Any, Dict, List


def get_todo_list():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, params={"userId": argv[1]})

    if (response.ok):
        todo_data: List[Dict[str, Any]] = response.json()
        TOTAL_NUMBER_OF_TASKS = len(todo_data)
        NUMBER_OF_DONE_TASKS = sum(
            1 for task in todo_data if task.get('completed'))
        print(f"Employee {EMPLOYEE_NAME} is done with tasks( \
              {NUMBER_OF_DONE_TASKS}/ \
                {TOTAL_NUMBER_OF_TASKS})")
        for task in todo_data:
            if (task.get('completed')):
                print(f"\t {task.get('title')}")
    else:
        response.raise_for_status()


def setup():
    api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    response = requests.get(api_url)
    if (response.ok):
        user_data: Dict[str, Any] = response.json()
        global EMPLOYEE_NAME
        EMPLOYEE_NAME = user_data.get('name')
    else:
        response.raise_for_status()

    get_todo_list()


if (__name__ == "__main__"):
    setup()
