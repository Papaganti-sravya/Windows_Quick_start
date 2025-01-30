import qrcode
import os 

def generate_qr_code(file_path, output_image="output_qr.png"):
    # Encode the file path (or a URL pointing to the file)
    data = f"file://{os.path.abspath(file_path)}"

    # Generate a QR code from the data
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_image)
    print(f"QR code saved to: {output_image}")
