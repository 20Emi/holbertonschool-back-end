#!/usr/bin/python3
"""Task 1"""

import requests
from sys import argv

if __name__ == '__main__':
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    users = 'https://jsonplaceholder.typicode.com/users/{}'
    text = 'Employee {} is done with tasks({}/{}):'
    id_ = int(argv[1])  # para el ID
    todo_ = requests.get(todos.format(id_)).json()
    user_ = requests.get(users.format(id_)).json()
    with open('{}.csv'.format(id_), 'w') as file:
        for id1 in todo_:
            if id1['userId'] == id_:
                file.write('"{}","{}","{}","{}"\n'.format(
                    id_, user_['username'], id1['completed'], id1['title']))
