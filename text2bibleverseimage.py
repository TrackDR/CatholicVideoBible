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

basename = "Wisdom6-12-16"
basename = "1Cor15-28"
infilename = basename + ".txt"
filename = basename + ".jpg"
imgwidth = instawidth
imgheight = instaheight

fgcolor = (0,0,0)
#fgcolor = (255,255,255)
fgcolor = (0,0,139)
img = Image.new('RGB', (imgwidth,imgheight), color=fgcolor)

canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', size=50)
font = ImageFont.truetype('arial.ttf', size=45)

with open(infilename) as f:
    flines = [line.rstrip() for line in f]
    
lines = [i for i in flines if i] 
    
maxcharline = max(lines, key = len)
lenmaxcharline = len(maxcharline)

instanumchars = 45
instanumchars = 50
videonumchars = 40
#lines = textwrap.wrap(text, width=instanumchars)
lenlines = len(lines)
linewidth, lineheight = font.getsize(maxcharline)
totallinesheight = lenlines * lineheight
hstart = imgheight/2 - totallinesheight/2

maxlinewidth = 0
maxlineheight = 0
linespace = 5

totallinesheight = 0
for verse in lines:
    vlines = textwrap.wrap(verse, width=instanumchars)
    for line in vlines:
        linewidth, lineheight = font.getsize(line)
        if linewidth > maxlinewidth:
            maxlinewidth = linewidth
        if lineheight > maxlineheight:
            maxlineheight = lineheight
        totallinesheight += lineheight
        totallinesheight += linespace

bgcolor = (255,255,255)
#bgcolor = (255,20,147)
hstart = imgheight/2 - totallinesheight/2
y_text = hstart
for verse in lines:
    vlines = textwrap.wrap(verse, width=instanumchars)
    for line in vlines:
        linewidth, lineheight = font.getsize(line)
        if linewidth > maxlinewidth:
            maxlinewidth = linewidth
        if lineheight > maxlineheight:
            maxlineheight = lineheight
        #canvas.text(((imgwidth - linewidth) / 2, y_text), line, font=font, fill=(255, 255, 255))
        canvas.text((10, y_text), line, font=font, fill=bgcolor)
        y_text += lineheight
        y_text += linespace

img.save(filename)

os.system(filename)
