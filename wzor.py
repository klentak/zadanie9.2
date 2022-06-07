from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/UG_encode.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            pass #TUTAJ należy uzupełnić funkcjonalność

    decoded_image.save("images/UG_decode.png")

def write_text(text_to_write, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode, template_image="images/UG.jpg"):
    pass #UZUPEŁNIJ TĘ FUNKCJĘ

if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()

    print("Encoding the image...")
    encode_image()