#!/usr/bin/python3
"""
Queries the Reddit API and recursively retrieves all hot article titles
for a given subreddit. If no results are found for the given subreddit,
the function returns None.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive function to get all hot article titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store the titles of the hot articles.
        after (str): The ID of the last article from the previous response
                     for pagination.

    Returns:
        list: A list of titles of all hot articles for the subreddit, or None
              if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    headers = {
        "User-Agent": "0x16-api_advanced:project:\
            v1.0.0 (by /u/Unfair-Listen1740)"
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        return hot_list if hot_list else None

    titles = [
        post.get("data", {}).get("title", "") for post in children
    ]
    hot_list.extend(titles)

    next_after = data.get("after")
    if next_after:
        return recurse(subreddit, hot_list, next_after)

    return hot_list
