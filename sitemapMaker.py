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

ofile1 = open("sitemap.txt", "w")
ofile2 = open("./livro/sitemap.txt", "w")
ofile3 = open("./livro-py/sitemap.txt", "w")
ofile4 = open("./livro-oct/sitemap.txt", "w")

#find and get all html
htmlFiles = []
for (dirpath, dirnames, filenames) in walk ("."):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile1.write("https://www.ufrgs.br/numerico/"+filename+"\n")
    break
for (dirpath, dirnames, filenames) in walk ("./livro"):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile1.write("https://www.ufrgs.br/numerico/livro/"+filename+"\n")
            ofile2.write("https://www.ufrgs.br/numerico/livro/"+filename+"\n")
    break
for (dirpath, dirnames, filenames) in walk ("./livro-py"):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile1.write("https://www.ufrgs.br/numerico/livro-py/"+filename+"\n")
            ofile3.write("https://www.ufrgs.br/numerico/livro-py/"+filename+"\n")
    break
for (dirpath, dirnames, filenames) in walk ("./livro-oct"):
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if (ext == ".html"):
            ofile1.write("https://www.ufrgs.br/numerico/livro-oct/"+filename+"\n")
            ofile4.write("https://www.ufrgs.br/numerico/livro-oct/"+filename+"\n")
    break
ofile1.close()
ofile2.close()
ofile3.close()
ofile4.close()
    



