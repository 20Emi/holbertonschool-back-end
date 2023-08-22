#!/usr/bin/python3
"""Task 2"""

import json
import requests


if __name__ == '__main__':
    todos = 'https://jsonplaceholder.typicode.com/todos'
    users = 'https://jsonplaceholder.typicode.com/users'
    todo_ = requests.get(todos).json()
    user_ = requests.get(users).json()
    with open('todo_all_employees.json', 'w') as file:
        lista = []
        dict_ = {}
        for key in user_:
            id_ = key['id']
            for value in todo_:
                if value['userId'] == id_:
                    lista.append({"task": value["title"],
                                  "completed": value["completed"],
                                  "username": key["username"]})
            dict_[id_] = lista
            lista = []  # se vuelve a reniciar
        json.dump(dict_, file)
