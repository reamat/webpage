#!/bin/bash

##################################################
#
# Compila e instala o hotsite CalculoNumerico.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Cálculo Numérico
cd ./CalculoNumerico
python3 mkhs.py
./mksrc.sh
./mkpub.sh
cd ..

echo "Congratulations! ./CalculoNumerico is ready to be published. :)"
