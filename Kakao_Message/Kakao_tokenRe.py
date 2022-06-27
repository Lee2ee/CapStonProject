import time
import requests
import json

#code url  https://kauth.kakao.com/oauth/authorize?client_id=473cfccae3abe1b71befc4ea36e69287&redirect_uri=https://localhost:3000&response_type=code&scope=talk_message
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '473cfccae3abe1b71befc4ea36e69287'
redirect_uri = 'https://localhost:3000'
authorize_code = 'fK43lD3ATeT4g3wl_60gP-DZrYjLFtSoX3Xrp2-WvkLtpF2___Rf5K6xxMiVjXTviZOnaQo9dZsAAAGBpXLZ-A'


def f_auth():
    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    r_token = ts["refresh_token"]
    return r_token


def f_auth_refresh(r_token):
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    data = {
        "grant_type": "refresh_token",
        "client_id": rest_api_key,
        "refresh_token": r_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    with open(r"kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    token = ts["access_token"]
    return token


def f_send_talk(token, text):
    header = {'Authorization': 'Bearer ' + token}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    post = {
        'object_type': 'feed',
        'description' : 'QRCode',
        'image_url' : '../../QRCode/QRCode.png',
        'image_width' : 640,
        'image_height' : 640,
        'text': text,
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "https://www.jvision.ac.kr/vision/main/",
                    "mobile_web_url": "https://www.jvision.ac.kr/vision/main/"
                }
            },
            {
                "title": "앱으로 이동",
                "link": {
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            }
        ]
    }
    data = {'template_object': json.dumps(post)}
    return requests.post(url, headers=header, data=data)


r_token = f_auth()


while True:
    token = f_auth_refresh(r_token)
    f_send_talk (token, '보낼 메시지')
    time.sleep(1800)