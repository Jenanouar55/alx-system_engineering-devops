#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers(not active
users, total subscribers) for a given subreddit. if an invalid subreddit
is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/Unfair-Listen1740)"
        }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    sub = response.json().get("data").get("subscribers")
    return sub
