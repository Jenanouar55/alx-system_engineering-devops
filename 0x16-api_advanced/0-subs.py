#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given the function returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers for the subreddit, or 0 if is invalid.
    """
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
            v1.0.0 (by /u/Unfair-Listen1740)"
          }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)

    return 0
