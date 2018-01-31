#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Cálculo vetorial
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../../Calculo/CV

#create dest and/or clean it up
mkdir -p .in_repo-cv
rm -rf .in_repo-cv/*

cp -rf $DIR_MASTER/* .in_repo-cv/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-cv/Makefile
cp myconfig.cfg  ./.in_repo-cv/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py cv

#add source infos
python3 invitations.py cv

#enter dest and make all local versions of the book
cd .in_repo-cv
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
