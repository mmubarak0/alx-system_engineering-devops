#!/usr/bin/python3
"""Information about his/her TODO list progress."""

if __name__ == "__main__":
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

    # Output
    print(
        f"Employee {user_name} is done with \
tasks({comp_tasks_number}/{all_tasks_number}):"
    )
    for task in comp_tasks:
        print(f"\t{task.get('title')}")
