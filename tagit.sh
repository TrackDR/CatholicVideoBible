#!/bin/sh
##
## tagit.sh
##
## Made by jer
## Login   <jer@localhost.localdomain>
##
## Started on  Tue Mar 14 23:05:56 2006 jer
## Last update Wed Mar 15 23:34:28 2006 jer
##

if [ $# -ne 3 ]
then
    echo "Usage:./tagit.sh mp3file Book Chapter"
    exit
fi

mp3file=$1
book=$2
chapter=$3

echo "$mp3file $book Ch $chapter (Douay-Rheims Bible)"

#./mp3info -t "$book Ch $chapter (Douay-Rheims Bible)" -a Jeremy -g Speech -y 2013 $mp3file
./mp3info -t "$book Ch $chapter" -l "Douay-Rheims Bible" -a Jeremy -g Speech -y 2013 $mp3file

./mp3info $mp3file
