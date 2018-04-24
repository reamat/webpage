#/usr/bin/bash

#############################################
# Finaliza a compilação dos recursos de
# Cálculo Numérico para publicação no hotsite.
#
# Author: Pedro H A Konzen - UFRGS - 01/2018
#############################################

#master repo
DIR_MASTER=.in_repo

#on server
DIR_SERVER=../on_server/CalculoNumerico

####################
# scilab
####################

#getting and preparing Book as HTML

mkdir -p ./.book_in_html
rm -rf ./.book_in_html/*

cp $DIR_MASTER/html/* ./.book_in_html/

mkdir -p ./$DIR_SERVER/livro-sci
mkdir -p ./.tmp

rm -rf ./$DIR_SERVER/livro-sci/*
rm -rf ./.tmp/*

mv ./.book_in_html/*.png ./$DIR_SERVER/livro-sci/
mv ./.book_in_html/*.css ./$DIR_SERVER/livro-sci/

#change encoding to utf-8
cd ./.book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp/$file
done

cd ..
python3.5 goodies.py livro-sci

rm -rf ./.tmp
rm -rf ./.book_in_html

#getting PDF
cp ./$DIR_MASTER/livro-sci.pdf ./$DIR_SERVER/livro-sci/livro-sci.pdf

####################

####################
# octave
####################

#getting and preparing Book as HTML

mkdir -p ./.book_in_html
rm -rf ./.book_in_html/*

cp $DIR_MASTER/html-oct/* ./.book_in_html/

mkdir -p ./$DIR_SERVER/livro-oct
mkdir -p ./.tmp

rm -rf ./$DIR_SERVER/livro-oct/*
rm -rf ./.tmp/*

mv ./.book_in_html/*.png ./$DIR_SERVER/livro-oct/
mv ./.book_in_html/*.css ./$DIR_SERVER/livro-oct/

#change encoding to utf-8
cd ./.book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp/$file
done

cd ..
python3.5 ./goodies.py livro-oct

rm -rf ./.tmp
rm -rf ./.book_in_html

#getting PDF
cp ./$DIR_MASTER/livro-oct.pdf ./$DIR_SERVER/livro-oct/

####################


####################
# python
####################

#getting and preparing Book as HTML

mkdir -p ./.book_in_html
rm -rf ./.book_in_html/*

cp $DIR_MASTER/html-py/* ./.book_in_html/

mkdir -p ./$DIR_SERVER/livro-py
mkdir -p ./.tmp

rm -rf ./$DIR_SERVER/livro-py/*
rm -rf ./.tmp/*

mv ./.book_in_html/*.png ./$DIR_SERVER/livro-py/
mv ./.book_in_html/*.css ./$DIR_SERVER/livro-py/

#change encoding to utf-8
cd ./.book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp/$file
done

cd ..
python3.5 ./goodies.py livro-py

rm -rf ./.tmp
rm -rf ./.book_in_html

#getting PDF
cp ./$DIR_MASTER/livro-py.pdf ./$DIR_SERVER/livro-py/

####################

#a nice final message
echo "You may now update the webpage on the server."
echo "Finished."
echo "Congratulation! Program ended successfully."

