import qrcode

url = input("Enter the URL you want to encode: ").strip()
file_path = "C:\\Users\\s antony vivin\\Desktop\\qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)


print(f"QR code saved to {file_path}")