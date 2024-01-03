#!/usr/bin/python3
"""Information about his/her TODO list progress."""

if __name__ == "__main__":
    import json
    import requests

    user_query = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
    )
    query = requests.get(
        f"https://jsonplaceholder.typicode.com/todos"
    )
    user_data = user_query.json()
    data = query.json()

    # Export to json
    with open("todo_all_employees.json", 'w', encoding='UTF8') as f:
        json_data = {
            user.get('id'): [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                for task in list(
                    filter(
                        lambda task: task.get('userId') == user.get('id'), data
                    )
                )
            ]
            for user in user_data
        }
        json.dump(json_data, f)
