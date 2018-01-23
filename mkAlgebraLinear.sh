#!/bin/bash

##################################################
#
# Compila e instala o hotsite AlgebraLinear.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Álgebra Linear
cd ./AlgebraLinear
python3 mkhs.py
./mksrc.sh
./mkpub.sh
cd ..

echo "Congratulations! ./AlgebraLinear is ready to be published. :)"
