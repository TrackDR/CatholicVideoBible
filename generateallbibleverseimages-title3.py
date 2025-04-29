from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def get_text_size(font, text):
    """
    Returns (width, height) of the given text using the specified font.
    """
    bbox = font.getbbox(text)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

# ideal image sizes from here: https://blog.hootsuite.com/social-media-image-sizes-guide/#instagram

def genbibleverseimage(Book,Chapter,Verse,imgwidth,imgheight,numchars,imgtag,fontsize,gentxt,basedirectory):
    
    #filename = "Wisdom14-12-insta-title.jpg"
    filename = Book + Chapter + "-" + Verse + imgtag + ".jpg"
    textfileout = Book + Chapter + "-" + Verse + imgtag + ".txt"
    
    #imgwidth = instawidth
    #imgheight = instaheight
    
    #img = Image.new('RGB', (imgwidth,imgheight), color=(0, 0, 0))
    #img = Image.new('RGB', (imgwidth,imgheight), color=(0,0,220))
    img = Image.new('RGB', (imgwidth,imgheight), color=(0,0,151))
    canvas = ImageDraw.Draw(img)
    
    font = ImageFont.truetype('arial.ttf', size=fontsize)
    
    text = "And from the beginning also, when the proud giants perished, the \
    hope of the world fleeing to a vessel, which was governed by thy hand, \
    left to the world seed of generation."
    
    text = "For the beginning of fornication is the devising of idols: and \
    the invention of them is the corruption of life."
    
    #text = "For neither were they from the beginning, neither shall they be for ever."
    
    #basedirectory = r"F:\Religious\BooksWithVideoOrig\BooksWithVideo\BooksWithVideo\newchps"
    filename2read = os.path.join(basedirectory,Book + "_" + Chapter + "aarm.txt")
    with open(filename2read, 'rt') as f:
        data = f.readlines()
    for line in data:
        if line.__contains__(Chapter + ":" + Verse + "."):
            print(line)
            line = line.split(None, 1)[-1]
            print(line)
            text  = line
    
    #title = "Wisdom 14:12"
    
    NewBook = Book.replace("_"," ")
    
    title = NewBook + " " + Chapter + ":" + Verse
    print(title)
    
    lines = textwrap.wrap(text, width=numchars)
    lenlines = len(lines) + 2
    #linewidth, lineheight = font.getsize(lines[0])
    linewidth, lineheight = get_text_size(font, lines[0])
    totallinesheight = lenlines * lineheight
    hstart = imgheight/2 - totallinesheight/2
    totallinesheight = 0
    
    maxlinewidth = 0
    maxlineheight = 0

    for line in lines:
        #linewidth, lineheight = font.getsize(line)
        linewidth, lineheight = get_text_size(font, line)
        if linewidth > maxlinewidth:
            maxlinewidth = linewidth
        if lineheight > maxlineheight:
            maxlineheight = lineheight
        totallinesheight += lineheight
        
    #linewidth, lineheight = font.getsize(title)
    linewidth, lineheight = get_text_size(font, title)
    totallinesheight += lineheight*3
    
    if maxlinewidth > imgwidth:
        while maxlinewidth > imgwidth:
            totallinesheight = 0
            numchars = numchars - 1
            lines = textwrap.wrap(text, width=numchars)
            lenlines = len(lines) + 2
            #linewidth, lineheight = font.getsize(lines[0])
            linewidth, lineheight = get_text_size(font, lines[0])
            #totallinesheight = lenlines * lineheight
            #hstart = imgheight/2 - totallinesheight/2
            
            maxlinewidth = 0
            maxlineheight = 0
            for line in lines:
                #linewidth, lineheight = font.getsize(line)
                linewidth, lineheight = get_text_size(font, line)
                if linewidth > maxlinewidth:
                    maxlinewidth = linewidth
                if lineheight > maxlineheight:
                    maxlineheight = lineheight
                totallinesheight += lineheight
            totallinesheight += lineheight*3
                    
    if totallinesheight > imgheight:
        while totallinesheight > imgheight:
            totallinesheight = 0
            fontsize = fontsize - 1
            font = ImageFont.truetype('arial.ttf', size=fontsize)
            lines = textwrap.wrap(text, width=numchars)
            lenlines = len(lines) + 2
            #linewidth, lineheight = font.getsize(lines[0])
            linewidth, lineheight = get_text_size(font, lines[0])
            #totallinesheight = lenlines * lineheight
            #hstart = imgheight/2 - totallinesheight/2
                
            maxlinewidth = 0
            maxlineheight = 0
            for line in lines:
                #linewidth, lineheight = font.getsize(line)
                linewidth, lineheight = get_text_size(font, line)
                if linewidth > maxlinewidth:
                    maxlinewidth = linewidth
                if lineheight > maxlineheight:
                    maxlineheight = lineheight
                totallinesheight += lineheight
            totallinesheight += lineheight*3
    
    hstart = imgheight/2 - totallinesheight/2
    y_text = hstart
    for line in lines:
        #linewidth, lineheight = font.getsize(line)
        linewidth, lineheight = get_text_size(font, line)
        if linewidth > maxlinewidth:
            maxlinewidth = linewidth
        if lineheight > maxlineheight:
            maxlineheight = lineheight
        canvas.text(((imgwidth - linewidth) / 2, y_text), line, font=font, fill=(255, 255, 255))
        y_text += lineheight
    
    #linewidth, lineheight = font.getsize(title)
    linewidth, lineheight = get_text_size(font, title)
    y_text += lineheight
    canvas.text(((imgwidth - linewidth) / 2, y_text), title, font=font, fill=(255, 255, 255))
    
    img.save(filename)
    
    if gentxt == 1:
        with open(textfileout, 'w') as f:
            f.write(Book + " Chapter " + Chapter + ":" + Verse + "\n")
            for line in lines:
                f.write(line)
                f.write(" ")
    
    #os.system(filename)
    
