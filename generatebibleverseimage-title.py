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

Book = "Wisdom"
Chapter = "14"
Verse = "13"

filename = "Wisdom14-12-insta-title.jpg"
filename = Book + Chapter + "-" + Verse + "-insta-title.jpg"

imgwidth = instawidth
imgheight = instaheight

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', size=80)

text = "And from the beginning also, when the proud giants perished, the \
hope of the world fleeing to a vessel, which was governed by thy hand, \
left to the world seed of generation."

text = "For the beginning of fornication is the devising of idols: and \
the invention of them is the corruption of life."

#text = "For neither were they from the beginning, neither shall they be for ever."

basedirectory = r"E:\Religious\BooksWithVideoOrig\BooksWithVideo\BooksWithVideo\newchps"
filename2read = os.path.join(basedirectory,Book + "_" + Chapter + "aarm.txt")
with open(filename2read, 'rt') as f:
    data = f.readlines()
for line in data:
    if line.__contains__(Chapter + ":" + Verse):
        print(line)
        line = line.split(None, 1)[-1]
        print(line)
        text  = line

title = "Wisdom 14:12"
title = Book + " " + Chapter + ":" + Verse

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
