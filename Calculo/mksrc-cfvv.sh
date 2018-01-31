#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Cálculo de funções de várias variáveis
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/Calculo/CFVV

#create dest and/or clean it up
mkdir -p .in_repo-cfvv
rm -rf .in_repo-cfvv/*

cp -rf $DIR_MASTER/* .in_repo-cfvv/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-cfvv/Makefile
cp myconfig.cfg  ./.in_repo-cfvv/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py cfvv

#add source infos
python3 invitations.py cfvv

#enter dest and make all local versions of the book
cd .in_repo-cfvv
make clean
make pdf
make clean
make html

#back to origin folder
cd ..

#a nice final message
echo "Congratulation! ./Calculo/mksrc-cfvv.py ended successfully. :)"
