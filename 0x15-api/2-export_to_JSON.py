#!/usr/bin/python3
"""Information about his/her TODO list progress."""

if __name__ == "__main__":
    import json
    import requests
    import sys

    user_query = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    )
    query = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"
    )
    user_data = user_query.json()
    data = query.json()

    user_name = user_data.get("name")
    comp_tasks = list(filter(lambda task: task.get("completed"), data))

    all_tasks_number = len(data)
    comp_tasks_number = len(comp_tasks)

    # Export to json
    with open(f"{sys.argv[1]}.json", 'w', encoding='UTF8') as f:
        json_data = {
            sys.argv[1]: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_data.get("username")
                }
                for task in data
            ]
        }
        json.dump(json_data, f)
