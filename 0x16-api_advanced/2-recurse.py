#!/usr/bin/python3
"""Recrusive function."""
import requests


def recurse(subreddit, hot_list=[]):
    """Hot subreddits."""
    if len(hot_list) == 10:
        return hot_list
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
        "Safari/537.36 Edg/120.0.0.0"
    }
    with requests.Session() as s:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        try:
            sub = s.get(url, headers=headers).json()
            hotest = sub["data"]["children"][len(hot_list)]
        except Exception:
            return None
        hot_list.append(hotest["data"]["title"])
    return recurse(subreddit, hot_list)
