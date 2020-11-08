from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

twitterwidth = 1024
twitterheight = 512

filename = "Wisdom13-13.jpg"
imgwidth = 1080
imgheight = 1080

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', size=80)

#text_width, text_height = canvas.textsize('Hello World', font=font)

text = "Wisdom 13:10. But unhappy are they, and their hope is among the dead, who have \
called gods the works of the hand of men, gold and silver, the \
inventions of art, and the resemblances of beasts, or an unprofitable \
stone the work of an ancient hand."

text = "Wisdom 13:11. Or if an artist, a carpenter, hath cut down a tree proper for his \
use in the wood, and skilfully taken off all the bark thereof, and with \
his art, diligently formeth a vessel profitable for the common uses of \
life," 

text = "Wisdom 13:12. And useth the chips of his work to dress his meat:"

text = "Wisdom 13:13. And taking what was left thereof, which is good for nothing, \
being a crooked piece of wood, and full of knots, carveth it diligently \
when he hath nothing else to do, and by the skill of his art fashioneth \
it, and maketh it like the image of a man:"

lines = textwrap.wrap(text, width=28)
lenlines = len(lines)
linewidth, lineheight = font.getsize(lines[0])
totallinesheight = lenlines * lineheight
hstart = imgheight/2 - totallinesheight/2

maxlinewidth = 0
maxlineheight = 0

y_text = hstart
for line in lines:
    linewidth, lineheight = font.getsize(line)
    if linewidth > maxlinewidth:
        maxlinewidth = linewidth
    if lineheight > maxlineheight:
        maxlineheight = lineheight
    canvas.text(((imgwidth - linewidth) / 2, y_text), line, font=font, fill=(255, 255, 255))
    y_text += lineheight

img.save(filename)

os.system(filename)
