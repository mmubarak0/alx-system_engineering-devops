#!/usr/bin/python3
"""Return number of subcribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Find number of subcribers."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
        "Safari/537.36 Edg/120.0.0.0"
    }
    with requests.Session() as s:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        sub = s.get(url, headers=headers, allow_redirects=False)
        if sub.status_code >= 300:
            return 0
        subscribers = sub.json()["data"]["subscribers"]
        return subscribers
