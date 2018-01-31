#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Cálculo de funções de uma variável
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/Calculo/CFUV

#create dest and/or clean it up
mkdir -p .in_repo-cfuv
rm -rf .in_repo-cfuv/*

cp -rf $DIR_MASTER/* .in_repo-cfuv/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-cfuv/Makefile
cp myconfig.cfg  ./.in_repo-cfuv/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py cfuv

#add source infos
python3 invitations.py cfuv

#enter dest and make all local versions of the book
cd .in_repo-cfuv
make clean
make pdf
make clean
make html

#back to origin folder
cd ..

#a nice final message
echo "Finished."
echo "INFO: You would problably like to run mkpub.sh now."
echo "Congratulation! Program ended successfully. :)"
