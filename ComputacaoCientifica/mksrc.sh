#/usr/bin/bash

####
# Pre-compila os recursos do repositório
# de Álgebra Linear.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../../ComputacaoCientifica

#create dest and/or clean it up
mkdir -p .in_repo
rm -rf .in_repo/*

cp -rf $DIR_MASTER/* .in_repo/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo/Makefile
cp myconfig.cfg  ./.in_repo/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py

#more styled invitions
python3 invitations.py

#enter dest and make all local versions of the book
cd .in_repo
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
