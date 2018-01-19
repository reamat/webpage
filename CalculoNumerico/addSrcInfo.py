#/usr/bin/python3
# -*- coding: utf-8 -*-

# Adiciona informação sobre o path do
# código-fonte de cada capítulo e seção
#
# Author: Pedro H A Konzen - UFRGS - 01/2018

import sys
import os
from os import walk
import numpy as np
import string

sdirname = ".in_repo/"
ldir = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    for i,dir in enumerate(dirnames):
        print(dir)
        if (dir[0:4] == "cap_"):
            ldir.append (dir)
    break

for i,dir in enumerate(ldir):
    sfile = dir + "/" + dir + ".tex"
    ifile = open(sdirname + sfile, 'r')
    text = ifile.read()
    ifile.close()

    stext = "\n\\verb+srcPath:"+sfile+"+\n"

    s = text.find("\\chapter{")
    auxText = text[s:]
    e = auxText.find("}")
    otext = text[:s+e+1] + stext
    text = text[s+e+1:]

    s = text.find("\\section{")
    while (s != -1):
        auxText = text[s:]
        e = auxText.find("}")
        otext += text[:s+e+1] + stext
        text = text[s+e+1:]
        s = text.find("\\section{")

    ofile = open(sdirname + sfile, 'w')
    ofile.write(otext+text)
    ofile.close()


