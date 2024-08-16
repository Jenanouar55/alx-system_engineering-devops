#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': (
            '0x16-api_advanced:project:v1.0.0 (by /u/Putrid-Search-6501)'
        )
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return 0
        response.raise_for_status()
        data = response.json()
        subs = data.get("data", {}).get("subscribers", 0)
        return subs
    except (requests.RequestException, ValueError):
        return 0