if __name__ == '__main__':
    twitterwidth = 1024
    twitterheight = 512
    instawidth = 1080
    instaheight = 1080
    instastorywidth = 1080
    instastoryheight = 1920
    videowidth = 1920
    videoheight = 1080

    instanumchars = 28
    instastorynumchars = 24
    videonumchars = 40
    twitternumchars = 40
    
    instafontsize = 80
    instastoryfontsize = 80
    twitterfontsize = 50

    gentxt = 0
    startchp = 1
    #Book = "2_Corinthians"
    Book = "Juan"
    numchps = 3
    #numchps = 12
    #Book = "Psalms"
    #numchps = 85
    #basedirectory = r"F:\Religious\BooksWithVideoOrig\BooksWithVideo\BooksWithVideo\newchps"
    basedirectory = r"C:\Users\empre\OneDrive\Documents\txts"
    
    for Chapter in range(startchp,startchp+numchps):

        Chapter = str(Chapter)
        filename2read = os.path.join(basedirectory,Book + "_" + Chapter + "aarm.txt")
        print(filename2read)
        with open(filename2read, 'rt') as f:
            data = f.readlines()
        for line in data:
            print(line)
            
        line = line.split(".")[0]
        print(line)
        line = line.split(":")[1]
        print(line)
                
        numverses = int(line)
        
        for verse in range(1,numverses+1):
            Verse = str(verse)
            #imgtag = "-insta-title"
            #genbibleverseimage(Book,Chapter,Verse,instawidth,instaheight,instanumchars,imgtag,instafontsize,gentxt)
        
            imgtag = "-insta-title-story"
            genbibleverseimage(Book,Chapter,Verse,instastorywidth,instastoryheight,instastorynumchars,imgtag,instastoryfontsize,gentxt,basedirectory)
            
            #imgtag = "-twitter-title"
            #genbibleverseimage(Book,Chapter,Verse,twitterwidth,twitterheight,twitternumchars,imgtag,twitterfontsize,gentxt)