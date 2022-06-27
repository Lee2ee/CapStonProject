import json
import requests

# 카카오톡 메시지 API
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '473cfccae3abe1b71befc4ea36e69287'
redirect_uri = 'https://localhost:3000'
authorize_code = '9Hab50MNdGGC9QP4PDaEx7_l_NLCqU-nuB_xAeGmG__D0ftGjGo75CHJgvnZGNpQJ8yUKAopb9UAAAGBo5tL7A'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }


response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_firedsCode.json", "w") as fp:
    json.dump(tokens, fp)

# 카카오 API 엑세스 토큰
with open("kakao_firedsCode.json", "r") as fp:
    tokens = json.load(fp)

print(tokens["access_token"])