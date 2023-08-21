#!/usr/bin/python3
"""Task 2"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    users = 'https://jsonplaceholder.typicode.com/users/{}'
    id_ = int(argv[1])  # para el ID
    todo_ = requests.get(todos.format(id_)).json()
    user_ = requests.get(users.format(id_)).json()

    with open('{}.json'.format(id_), 'w') as file:
        lista = []
        for id1 in todo_:
            if id1['userId'] == id_:
                lista.append({"task": id1["title"],
                             "completed": id1["completed"],
                              "username": user_["username"]})
        json.dump({'{}'.format(id_): lista}, file)
