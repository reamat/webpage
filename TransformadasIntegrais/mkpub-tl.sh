#/usr/bin/bash

#############################################
# Finaliza a compilação do livro colaborativo
# de Transformada de Laplace para publicação
# no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo-tl

#on server
DIR_SERVER=../on_server/TransformadasIntegrais

#getting and preparing Book as HTML

mkdir -p ./.book_in_html-tl
rm -rf ./.book_in_html-tl/*

cp $DIR_MASTER/html/* ./.book_in_html-tl/

mkdir -p ./$DIR_SERVER/livro-tl
mkdir -p ./.tmp-tl

rm -rf ./$DIR_SERVER/livro-tl/*
rm -rf ./.tmp-tl/*

mv ./.book_in_html-tl/*.png ./$DIR_SERVER/livro-tl/
mv ./.book_in_html-tl/*.css ./$DIR_SERVER/livro-tl/

#change encoding to utf-8
cd ./.book_in_html-tl
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp-tl/$file
done

cd ..
python3.5 goodies-tl.py

rm -rf ./.tmp-tl
rm -rf ./.book_in_html-tl

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro-tl/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

