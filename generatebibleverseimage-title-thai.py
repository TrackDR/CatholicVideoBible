# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:53:15 2020

@author: jerem
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
from pythainlp import word_tokenize

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

twitterwidth = 1024
twitterheight = 512
instawidth = 1080
instaheight = 1080
videowidth = 1920
videoheight = 1080

filename = "Genesis1-1-insta-title-thai.jpg"
imgwidth = instawidth
imgheight = instaheight

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('Arial Unicode MS.ttf', size=80)

origtext = u"ในปฐมกาล พระเจ้าทรงสร้างทุกสิ่งในฟ้าสวรรค์และโลก"
wordlist = word_tokenize(origtext, keep_whitespace=False)
text = ' '.join(wordlist)
print("".join(text.split()))

title = u"ในปฐมกาล 1:1"

instanumchars = 28
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
    line = "".join(line.split())
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
