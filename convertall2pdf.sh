#!/bin/sh

# Usage ./convertall2pdf.sh fldrname
# ./convertall2pdf newchps

newfldr=$1

pushd $newfldr

rm -f *.bak
rm -f *.nav
rm -f *.out
rm -f *.log
rm -f *.snm
rm -f *.aux
rm -f *.toc
rm -f *.tex
rm -f *.pdf

files=`find -name '*aarm.txt'`

for x in $files
do
    echo $x
    name=`echo $x | sed 's/\.\///g' | cut -d"." -f1`
    echo $name
    ../convert2pdf.sh ${name}.txt
done

popd

# ./split2chps.sh 8300.txt newchps
# ./removechpcomments.sh newchps
# ./convertall2pdf.sh newchps
