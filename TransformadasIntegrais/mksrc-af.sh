#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Análise de Fourier
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/TransformadasIntegrais/AnaliseFourier

#create dest and/or clean it up
mkdir -p .in_repo-af
rm -rf .in_repo-af/*

cp -rf $DIR_MASTER/* .in_repo-af/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-af/Makefile
cp myconfig.cfg  ./.in_repo-af/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#make pdf version
cd .in_repo-af
make clean
make pdf
cd ..

#add source infos
python3 addSrcInfo.py af

#add source infos
python3 invitations.py af

#make html version
cd .in_repo-af
make clean
make html
cd ..

#a nice final message
echo "Congratulation! ./TransformadasIntegrais/mksrc-af.sh ended successfully. :)"
