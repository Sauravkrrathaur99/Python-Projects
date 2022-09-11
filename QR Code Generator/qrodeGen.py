import qrcode as qr

img = qr.make("https://sauravkrrathaur99.github.io/profile.iamsaurav_kumar_rathaur/")
img.save("generatedQr.png")