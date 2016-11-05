#/usr/bin/bash

# This script copy the important files
# from the repo to ./.book_in_repo.
#
# Author: Pedro H A Konzen - UFRGS - 11/2016

#master repo
DIR_MASTER=../master

#create dest and/or clean it up
mkdir -p .book_in_repo
rm -rf .book_in_repo/*

cp -rf $DIR_MASTER/* .book_in_repo/

#copy local Makefile and config's for Tex4ht
cp Makefile_example ./.book_in_repo/Makefile
cp myconfig.cfg  ./.book_in_repo/myconfig.cfg

#enter dest and make all local versions of the book
cd .book_in_repo
make all

#back to origin folder
cd ..

#a nice final message
echo "Congratulation! Book is in .book_in_repo now."
echo "Finished."
echo "Run updateBookInWeb to update livro."
