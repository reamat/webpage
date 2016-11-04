#/usr/bin/python
# -*- coding: utf-8 -*-

# This script changes how things look like
# from the the previous TeX4ht generated version.
#
# Author: Pedro H A Konzen - UFRGS - 2016

import os
from os import walk
import numpy as np
import string

sdirname = "./.tmp/"

lfiles = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    lfiles.extend (filenames)
    break

for index, f in enumerate (lfiles):
    lfiles[index] = os.path.splitext(f)[0]
print("Source files: ", lfiles)

listOfContents = []

#create names for hrefs in main.html
ifile = open(sdirname + "main.html", 'r')
text = ifile.read()

s = text.index('<div class="tableofcontents">')
rtext = text[s:]

s = rtext.find('href="main')
saux = s
while (saux != -1):
    auxText = rtext[s+10:]
    e = s + 10 + auxText.index('"')
    rep = 'name ="main'
    aux_e = s + 10 + auxText.find(".html")+5
    rep += rtext[s+10:aux_e] + '"'
    rep += rtext[s:aux_e]
    sub = rtext[s:e]
    rtext = rtext.replace(sub, rep)

    #add to listOfContents
    e = sub.index(".html")
    listOfContents.append((sub[6:e],sub[6:e+5]))

    s += auxText.index("</a>")
    saux = rtext[s:].find('href="main')
    s += saux
    
s = text.index('<div class="tableofcontents">')
text = text.replace(text[s:],rtext)
ifile.close()

#change title
text = text.replace('<h2 class="titleHead">Cálculo Numérico<br />',
                    '<h2 class="titleHead">Cálculo Numérico<br /><small>')
s = text.index('<h2 class="titleHead">')
auxText = text[s:]
e = s + auxText.index('</h2>')
text = text.replace(text[s:e],text[s:e]+"</small>")

ofile = open(sdirname + "main.html", 'w')
ofile.write(text)
ofile.close()

#print(text)
#raise Error("Oie")

print("listOfContents = ")
print(listOfContents)
    

for index, f in enumerate (lfiles):
    print ("Changing %s file." % (f))
    ifile = open(sdirname + f + ".html", "r")
    ofile = open("./book_in_webpage/"+f+".html", "w")

    text = ifile.read()

    #replace meta charset
    text = text.replace("iso-8859-1","utf-8")
    
    #include head
    head_aux_file = open("head.html_aux", "r")
    head_include = head_aux_file.read()
    
    #get chapterHead or sectionHead to include in <meta> keywords
    s=-1
    e=-1
    title = []
    #chapterHead
    s = text.find('<h2 class="chapterHead">')
    if (s != -1):
        auxText = text[s:]
        s = auxText.find('</a>')+4
        e = auxText.index('</h2>')
        kw = auxText[s:e]
        title = kw
    else:
        #sectionHead
        s = text.find('<h3 class="sectionHead">')
        if (s != -1):
            auxText = text[s:]
            s = auxText.find('</a>')+4
            e = auxText.index('</h3>')
            kw = auxText[s:e]
            title = kw
            #subsectionHead
            s=-1
            e=-1
            s = auxText.find('<h4 class="subsectionHead">')
            while (s != -1):
                auxText = auxText[s:]
                s = auxText.find('</a>')+4
                e = auxText.index('</h4>')
                kw += ", " + auxText[s:e]
                s = auxText.find('<h4 class="subsectionHead">',e)
        else:
            kw = []
    head1 = "<meta name='keywords' content='"
    head1 += "Livro, Cálculo Numérico, Métodos, Análise"
    if (len(kw) != 0):
        head1 += ", " + kw 
    head1 += "'>\n"
    head_include = head1 + head_include;
    
    text = text.replace("</head><body \n>", head_include)

    #hrule abaixo de h3, h4
    if ((f[0:6] == "mainse") or (f[0:6] == "mainli") or (f[0:6] == "mainch")):
        text = text.replace("</h2>",'</h2><hr class="section">')
        text = text.replace("</h3>",'</h3><hr class="section">')
        text = text.replace("</h4>",'</h4><hr class="section">')
        text = text.replace("</h5>",'</h5><hr class="section">')

    #include on bottom
    bottom_aux_file = open("bottom.html_aux", "r")
    bottom_include = bottom_aux_file.read()
    text = text.replace("</body></html>", bottom_include)

    #remove original crosslinks
    #top crosslinks
    s = text.find('<div class="crosslinks">')
    if (s != -1):
        auxText = text[s:]
        e = s + auxText.index('</div>') + 6
        text = text.replace(text[s:e], "")
    #bottom crosslinks
    s = text.find('<div class="crosslinks">')
    if (s != -1):
        auxText = text[s:]
        e = s + auxText.index('</div>') + 6
        text = text.replace(text[s:e], "")

    #configure navigation links
    if ((f[0:6] == "mainch") or (f[0:6] == "mainse") or
        (f[0:6] == "mainli") or (f[0:6] == "mainap")):

        #find file at listOfContents
        pos = -1
        for i, content in enumerate(listOfContents):
            if (content[0] == f):
                pos = i
                break
        if (pos == -1):
            print("file %s not found in listOfContents" % f)
            raise
        if (pos == 0):
            text = text.replace('#Previous#',('%s' % "main.html"))
        else:
            text = text.replace('#Previous#',('%s' % listOfContents[pos-1][1]))
        text = text.replace('#TableOfContents#',('main.html#%s.html' %f))
        if (pos == len(listOfContents)-1):
            text = text.replace('<span class="glyphicon glyphicon-chevron-right">', "")
        else:
            text = text.replace('#Next#',('%s' % listOfContents[pos+1][1]))
    else:
        text = text.replace('<span class="glyphicon glyphicon-chevron-left">', "")
        text = text.replace('<span class="glyphicon glyphicon-menu-hamburger">', "")
        text = text.replace('<span class="glyphicon glyphicon-chevron-right">', "")
        

    #sectionTOCS title
    if (f[0:6] == "mainch"):
        rep = '<div class="sectionTOCS">'
        rep += '<h3 class="sectionHead">Sumário</h3><hr class="section">'
        text = text.replace('<div class="sectionTOCS">', rep)
        
    #collapse demo's
    s = text.find("<!--prova begin-->")
    count = 0
    while (s != -1):
        count += 1
        sub =  '<div class="container-fluid">\n'
        sub += '<button type="button" class="btn btn-info" data-toggle="collapse" data-target="#demo'
        sub += str(count) + '">Demonstração</button>\n'
        sub += '<div id="demo' + str(count) + '" class="collapse out">\n'
        text = text.replace("<!--prova begin-->",sub,1)
        text = text.replace("<!--prova end-->",'</div></div>',1)
        s = text.find("<!--prova begin-->")

    #change title
    if (len(title) != 0):
        s = -1
        e = -1
        s = text.index('<title>')+7
        e = text.index('</title>')
        text = text.replace(text[s:e], title)

    ofile.write(text)
    ifile.close ()
    ofile.close ()
    head_aux_file.close()
    bottom_aux_file.close()


#change main.css
ifile = open("./book_in_webpage/main.css",'r')
bookfile = open("book.css",'r')
ofile = open("./book_in_webpage/new_main.css",'w')

for line in ifile:
    ofile.write (line)

for line in bookfile:
    ofile.write (line)

ifile.close ()
bookfile.close ()
ofile.close ()
