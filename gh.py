import requests
import base64
import json
import github3
from github import Github


def getter():
    url = "https://raw.githubusercontent.com/SupremeCoder1707/Game/main/score.json"
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        """first_content = base64.b64decode(req['content'])
        second_content = first_content.decode('ascii')
        jsonstring = json.dumps(second_content)"""
        with open("score.json", "w") as f:
            json.dump(req, f, indent=4)
    else:
        print("Content not found")


def setter():
    g = Github("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")
    repo = g.get_repo("SupremeCoder1707/Game")
    contents = repo.get_contents("score.json")
    with open("score.json", "r") as f:
        file = json.load(f)
    file_string = json.dumps(file)

    repo.update_file(contents.path, "Uploading updated scores.", file_string, contents.sha, branch="main")

