#/usr/bin/python
# -*- coding: utf-8 -*-

#just once ... I hope :(

import os
from os import walk
import string

sdirname = "./"

lfiles = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    lfiles.extend (filenames)
    break

for index, f in enumerate (lfiles):
    print(f)
    file = open(f, 'r')
    text = file.read()
    file.close()
    
    text = text.replace('livro','livro')
    file = open(f,'w')
    file.write(text)
    file.close()

print("Feito.")
