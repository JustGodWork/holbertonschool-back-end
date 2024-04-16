#!/usr/bin/python3
"""
    Using a REST API, for a given employee ID,
    returns information about his/her in CSV format
"""


import csv
import requests
from sys import argv


def get_todo_list():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url, params={"userId": argv[1]})

    if (response.ok):
        todo_data = response.json()
        with open(f"{argv[1]}.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todo_data:
                csv_writer.writerow([
                    argv[1],
                    EMPLOYEE_NAME,
                    task.get('completed'),
                    task.get('title')
                ])
    else:
        response.raise_for_status()


def setup():
    api_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    response = requests.get(api_url)
    if (response.ok):
        user_data = response.json()
        global EMPLOYEE_NAME
        EMPLOYEE_NAME = user_data.get('name')
    else:
        response.raise_for_status()

    get_todo_list()


if (__name__ == "__main__"):
    setup()
