# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:53:15 2020

@author: jerem
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import numpy as np


def writebiblejpg(basename,imgwidth,imgheight,lines,Book,Chapter,verses,numchars,imgtag,fontsize):
    outfilename = basename + imgtag + ".txt"
    filename = basename + imgtag + ".jpg"
    
    fgcolor = (0,0,0)
    fgcolor = (255,255,255)
    fgcolor = (0,0,139)
    #fgcolor = (255,20,147)
    #fgcolor = (1,68,38)
    #fgcolor = (0,77,35)
    #fgcolor = (9, 36, 9)
    #fgcolor = (61, 61, 61)
    img = Image.new('RGB', (imgwidth,imgheight), color=fgcolor)
    
    canvas = ImageDraw.Draw(img)
    
    font = ImageFont.truetype('arial.ttf', size=50)
    font = ImageFont.truetype('arial.ttf', size=45)
    font = ImageFont.truetype('arial.ttf', size=fontsize)
    
    #with open(infilename) as f:
    #    flines = [line.rstrip() for line in f]
        
    for line in lines:
        flines = [line.rstrip() for line in lines]
    
    lines = [i for i in flines if i] 
        
    maxcharline = max(lines, key = len)
    lenmaxcharline = len(maxcharline)
    
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
        vlines = textwrap.wrap(verse, width=numchars)
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
        vlines = textwrap.wrap(verse, width=numchars)
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

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

twitterwidth = 1024
twitterheight = 512
instawidth = 1080
instaheight = 1080
videowidth = 1920
videoheight = 1080
instanumchars = 45
instanumchars = 50
videonumchars = 40


with open('abbreviations.txt') as f:
  d = dict(x.rstrip().split(',') for x in f)

#
bcvinput = ""
bcvinput = ""
bcvinput = ""
bcvinput = ""
bcvinput = ""

# 4th  Sunday Ordinary Time
bcvinput = "Dt 18:15-20"
bcvinput = "Ps 95:1-2, 6-9"
bcvinput = "1 Cor 7:32-35"
bcvinput = "Mt 4:16"
bcvinput = "Mk 1:21-28"

# 3rd Sunday Ordinary Time
bcvinput = "Jon 3:1-5, 10"
bcvinput = "Ps 25:4-9"
bcvinput = "1 Cor 7:29-31"
bcvinput = "Mk 1:15"
bcvinput = "Mk 1:14-20"

# 2nd Sunday Ordinary Time
bcvinput = "1 Sm 3:3b-10, 19"
bcvinput = "Ps 2,7-10"
bcvinput = "1 Cor 6:13c-15a, 17-20"
bcvinput = "Jn 1:41, 17b"
bcvinput = "Jn 1:35-42"

# The Baptism of the Lord
bcvinput = "Is 42:1-4, 6-7"
bcvinput = "Is 55:1-11"
bcvinput = "Ps 29:1-2, 3-4, 3, 9-10, 11b"
bcvinput = "Is 12:2-3, 4bcd, 5-6"
bcvinput = "Acts 10:34-38"
bcvinput = "1Jn 5:1-9"
bcvinput = "Jn 1:29"
bcvinput = "Mk 1:7-11"

# The Epiphany of the Lord
bcvinput = "Is 60:1-6"
bcvinput = "Ps 72:1-2, 7-8, 10-11, 12-13"
bcvinput = "Eph 3:2-3a, 5-6"
bcvinput = "Mt 2:2"
bcvinput = "Mt 2:1-12"

# Solemnity of Mary, Mother of God
bcvinput = "Nm 6:22-27"
bcvinput = "Ps 67:2-3,5,6,8"
bcvinput = "Gal 4:4-7"
bcvinput = "Heb 1:1-2"
bcvinput = "Lk 2:16-21"

# Christmas Vigil Mass
bcvinput = "Is 62:1-5"
bcvinput = "Ps 89:2a, 4-5, 16-17, 27, 29"
bcvinput = "Acts 13:16-17, 22-25"
bcvinput = ""
bcvinput = "Mt 1:1-25"

# 4th Sunday Advent
bcvinput = "2 Sm 7:1-5, 8B-12, 14A, 16"
bcvinput = "Ps 89:2-5, 27, 29"
bcvinput = "Rom 16:25-27"
bcvinput = "Lk 1:38"
bcvinput = "Lk 1:26-38"

# 3rd Sunday Advent
bcvinput = "Is 61:1-2A, 10-11"
bcvinput = "Lk 1:46-50, 53-54"
bcvinput = "1 Thes 5:16-24"
bcvinput = "Is 61:1"
bcvinput = "Jn 1:6-8, 19-28"

