#/usr/bin/bash

#master repo
DIR_MASTER=../master

mkdir -p .book_in_repo

rsync -av --delete $DIR_MASTER/* .book_in_repo/

cp Makefile_example ./book_in_repo/Makefile
cp myconfig.cfg ./book_in_repo/myconfig.cfg

cd .book_in_repo
make all

cd ..

echo "Congratulation! Book is in .book_in_repo now."
echo "Finished."
echo "\nRun updateBookInWeb to update book_in_webpage."
