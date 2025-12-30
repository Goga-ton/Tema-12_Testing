import requests


# функци просмотра случайных фоток кошек
def get_catapi_pic():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    if res.status_code == 200:
        # print(res.json())
        return res.json()
    else:
        # print('error')
        return None

# get_catapi_pic()