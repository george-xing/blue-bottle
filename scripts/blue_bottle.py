import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from datetime import datetime

def main():
    start = datetime(2014, 1, 11, 0, 0, 0)
    for i, filename in enumerate(sorted(os.listdir('.'))):
        font = ImageFont.truetype("../../scripts/Arial.ttf", 40)
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        timestamp = start + timedelta(0, 60) * i
        draw.text((500, 0), timestamp.strftime('%H:%M'), (204, 0, 0), font=font)
        draw = ImageDraw.Draw(img)
        img.save("%06d_new.jpg" % int(i+1))

if __name__ == "__main__":
    main()