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

    # Export to csv
    with open(f"{sys.argv[1]}.csv", 'w', encoding='UTF8') as f:
        csv_data = [
            ",".join([
                f'"{sys.argv[1]}"', f'"{user_data.get("username")}"',
                f'"{task.get("completed")}"', f'"{task.get("title")}"'
            ])
            for task in data
        ]
        for line in csv_data:
            f.write(f"{line}\n")
