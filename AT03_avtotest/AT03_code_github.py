import requests
import config

# функци просмотра GitHub
def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None