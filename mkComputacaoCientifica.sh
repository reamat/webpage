#!/bin/bash

##################################################
#
# Compila e instala o hotsite ComputacaoCientifica.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Álgebra Linear
cd ./repos/ComputacaoCientifica
git pull
cd ../../ComputacaoCientifica
python3.5 mkhs.py
./mksrc.sh
./mkpub.sh
cd ..

echo "Congratulations! ./ComputacaoCientifica is ready to be published. :)"
