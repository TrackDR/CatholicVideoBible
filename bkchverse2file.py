import os
import numpy as np

bcvinput = "Jn 6: 1-3,3-5,10,11,15-18"

verses = bcvinput.split(":")[-1]
bkch = bcvinput.split(":")[0:-1][0]
chp = bkch.split()[-1]
bk = bkch.split()[0:-1]
bk = " ".join(bk)
Book = d[bk]

splitverses = verses.replace(" ", "").split(",")
lensplitverses = len(splitverses)
verselinenums = np.array((0,1),int)
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
            
verselinenums = np.unique(verselinenums)
verselinenums = np.delete(verselinenums, 0, 0)
print(verselinenums)
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
            
numverses2write = 5
print(basename)
print(basenamebkch)

with open(basename + '.txt', 'w') as f:
    f.write(Book + " Chapter " + Chapter + ":" + verses + "\n")
    for line in verselines:
        f.write(line)
