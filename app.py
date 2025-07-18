from PIL import Image, ImageDraw, ImageFont

def get_base_img(color="FFFFFF", size=(300, 600)):
    rgb = tuple(int(color.upper()[i:i+2], 16) for i in (0, 2, 4))
    return Image.new("RGBA", size, rgb)

def draw_line(img, width, y):
    img_draw = ImageDraw.Draw(img)
    img_draw.line([(0, y), (width, y)], fill =(0, 0, 0), width = 0)
    return img

def draw_code(img, code, font, x, y):
    img_draw = ImageDraw.Draw(img)
    print(code)
    img_draw.text((x, y), code, fill=(0, 0, 0), font=font)
    return img

def create(filename, font_path):
    codes = open(filename).read().split("\n")[1:-1]

    padding = 20
    font_size = 32
    height = len(codes) * ((padding * 2) + font_size + padding)
    width = font_size * 16
    img = get_base_img(size=(width, height))

    font = ImageFont.truetype(font_path, font_size)

    position = 0
    for i in range(len(codes)):
        position += padding
        img = draw_code(img, codes[i], font , 70, position)
        position += font_size + (padding * 2)
        img = draw_line(img, width, position)
    img.show()
    img.save("codes.png")

create("codes.csv", "JetBrainsMono.ttf")
