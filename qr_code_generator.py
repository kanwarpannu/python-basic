import qrcode

data = input ('Enter the text or a URL: ').strip()
filename = input('Enter the filename: ').strip()
default_location = 'output_image'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(default_location+'/'+filename)

print(f'QR code saved as {filename}')