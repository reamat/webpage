#/usr/bin/bash

#############################################
# This script build the version of the book
# for the webpage.
#
# Author: Pedro H A Konzen - UFRGS - 2016
#############################################

#master repo
DIR_MASTER=.book_in_repo

#getting and preparing Book as HTML

mkdir -p ./.book_in_html
rm -rf ./.book_in_html/*

cp $DIR_MASTER/html/* ./.book_in_html/

mkdir -p ./livro
mkdir -p ./.tmp

rm -rf ./livro/*
rm -rf ./.tmp/*

mv ./.book_in_html/*.png ./livro/
mv ./.book_in_html/*.css ./livro/

#google search validator
#cp googlee521115172992e66.html ./livro/

#change encoding to utf-8
cd ./.book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp/$file
done

cd ..
python tbinsert4.py

rm -rf ./.tmp
rm -rf ./.book_in_html

#getting PDF
cp $DIR_MASTER/main.pdf ./livro/main.pdf

#getting EPUB
cp $DIR_MASTER/main.epub ./livro/

#getting Slide
cp $DIR_MASTER/slide.pdf ./livro/

#update sitemap
python sitemapMaker.py

#a nice final message
echo "Congratulation! Book is already build for webpage."
echo "You may now update the webpage server."
echo "Finished."

