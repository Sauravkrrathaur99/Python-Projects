import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "http://localhost:8000/"
