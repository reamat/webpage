#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Álgebra Linear para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo-cv

#on server
DIR_SERVER=../on_server/Calculo

#getting and preparing Book as HTML

mkdir -p ./.book_in_html-cv
rm -rf ./.book_in_html-cv/*

cp $DIR_MASTER/html/* ./.book_in_html-cv/

mkdir -p ./$DIR_SERVER/livro-cv
mkdir -p ./.tmp-cv

rm -rf ./$DIR_SERVER/livro-cv/*
rm -rf ./.tmp-cv/*

mv ./.book_in_html-cv/*.png ./$DIR_SERVER/livro-cv/
mv ./.book_in_html-cv/*.css ./$DIR_SERVER/livro-cv/

#change encoding to utf-8
cd ./.book_in_html-cv
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp-cv/$file
done

cd ..
python3 goodies-cv.py

rm -rf ./.tmp-cv
rm -rf ./.book_in_html-cv

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro-cv/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

