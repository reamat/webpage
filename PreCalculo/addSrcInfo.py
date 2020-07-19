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
    for i,filename in enumerate(filenames):
        lfn = len(filename)
        if (filename[lfn-4:] == ".tex"):
            sfile = dirpath + "/" + filename
            ifile = open(sfile, 'r')
            text = ifile.read()
            ifile.close()

            stext = "\n\\verb+#srcPath:"+sfile[len(sdirname):]+"#+\n"
            otext = ""

            s = text.find("\\chapter{")
            while (s != -1):
                auxText = text[s:]
                e = auxText.find("}")
                otext += text[:s+e+1] + stext
                text = text[s+e+1:]
                s = text.find("\\chapter{")

            s = text.find("\\chapter*{")
            while (s != -1):
                auxText = text[s:]
                e = auxText.find("}")
                otext += text[:s+e+1] + stext
                text = text[s+e+1:]
                s = text.find("\\chapter*{")

            s = text.find("\\section{")
            while (s != -1):
                auxText = text[s:]
                e = auxText.find("}")
                otext += text[:s+e+1] + stext
                text = text[s+e+1:]
                s = text.find("\\section{")

            s = text.find("\\section*{")
            while (s != -1):
                auxText = text[s:]
                e = auxText.find("}")
                otext += text[:s+e+1] + stext
                text = text[s+e+1:]
                s = text.find("\\section*{")

            ofile = open(sfile, 'w')
            ofile.write(otext+text)
            ofile.close()
