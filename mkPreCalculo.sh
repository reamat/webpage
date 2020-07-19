#!/bin/bash

##################################################
#
# Compila e instala o hotsite PreCalculo.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Pré-cálculo
cd ./repos/PreCalculo
git pull
cd ../../PreCalculo
python3.5 mkhs.py
./mksrc.sh
./mkpub.sh
cd ..

echo "Congratulations! ./PreCalculo is ready to be published. :)"
