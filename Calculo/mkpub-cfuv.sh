#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Álgebra Linear para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo-cfuv

#on server
DIR_SERVER=../on_server/Calculo

#getting and preparing Book as HTML

mkdir -p ./.book_in_html-cfuv
rm -rf ./.book_in_html-cfuv/*

cp $DIR_MASTER/html/* ./.book_in_html-cfuv/

mkdir -p ./$DIR_SERVER/livro-cfuv
mkdir -p ./.tmp-cfuv

rm -rf ./$DIR_SERVER/livro-cfuv/*
rm -rf ./.tmp-cfuv/*

mv ./.book_in_html-cfuv/*.png ./$DIR_SERVER/livro-cfuv/
mv ./.book_in_html-cfuv/*.css ./$DIR_SERVER/livro-cfuv/

#change encoding to utf-8
cd ./.book_in_html-cfuv
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp-cfuv/$file
done

cd ..
python3.5 goodies-cfuv.py

rm -rf ./.tmp-cfuv
rm -rf ./.book_in_html-cfuv

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro-cfuv/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

