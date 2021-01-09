from PIL import Image, ImageDraw


def encode(text, img_path):
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    if len(text) + 1 > width * height:
        raise ValueError('text is too long')
    pix = img.load()
    for i in enumerate(text):
        coords = (i[0] % width, i[0] // width)
        g, b = pix[coords][1:3]
        draw.point(coords, (ord(i[1]), abs(g-1), b))
    coords = (len(text) % width, len(text) // width)
    draw.point(coords, (255, 255, 255))
    img.save("encoded_img.png", "PNG")


def get_text(img_path):
    img = Image.open(img_path)
    width = img.size[0]
    answ = ''
    i = 0
    while True:
        coords = (i % width, i // width)
        r, g = img.getpixel(coords)[0:2]
        if g == 255:
            break
        answ += chr(r)
        i += 1
    return answ


path = "modern_house.png"
#encode('Hello, world!', path)
print(get_text('encoded_img.png'))
