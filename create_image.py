import PIL.Image, PIL.ImageDraw, PIL.ImageFont

def create_image(text):
    img = PIL.Image.new('RGB', (800, 400), color=(255, 255, 255))
    d = PIL.ImageDraw.Draw(img)
    font = PIL.ImageFont.load_default()
    d.text((10, 10), text, fill=(0, 0, 0), font=font)
    img.save('output_image.png')

# I tryed to learn how to create img by text, I need more time to create this.