#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. If an invalid subreddit is given, prints None.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        Titles of the first 10 hot posts, or None if the subreddit is invalid.
    """
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
            v1.0.0 (by /u/Unfair-Listen1740)"
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for i, post in enumerate(posts[:10]):
            print(post.get("data", {}).get("title", ""))
    else:
        print(None)
