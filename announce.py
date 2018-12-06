from PIL import Image, ImageDraw, ImageFont

transparent = (255, 255, 255, 0)
black = (0, 0, 0, 255)


def generate(line1, line2):
    base = Image.open('./work/blank.png').convert('RGBA')
    txt = Image.new('RGBA', base.size, transparent)
    fnt = ImageFont.truetype(
        './work/UtsukushiMincho-FONT/UtsukushiFONT.otf', 80)
    d = ImageDraw.Draw(txt)
    d.text((125, 60), line1, font=fnt, fill=black)
    d.text((130, 140), line2, font=fnt, fill=black)
    rot = txt.rotate(3, resample=Image.BILINEAR)
    return Image.alpha_composite(base, rot)


def main():
    import sys
    img = generate(*sys.argv[1])
    img.show()


if __name__ == '__main__':
    main()