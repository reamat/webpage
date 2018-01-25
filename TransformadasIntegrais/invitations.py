#/usr/bin/python3

# Adiciona informação sobre o path do
# código-fonte de cada capítulo e seção
#
# Author: Pedro H A Konzen - UFRGS - 01/2018

import sys
import os
from os import walk
import numpy as np
import string

sdirname = ".in_repo-"+sys.argv[1]
ldir = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    for i,filename in enumerate(filenames):
        lfn = len(filename)
        if ((dirpath != sdirname) and filename.endswith('.tex')):
            sfile = dirpath + "/" + filename
            print(sfile)
            ifile = open(sfile, 'r')
            text = ifile.read()
            ifile.close()

            text = text.replace('\\foraDoEstilo', "+++foraDoEstilo+++")
            text = text.replace('\\emconstrucao', "+++emConstrucao+++")
            text = text.replace('\\construirSec', "+++construirSec+++")
            text = text.replace('\\construirExeresol', "+++construirExeresol+++")
            text = text.replace('\\construirResol', "+++construirResol+++")
            text = text.replace('\\construirExer', "+++construirExer+++")
            text = text.replace('\\construirResp', "+++construirResp+++")

            

            ofile = open(sfile, 'w')
            ofile.write(text)
            ofile.close()
