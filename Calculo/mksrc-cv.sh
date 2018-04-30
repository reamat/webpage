#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Cálculo vetorial
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/Calculo/CV

#create dest and/or clean it up
mkdir -p .in_repo-cv
rm -rf .in_repo-cv/*

cp -rf $DIR_MASTER/* .in_repo-cv/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-cv/Makefile
cp myconfig.cfg  ./.in_repo-cv/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#make pdf version
cd .in_repo-cfuv
make clean
make pdf
cd ..

#add source infos
python3.5 addSrcInfo.py cv

#add source infos
python3.5 invitations.py cv

#make html version
cd .in_repo-cv
make clean
make html
cd ..

#a nice final message
echo "Congratulation! ./Calculo/mksrc-cv.py ended successfully. :)"
