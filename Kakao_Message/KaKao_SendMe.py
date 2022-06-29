import requests
import json
from PIL import Image

#1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","r") as fp:
#     tokens = json.load(fp)

#2.
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}
with open('./../QRCode/imageURL.txt', 'r') as tx:
    img = tx.read()


data={
    "template_object": json.dumps({
        "object_type": "feed",
        "content": {
            "title": "요청사항",
            "description": "우리 애가 먹을건데 탕수육 조금만 넣어주세요^^",
            "image_url": 'https://postfiles.pstatic.net/MjAyMjA2MjhfMTkw/MDAxNjU2NDIxMzg5ODc3.gJCFjuWSfl65BWqXi_SuZ9Rx8wO4h4Hr2Bv84XU4PoIg.HAIGjElsXQYNvRnlcLeukAVmAK4RLrRdprNm7-dLlF8g.PNG.e990727/QRCode.png?type=w966', #스테이크 //qr코드
            "image_width": 640,
            "image_height": 640,
            "link": {
                "web_url": "http://www.daum.net",
                "mobile_web_url": "http://m.daum.net",
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
        },
        "item_content" : {
            "profile_text" :"가게이름",
            "profile_image_url" :"https://www.urbanbrush.net/web/wp-content/uploads/edd/2018/09/urbanbrush-20180918002417018176.png", #치즈 //가게 로고
            "title_image_url" : "https://pbs.twimg.com/media/FGP7oInVcAQOvUx?format=jpg&name=900x900", #국밥 //메뉴사진
            "title_image_text" :"메뉴1",
            "title_image_category" : "얼큰한 국밥",
            "items" : [
                {
                    "item" :"추가메뉴1",
                    "item_op" : "1000원"
                },
                {
                    "item" :"추가메뉴2",
                    "item_op" : "2000원"
                },
                {
                    "item" :"추가메뉴3",
                    "item_op" : "3000원"
                },
                {
                    "item" :"추가메뉴4",
                    "item_op" : "4000원"
                },
                {
                    "item" :"추가메뉴5",
                    "item_op" : "5000원"
                }
            ],
            "sum" :"Total",
            "sum_op" : "15000원"
        },
        "social": {
            "like_count": 100,
            "comment_count": 200,
            "shared_count": 300,
            "view_count": 400,
            "subscriber_count": 500
        },
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net"
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
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code