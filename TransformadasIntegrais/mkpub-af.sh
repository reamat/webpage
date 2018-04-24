#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Álgebra Linear para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo-af

#on server
DIR_SERVER=../on_server/TransformadasIntegrais

#getting and preparing Book as HTML

mkdir -p ./.book_in_html-af
rm -rf ./.book_in_html-af/*

cp $DIR_MASTER/html/* ./.book_in_html-af/

mkdir -p ./$DIR_SERVER/livro-af
mkdir -p ./.tmp-af

rm -rf ./$DIR_SERVER/livro-af/*
rm -rf ./.tmp-af/*

mv ./.book_in_html-af/*.png ./$DIR_SERVER/livro-af/
mv ./.book_in_html-af/*.css ./$DIR_SERVER/livro-af/

#change encoding to utf-8
cd ./.book_in_html-af
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp-af/$file
done

cd ..
python3.5 goodies-af.py

rm -rf ./.tmp-af
rm -rf ./.book_in_html-af

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro-af/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

