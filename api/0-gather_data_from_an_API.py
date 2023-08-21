#!/usr/bin/python3
"""Task 0"""

from sys import argv
import requests

if __name__ == '__main__':
    text = 'Employee {} is done with tasks({}/{}):'
    id_ = int(argv[1])  # para el ID
    todos_ = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(id_)).json()
    users_ = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_)).json()
    num_of_done_tasks = 0
    total_tasks = 0
    for id1 in todos_:
        if id1['userId'] == id_:
            total_tasks += 1
        if id1['userId'] == id_ and id1['completed'] is True:
            num_of_done_tasks += 1

    print(text.format(users_['name'], num_of_done_tasks, total_tasks))

    for id1 in todos_:
        if id1['userId'] == id_ and id1['completed'] is True:
            print('\t {}'.format(id1['title']))
