#!/bin/bash

##################################################
#
# Compila e instala o hotsite ComputacaoCientifica.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Álgebra Linear
cd ./ComputacaoCientifica
python3 mkhs.py
./mksrc.sh
./mkpub.sh
cd ..

echo "Congratulations! ./ComputacaoCientifica is ready to be published. :)"
