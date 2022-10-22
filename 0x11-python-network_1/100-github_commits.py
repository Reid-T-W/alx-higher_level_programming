#!/usr/bin/python3
"""
Gets the latest 10 github commits by a user rail
in the rail repository, sorted from most recent to
oldest
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    res = requests.get("https://api.github.com/repos/{}/{}/commits".
                       format(user, repo))
    commits = res.json()
    keys = ['sha', 'commit', 'author']
    sub_list = []
    sub_dict = {}
    for commit in commits[-10:]:
        sub_dict = {}
        sub_dict['sha'] = commit.get('sha')
        sub_dict['name'] = commit.get('commit').get('author').get('name')
        sub_dict['date'] = commit.get('commit').get('author').get('date')
        sub_list.append(sub_dict)
    # Sort based on date, latest to oldest
    sorted_list = sorted(sub_list, key=lambda x: x['date'], reverse=True)
    for item in sorted_list:
        print("{}: {}".format(item.get('sha'), item.get('name')))
