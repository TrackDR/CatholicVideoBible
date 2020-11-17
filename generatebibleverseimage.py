# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:53:15 2020

@author: jerem
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

twitterwidth = 1024
twitterheight = 512
instawidth = 1080
instaheight = 1080
videowidth = 1920
videoheight = 1080

filename = "Wisdom14-3-insta.jpg"
imgwidth = instawidth
imgheight = instaheight

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', size=80)

text = "Wisdom 13:15. And maketh a convenient dwelling place for it, and setting it in \
a wall, and fastening it with iron,"

text = "Wisdom 13:17. And then maketh prayer to it, enquiring concerning his substance, \
and his children, or his marriage.  And he is not ashamed to speak to \
that which hath no life:"

text = "Wisdom 13:18. And for health he maketh supplication to the weak, and for life \
prayeth to that which is dead, and for help calleth upon that which is \
unprofitable:"

text = "Wisdom 14:1. Again, another designing to sail, and beginning to make his voyage \
through the raging waves, calleth upon a piece of wood more frail than \
the wood that carrieth him."

text = "Wisdom 14:2. For this the desire of gain devised, and the workman built it by his skill."

text = "Wisdom 14:3. But thy providence, O Father, governeth it: for thou hast made a \
way even in the sea, and a most sure path among the waves,"

instanumchars = 28
videonumchars = 40
lines = textwrap.wrap(text, width=instanumchars)
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