# 2nd Sunday Advent
bcvinput = "Is 40:1-5,9-11"
bcvinput = "Ps 84:8,9-14"
#bcvinput = "2 Pt 3:8-14"
#bcvinput = "Lk 3:4,6"
#bcvinput = "Mk 1:1-8"

verses = bcvinput.split(":")[-1]
bkch = bcvinput.split(":")[0:-1][0]
chp = bkch.split()[-1]
bk = bkch.split()[0:-1]
bk = " ".join(bk)
Book = d[bk]

splitverses = verses.replace(" ", "").split(",")
lensplitverses = len(splitverses)
verselinenums = np.array((0),int)
print("verses:",verselinenums)
for splitverse in splitverses:
    print(splitverse)
    moreverses = splitverse.split('-')
    print(moreverses)
    if len(moreverses) == 1:
        verselinenums=np.append(verselinenums, int(moreverses[0]))
    else:
        firstverse = moreverses[0]
        lastverse = moreverses[1]
        for i in range(int(firstverse),int(lastverse)+1):
            verselinenums=np.append(verselinenums, i)
            
print("verses:",verselinenums)
verselinenums = np.unique(verselinenums)
print("verses:",verselinenums)
verselinenums = np.delete(verselinenums, 0, 0)
print("verses:",verselinenums)
lenverses = len(verselinenums)

              
Chapter = chp
basedirectory = r"E:\Religious\BooksWithVideoOrig\BooksWithVideo\BooksWithVideo\newchps"
filename2read = os.path.join(basedirectory,Book + "_" + Chapter + "aarm.txt")
with open(filename2read, 'rt') as f:
    data = f.readlines()

basenamebkch = Book + Chapter
basename = basenamebkch
verselines = []
for i in verselinenums:
    Verse = str(i)
    print(Verse)
    basename += "-"
    basename += Verse
    
    for line in data:
        if line.__contains__(Chapter + ":" + Verse + '.'):
            print(line)
            #line = line.split(None, 1)[-1]
            verselines.append(line)
            
print(basename)
print(basenamebkch)

#basename = "Wisdom6-12-16"
#basename = "1Cor15-28"
#basename = "Ez34-11-12--15-17"
#basename = "Psalm22"

instanumverses2write = 8
instastorynumverses2write = 5
twitternumverses2write = 5

instanumchars = 45
instanumchars = 50
videonumchars = 40

twitterwidth = 1024
twitterheight = 512
instawidth = 1080
instaheight = 1080
instastorywidth = 1080
instastoryheight = 1920
videowidth = 1920
videoheight = 1080

instanumchars = 50
instastorynumchars = 27
videonumchars = 40
twitternumchars = 40

instafontsize = 45
instastoryfontsize = 80
twitterfontsize = 50

imgtag = imgtag = "-twitter-title"
numverses2write = twitternumverses2write
imgwidth = twitterwidth
imgheight = twitterheight
fontsize = twitterfontsize
numchars = twitternumchars

imgtag = imgtag = "-insta-title"
numverses2write = instanumverses2write
imgwidth = instawidth
imgheight = instaheight
fontsize = instafontsize
numchars = instanumchars

# imgtag = imgtag = "-insta-title-story"
# numverses2write = instastorynumverses2write
# imgwidth = instastorywidth
# imgheight = instastoryheight
# fontsize = instastoryfontsize
# numchars = instastorynumchars

with open(basename + '.txt', 'w') as f:
    f.write(Book.replace("_"," ") + " Chapter " + Chapter + ":" + verses + "\n")
    for line in verselines:
        f.write(line)

lines = [Book.replace("_"," ") + " Chapter " + Chapter + ":" + verses]
firstverseidx = 0
basename = basenamebkch
# subtract 1 for first page since one line will be the title
for i in range(firstverseidx,firstverseidx+numverses2write-1):
    if i < lenverses:
        
        basename += "-"
        Verse = verselinenums[i]
        basename += str(Verse)
        lines.append(verselines[i])
print(basename)
writebiblejpg(basename,imgwidth,imgheight,lines,Book,Chapter,verses,numchars,imgtag,fontsize)

firstverseidx = firstverseidx + numverses2write - 1
while firstverseidx < lenverses:
    basename = basenamebkch
    lines = []
    for i in range(firstverseidx,firstverseidx+numverses2write):
        if i < lenverses:
            basename += "-"
            Verse = verselinenums[i]
            basename += str(Verse)
            lines.append(verselines[i])
    print(basename)
    firstverseidx = firstverseidx + numverses2write
    writebiblejpg(basename,imgwidth,imgheight,lines,Book,Chapter,verses,numchars,imgtag,fontsize)

