# import base64
# import io
# from PIL import Image
#
#
# def pillow_image_to_base64_string(img):
#     buffered = io.BytesIO()
#     img.save(buffered, format="png")
#     return base64.b64encode(buffered.getvalue()).decode("utf-8")
#
#
# def base64_string_to_pillow_image(base64_str):
#     return Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))
#
#
# # Example for Converting pillow image to base64 data URL to view in browser
# my_img = Image.open('QRCode.png')
# data_url = 'data:image/png;base64,' + pillow_image_to_base64_string(my_img)
# # You can put this data URL in the address bar of your browser to view the image
#
# with open("imageURL.txt", "w") as tx:
#     tx.write(data_url)
# print(data_url)

import urllib.request

#python 3
urllib.request.urlretrieve('http://www.daum.net', './../QRCode/QRCode.png')