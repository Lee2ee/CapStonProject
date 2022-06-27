import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '473cfccae3abe1b71befc4ea36e69287'
redirect_uri = 'https://localhost:3000'
authorize_code = 'gzGk_01ncbDkATYHUIVlgFk0RTSxWyh5UN-V4_Vp11Qlc74oyJ0L-wKifCHxrO4dygi34wo9c00AAAGBo5mDbA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)