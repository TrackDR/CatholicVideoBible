#!/bin/sh


# ./convert2pdf.sh infile

infile=$1

name=`echo $infile | cut -d"." -f1 | sed 's/aarm//g'`

outfile=${name}.pdf
texfile=${name}.tex

numlines=`wc -l $infile | cut -d" " -f1`

firstname=`echo $name | cut -d"_" -f1`
mytstC=`echo $firstname | grep "Canticle"`
mytstK=`echo $firstname | cut -d" " -f1`

#if [ $name -eq "Canticle_of_Canticles" ]

if [ ! -z "$mytstC" ]
then
    book=`echo $name | cut -d"_" -f1,2,3`
    ch=`echo $name | cut -d"_" -f4`
elif [ ! -z "${mytstK##*[!0-9]*}" ]
then
    book=`echo $name | cut -d"_" -f1,2`
    ch=`echo $name | cut -d"_" -f3`
else
    book=`echo $name | cut -d"_" -f1`
    ch=`echo $name | cut -d"_" -f2`
fi

ch=`echo $ch | tr -d '.'`
book=`echo $book | sed 's/_/ /g'`

echo "\\documentclass{beamer}" > $texfile
echo "\\title{Book of $book}" >> $texfile
echo "\\author{Chapter $ch}" >> $texfile
echo "\\date{Douay-Rheims Bible}" >> $texfile
echo "\\begin{document}" >> $texfile
echo "\\begin{frame}" >> $texfile
echo " \\titlepage" >> $texfile
echo "\\end{frame}" >> $texfile
echo "\\begin{frame}[allowframebreaks]" >> $texfile

firstverse=`grep -n ":" $infile | awk -F: '{if ($2 ~ /^[0-9]+$/) print $1 }' | head -1`
firstout=`expr $firstverse - 1`
echo "firstverse: $firstverse"
echo "firstout: $firstout"

#head -4 $infile >> $texfile
head -$firstout $infile >> $texfile


echo "\\begin{itemize}" >> $texfile

x=$firstverse
echo "x: $x"
echo "numlines: $numlines"

while [ $x -le $numlines ]
do
    verse=`head -$x $infile | tail -1`
    echo "\\item[] $verse" >> $texfile
    x=`expr $x + 2`
done


echo "\\end{itemize}" >> $texfile
echo "\\end{frame}" >> $texfile
echo "\\end{document}" >> $texfile

echo "Creating pdf"
rm $outfile
pdflatex $texfile
