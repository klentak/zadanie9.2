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
      pixels[i, j] = bin(red_channel.getpixel((i, j)))[-1] == '0' and (255, 255, 255) or (0, 0, 0)

  decoded_image.save("images/UG_decode.png")


def write_text(text_to_write, image_size):
  image_text = Image.new("RGB", image_size)
  font = ImageFont.load_default().font
  drawer = ImageDraw.Draw(image_text)

  margin = offset = 10
  for line in textwrap.wrap(text_to_write, width=60):
    drawer.text((margin, offset), line, font=font)
    offset += 10
  return image_text


def encode_image(text_to_encode, template_image="images/UG.jpg"):
  image = Image.open(template_image)
  red_temp, green_temp, blue_temp, _ = image.split()

  x_size, y_size = image.size

  image_with_text = write_text(text_to_encode, image.size)
  black_white_image = image_with_text.convert('1')

  encoded_image = Image.new("RGB", (x_size, y_size))
  pixels = encoded_image.load()
  for i in range(x_size):
    for j in range(y_size):
      red_temp_pix = bin(red_temp.getpixel((i, j)))
      black_white_temp_pix = bin(black_white_image.getpixel((i, j)))

      red_temp_pix = black_white_temp_pix[-1] == '1' \
         and red_temp_pix[:-1] + '1' \
         or red_temp_pix[:-1] + '0'

      pixels[i, j] = (int(red_temp_pix, 2), green_temp.getpixel((i, j)), blue_temp.getpixel((i, j)))

  encoded_image.save("images/encoded_image.png")


if __name__ == '__main__':
  print("Encoding the image...")
  encode_image("test", 'images/test.png')

  print("Decoding the image...")
  decode_image('images/encoded_image.png')
