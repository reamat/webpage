#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Análise de Fourier
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../../TransformadasIntegrais/AnaliseFourier

#create dest and/or clean it up
mkdir -p .in_repo-af
rm -rf .in_repo-af/*

cp -rf $DIR_MASTER/* .in_repo-af/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-af/Makefile
cp myconfig.cfg  ./.in_repo-af/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py af

#enter dest and make all local versions of the book
cd .in_repo-af
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
