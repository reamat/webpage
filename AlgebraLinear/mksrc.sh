#/usr/bin/bash

####
# Pre-compila os recursos do repositório
# de Álgebra Linear.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/AlgebraLinear

#create dest and/or clean it up
mkdir -p .in_repo
rm -rf .in_repo/*

cp -rf $DIR_MASTER/* .in_repo/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo/Makefile
cp myconfig.cfg  ./.in_repo/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#make pdf version
cd .in_repo
make clean
make pdf
cd ..

#add source infos
python3.5 addSrcInfo.py

#more notable invitations
python3.5 invitations.py

#make html version
cd .in_repo
make clean
make html
cd ..

#a nice final message
echo "Congratulation! ./AlgebraLinear/mksrc.py ended successfully. :)"
