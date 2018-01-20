#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Álgebra Linear para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo

#on server
DIR_SERVER=../on_server/AlgebraLinear

#getting and preparing Book as HTML

mkdir -p ./.book_in_html
rm -rf ./.book_in_html/*

cp $DIR_MASTER/html/* ./.book_in_html/

mkdir -p ./$DIR_SERVER/livro
mkdir -p ./.tmp

rm -rf ./$DIR_SERVER/livro/*
rm -rf ./.tmp/*

mv ./.book_in_html/*.png ./$DIR_SERVER/livro/
mv ./.book_in_html/*.css ./$DIR_SERVER/livro/

#change encoding to utf-8
cd ./.book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp/$file
done

cd ..
python3 goodies.py

rm -rf ./.tmp
rm -rf ./.book_in_html

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

