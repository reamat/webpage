#/usr/bin/python
# -*- coding: utf-8 -*-

'''
Descricao:
Gera um sitemap no formato texto do site do projeto
Calculo Numerico - Um Livro Colaborativo
http://www.ufrgs.br/numerico

Autor: Pedro H A Konzen - 10/2016
'''

import os
from os import walk
import numpy as np
import string

ofile = open("sitemap.txt", "w")

#find and get all html
htmlFiles = []
for (dirpath, dirnames, filenames) in walk ("."):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile.write("http://www.ufrgs.br/numerico/"+filename+"\n")
    break
for (dirpath, dirnames, filenames) in walk ("./book_in_webpage"):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile.write("http://www.ufrgs.br/numerico/book_in_webpage/"+filename+"\n")
    break
ofile.close()
    



