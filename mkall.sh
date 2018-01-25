#!/bin/bash

##################################################
#
# Compila e instala todo o site!
#
# Autor: Pedro H A Konzen - UFRGS - 01/2018
#
##################################################

#portal REAMAT
python3 mkwp.py

./mkAlgebraLinear.sh &
./mkCalculoNumerico.sh &
./mkComputacaoCientifica.sh &
./mkTransformadasIntegrais.sh &

#sitemap.txt
python3 sitemapMaker.py

echo "Congratulations! Program ended successfully. :)"
