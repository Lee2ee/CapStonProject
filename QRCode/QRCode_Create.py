import qrcode

img = qrcode.make("인증 되었습니다.")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=4,
    border=10,
)
qr.add_data(img)
qr.make(fit=True)
img.save("QRCode.png")
print(type(img))
print(img.size)