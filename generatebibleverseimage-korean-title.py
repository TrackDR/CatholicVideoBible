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

filename = "Genesis-1-1-insta-title-kr.jpg"
imgwidth = instawidth
imgheight = instaheight

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('Arial Unicode MS.ttf', size=80)

text = "But that the works of thy wisdom might not be idle: therefore men \
also trust their lives even to a little wood, and passing over the sea \
by ship, are saved."

text = "And from the beginning also, when the proud giants perished, the \
hope of the world fleeing to a vessel, which was governed by thy hand, \
left to the world seed of generation."

text = "For blessed is the wood, by which justice cometh"

title = "Wisdom 14:7"

text = u"태초에 하나님이 천지를 창조하시니라 !"
#text.encode("utf-8")

title = u"창세기 1:1"

instanumchars = 18
videonumchars = 40
lines = textwrap.wrap(text, width=instanumchars)
lenlines = len(lines) + 2
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

linewidth, lineheight = font.getsize(title)
y_text += lineheight
canvas.text(((imgwidth - linewidth) / 2, y_text), title, font=font, fill=(255, 255, 255))

img.save(filename)

os.system(filename)
