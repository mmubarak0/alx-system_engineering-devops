#!/usr/bin/python3
"""List to 10 hot articles."""
import requests


def top_ten(subreddit):
    """Hot subreddits."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
        "Safari/537.36 Edg/120.0.0.0"
    }
    with requests.Session() as s:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        sub = s.get(url, headers=headers)
        if sub.status_code >= 300:
            print(None)
            return
        hotest = sub.json()["data"]["children"]
        for i in range(10):
            print(hotest[i]["data"]["title"])
