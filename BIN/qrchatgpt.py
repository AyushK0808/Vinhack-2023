import qrtools

qr = qrtools.QRTool()

# read QR code from an image file
qr.decode("qrcode.jpg")
print(qr.data)

# or decode QR code from a webcam
qr.decode_webcam()
print(qr.data)
