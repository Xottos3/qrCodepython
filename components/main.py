import qrcode

# Define the link you want the QR code to point to
link = "https://www.example.com"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 to 40, higher means bigger)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each "box" in the QR code
    border=4,  # Size of the border around the QR code
)
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code instance
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_img.save("qrcode.png")
