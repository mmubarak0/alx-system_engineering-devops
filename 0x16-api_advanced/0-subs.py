#!/usr/bin/env python3
"""Return number of subcribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Find number of subcribers."""
    with requests.Session() as s:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        try:
            sub = s.get(url).json()
            subscribers = sub["data"]["subscribers"]
        except Exception:
            return 0
        return subscribers
