#/usr/bin/bash

####
# Pre-compila os o livro colaborativo
# de Transformada de Laplace
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
####

#master repo
DIR_MASTER=../repos/TransformadasIntegrais/TransformadaLaplace

#create dest and/or clean it up
mkdir -p .in_repo-tl
rm -rf .in_repo-tl/*

cp -rf $DIR_MASTER/* .in_repo-tl/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.in_repo-tl/Makefile
cp myconfig.cfg  ./.in_repo-tl/myconfig.cfg
#cp pgfsys-tex4ht.def ./.in_repo/

#add source infos
python3 addSrcInfo.py tl

#styled invitations
python3 invitations.py tl

#enter dest and make all local versions of the book
cd .in_repo-tl
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
