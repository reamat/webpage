#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Cálculo para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo-cfvv

#on server
DIR_SERVER=../on_server/Calculo

#getting and preparing Book as HTML

mkdir -p ./.book_in_html-cfvv
rm -rf ./.book_in_html-cfvv/*

cp $DIR_MASTER/html/* ./.book_in_html-cfvv/

mkdir -p ./$DIR_SERVER/livro-cfvv
mkdir -p ./.tmp-cfvv

rm -rf ./$DIR_SERVER/livro-cfvv/*
rm -rf ./.tmp-cfvv/*

mv ./.book_in_html-cfvv/*.png ./$DIR_SERVER/livro-cfvv/
mv ./.book_in_html-cfvv/*.css ./$DIR_SERVER/livro-cfvv/

#change encoding to utf-8
cd ./.book_in_html-cfvv
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp-cfvv/$file
done

cd ..
python3 goodies-cfvv.py

rm -rf ./.tmp-cfvv
rm -rf ./.book_in_html-cfvv

#getting PDF
cp ./$DIR_MASTER/livro.pdf ./$DIR_SERVER/livro-cfvv/livro.pdf

####################

#a nice final message
echo "You may now update the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

