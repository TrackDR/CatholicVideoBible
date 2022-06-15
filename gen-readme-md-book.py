import os
 
if __name__ == '__main__':

    startchp = 1
    Book = "John"
    numchps = 21

    basedirectory = r"F:\Religious\BooksWithVideoOrig\BooksWithVideo\BooksWithVideo\newchps"
    
    print(Book)
    
    for Chapter in range(startchp,startchp+numchps):

        Chapter = str(Chapter)
        
        txtpath = "../../txts/" + Book + "_" + Chapter + "aarm.txt"
        txttxt = "[txt](" + txtpath + ")"
        
        pdfpath = "../../pdfs/" + Book + "_" + Chapter + ".pdf"
        pdftxt = "[pdf](" + pdfpath + ")"
        
        print("## " + Book + " " + Chapter + ": " + txttxt + ", " + pdftxt)
        filename2read = os.path.join(basedirectory,Book + "_" + Chapter + "aarm.txt")
        #print(filename2read)
        with open(filename2read, 'rt') as f:
            data = f.readlines()
        for line in data:
            #print(line)
            line
            
        line = line.split(".")[0]
        #print(line)
        line = line.split(":")[1]
        #print(line)
                
        numverses = int(line)
        
        for verse in range(1,numverses+1):
            Verse = str(verse)
            instapath = "../../insta/" + Book + "/" + Book + Chapter + "-" + Verse + "-insta-title.jpg"
            instatxt = "[insta]" + "(" + instapath + ")"
            
            storypath = "../../stories/" + Book + "/" + Book + Chapter + "-" + Verse + "-insta-title-story.jpg"
            storytxt = "[story]" + "(" + storypath + ")"
            
            tiktoktxt = "[tiktok]()"
            
            instagramtxt = "[instagram]()"
        
            print("- " + Verse + " " + instatxt + ", " + storytxt + ", " + tiktoktxt + ", " + instagramtxt)
