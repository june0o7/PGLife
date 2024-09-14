from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    binary_data = ""

    for pixel in img.getdata():
        for channel in pixel:
            binary_data += str(channel & 1)

    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":  # End delimiter
            break

    print("Hidden Message:", decoded_data)

# Replace 'image.png' with your image file
extract_lsb('C:\xampp\htdocs\Module 6 assignment - complete solution\js\img.png')