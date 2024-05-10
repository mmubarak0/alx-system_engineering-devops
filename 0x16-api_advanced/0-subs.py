#!/usr/bin/python3
"""Return number of subcribers of a subreddit."""
import requests
import requests.auth


def number_of_subscribers(subreddit):
    """Find number of subcribers."""
    headers = {
            "User-Agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
        }
    auth = requests.auth.HTTPBasicAuth(
            'p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI'
        )
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(
                url, headers=headers, allow_redirects=False, auth=auth
            )
    if response.status_code >= 300:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    return 0
