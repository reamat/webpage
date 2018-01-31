#!/bin/bash

##################################################
#
# Compila e instala o hotsite de Cálculo
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Cálculo
cd ./repos/Calculo
git pull
cd ../../Calculo
python3 mkhs.py
./mksrc-cfuv.sh
./mkpub-cfuv.sh
./mksrc-cfvv.sh
./mkpub-cfvv.sh
./mksrc-cv.sh
./mkpub-cv.sh
cd ..

echo "Congratulations! ./Calculo is ready to be published. :)"
