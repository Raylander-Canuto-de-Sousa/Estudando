import qrcode
image_qrcode = qrcode.make("https://www.google.com/")

image_qrcode.save("qrcode_python.jpg")