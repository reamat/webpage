#/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Gera um sitemap no formato texto do site
do projeto REAMAT.

http://www.ufrgs.br/reamat

Autor: Pedro H A Konzen - 01/2018
'''

import os
from os import walk
import numpy as np
import string

ofile = open("./on_server/sitemap.txt", "w")

#find and get all html
htmlFiles = []
for (dirpath, dirnames, filenames) in walk ("./on_server"):
    for (dirpath1, dirnames1, filenames1) in walk(dirpath):
        if (dirpath1[:19] != "./on_server/MathJax"):
            for filename in filenames1:
                ext = os.path.splitext(filename)[1]
                if (ext == ".html"):
                    print("%s/%s" % (dirpath1,filename))
                    ofile.write("https://www.ufrgs.br" +
                                    dirpath[11:]+"/"+filename+"\n")
            break

ofile.close()
    



