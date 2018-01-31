#!/bin/bash

##################################################
#
# Compila e instala o hotsite TransformadasIntegrais.
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#REAMAT - Transformadas Integrais
cd ./repos/TransformadasIntegrais
git pull
cd ../../TransformadasIntegrais
python3 mkhs.py
./mksrc-af.sh
./mkpub-af.sh
./mksrc-tl.sh
./mkpub-tl.sh
cd ..

echo "Congratulations! ./TransformadasIntegrais is ready to be published. :)"
