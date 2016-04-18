#!/bin/sh

infile=$1

name=`echo $infile | cut -d"." -f1 | sed 's/aarm//g'`

m4vfile=${name}.m4v
wavfile=${name}.wav
mp4file=${name}.mp4
dvifile=${name}.dvi

dvipng -o ${name}-%d.png -D 600 $dvifile
