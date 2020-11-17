# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:53:15 2020

@author: jerem
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import budou

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

twitterwidth = 1024
twitterheight = 512
instawidth = 1080
instaheight = 1080
videowidth = 1920
videoheight = 1080

filename = "Genesis-1-1-insta-title-jp.jpg"
imgwidth = instawidth
imgheight = instaheight
instanumchars = 28
videonumchars = 40

img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
canvas = ImageDraw.Draw(img)

font = ImageFont.truetype('Arial Unicode MS.ttf', size=80)

text = u"初めに、神は天地を創造された。"
#text.encode("utf-8")

title = "創世記/ 01章 01節"

parser = budou.get_parser('tinysegmenter')
results = parser.parse('初めに、神は天地を創造された。')
#print(results['html_code'])

linelen = 0
lines = []
i = 0
lines.append("")
for chunk in results['chunks']:
  print(chunk.word)
  
  linelen = len(lines[i])*2
  if (len(chunk.word)*2+linelen) < instanumchars:
     lines[i] = lines[i] + chunk.word
  else:
     lines.append(chunk.word)

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

